import concurrent.futures
import enum
import functools
import logging
from dataclasses import dataclass
from typing import Callable, TypedDict

from django.http import HttpRequest
from django.urls import reverse
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView

from furl import furl
from view_breadcrumbs import BaseBreadcrumbMixin
from zgw_consumers.concurrent import parallel

from open_inwoner.htmx.mixins import RequiresHtmxMixin
from open_inwoner.openzaak.api_models import OpenSubmission, Zaak
from open_inwoner.openzaak.clients import CatalogiClient, ZakenClient
from open_inwoner.openzaak.models import (
    OpenZaakConfig,
    ZaakTypeConfig,
    ZaakTypeStatusTypeConfig,
    ZGWApiGroupConfig,
)
from open_inwoner.openzaak.types import UniformCase
from open_inwoner.openzaak.utils import get_user_fetch_parameters, is_zaak_visible
from open_inwoner.utils.mixins import PaginationMixin
from open_inwoner.utils.views import CommonPageMixin

from .mixins import CaseAccessMixin, CaseLogMixin, OuterCaseAccessMixin

logger = logging.getLogger(__name__)


class CaseFilterFormOption(enum.Enum):
    OPEN_SUBMISSION = _("Openstaande formulieren")
    OPEN_CASE = _("Lopende aanvragen")
    CLOSED_CASE = _("Afgeronde aanvragen")


@dataclass(frozen=True)
class ZaakWithApiGroup(UniformCase):
    zaak: Zaak
    api_group: ZGWApiGroupConfig

    @property
    def identification(self):
        return self.zaak.url

    def process_data(self) -> dict:
        return {**self.zaak.process_data(), "api_group": self.api_group}


@dataclass(frozen=True)
class SubmissionWithApiGroup:
    submission: OpenSubmission
    api_group: ZGWApiGroupConfig

    @property
    def identifier(self):
        return self.submission.url

    def process_data(self) -> dict:
        return {**self.submission.process_data(), "api_group": self.api_group}


class ThreadLimits(TypedDict):
    zgw_api_groups: int
    resolve_case_list: int
    resolve_case_instance: int


class CaseListService:
    request: HttpRequest
    _thread_limits: ThreadLimits
    _cumulative_case_fetching_timeout: int = 60
    _fetch_task_timeout: int = 6

    def __init__(self, request: HttpRequest):
        self.request = request

        if ZGWApiGroupConfig.objects.count() > 1:
            self._thread_limits = {
                "zgw_api_groups": 2,
                "resolve_case_list": 1,
                "resolve_case_instance": 3,
            }
        else:
            self._thread_limits = {
                "zgw_api_groups": 1,
                "resolve_case_list": 2,
                "resolve_case_instance": 3,
            }

        logger.info("Configured thread limits as %s", self._thread_limits)

    def get_submissions_for_api_group(
        self, group: ZGWApiGroupConfig
    ) -> list[UniformCase]:
        return group.forms_client.fetch_open_submissions(
            **get_user_fetch_parameters(self.request, check_rsin=False)
        )

    def get_submissions(self):
        all_api_groups = list(
            ZGWApiGroupConfig.objects.exclude(form_service__isnull=True)
        )

        with parallel() as executor:
            futures = [
                executor.submit(self.get_submissions_for_api_group, group)
                for group in all_api_groups
            ]

            subs_with_api_group = []
            for task in concurrent.futures.as_completed(futures):
                try:
                    group_for_task = all_api_groups[futures.index(task)]
                    for row in task.result():
                        subs_with_api_group.append(
                            SubmissionWithApiGroup(
                                submission=row, api_group=group_for_task
                            )
                        )
                except BaseException:
                    logger.exception("Error fetching and pre-processing cases")

        # Sort submissions by date modified
        subs_with_api_group.sort(
            key=lambda sub: sub.submission.datum_laatste_wijziging, reverse=True
        )

        return subs_with_api_group

    @staticmethod
    def get_case_filter_status(zaak: Zaak) -> CaseFilterFormOption:
        if zaak.einddatum:
            return CaseFilterFormOption.CLOSED_CASE

        return CaseFilterFormOption.OPEN_CASE

    def get_case_status_frequencies(self) -> dict[CaseFilterFormOption, int]:
        cases = self.get_cases()
        submissions = self.get_submissions()

        case_statuses = [self.get_case_filter_status(case.zaak) for case in cases]

        # add static text for open submissions
        case_statuses += [CaseFilterFormOption.OPEN_SUBMISSION for _ in submissions]

        return {
            status: case_statuses.count(status) for status in list(CaseFilterFormOption)
        }

    def get_cases(self) -> list[ZaakWithApiGroup]:
        all_api_groups = list(ZGWApiGroupConfig.objects.all())

        with parallel(max_workers=self._thread_limits["zgw_api_groups"]) as executor:
            futures = [
                executor.submit(self._get_cases_for_api_group, group)
                for group in all_api_groups
            ]

            cases_with_api_group = []
            for task in concurrent.futures.as_completed(
                futures,
                timeout=self._cumulative_case_fetching_timeout,
            ):
                group_for_task = all_api_groups[futures.index(task)]
                try:
                    for row in task.result():
                        cases_with_api_group.append(
                            ZaakWithApiGroup(zaak=row, api_group=group_for_task)
                        )
                except BaseException:
                    logger.exception(
                        "Error while fetching and pre-processing cases for API group %s",
                        group_for_task,
                    )

        # Ensure stable sorting for pagination and testing purposes
        cases_with_api_group.sort(key=lambda c: all_api_groups.index(c.api_group))

        return cases_with_api_group

    def _get_cases_for_api_group(self, group: ZGWApiGroupConfig):
        raw_cases = group.zaken_client.fetch_cases(
            **get_user_fetch_parameters(self.request)
        )
        preprocessed_cases = self.resolve_cases(raw_cases, group)
        return preprocessed_cases

    def resolve_cases(
        self,
        cases: list[Zaak],
        group: ZGWApiGroupConfig,
    ) -> list[Zaak]:
        with parallel(max_workers=self._thread_limits["resolve_case_list"]) as executor:
            futures = [
                executor.submit(self.resolve_case, case, group) for case in cases
            ]

            concurrent.futures.wait(futures, timeout=self._fetch_task_timeout)

        cases = [case for case in cases if case.status and is_zaak_visible(case)]
        cases.sort(key=lambda case: case.startdatum, reverse=True)

        return cases

    def resolve_case(self, case: Zaak, group: ZGWApiGroupConfig):
        logger.debug("Resolving case %s with group %s", case.identificatie, group)

        functions = [
            functools.partial(
                self._resolve_resultaat_and_resultaat_type,
                zaken_client=group.zaken_client,
                catalogi_client=group.catalogi_client,
            ),
            functools.partial(
                self._resolve_status_and_status_type,
                zaken_client=group.zaken_client,
                catalogi_client=group.catalogi_client,
            ),
            functools.partial(
                self._resolve_zaak_type,
                client=group.catalogi_client,
            ),
        ]

        # use contextmanager to ensure the `requests.Session` is reused
        with group.catalogi_client, group.zaken_client:
            with parallel(
                max_workers=self._thread_limits["resolve_case_instance"]
            ) as executor:
                futures = [executor.submit(func, case) for func in functions]

            for task in concurrent.futures.as_completed(
                futures, timeout=self._fetch_task_timeout
            ):
                if exc := task.exception():
                    logger.error("Error in resolving case: %s", exc, stack_info=True)

                update_case = task.result()
                if hasattr(update_case, "__call__"):
                    update_case(case)

        try:
            zaaktype_config = ZaakTypeConfig.objects.filter_case_type(
                case.zaaktype
            ).get()

            case.zaaktype_config = zaaktype_config

            if zaaktype_config:
                statustype_config = ZaakTypeStatusTypeConfig.objects.get(
                    zaaktype_config=zaaktype_config,
                    statustype_url=case.status.statustype.url,
                )
                case.statustype_config = statustype_config
        except (
            ZaakTypeConfig.DoesNotExist,
            AttributeError,
            ZaakTypeStatusTypeConfig.DoesNotExist,
        ):
            logger.exception(
                "Unable to resolve zaaktype_config and statustype_config for case %s",
                case.identificatie,
                exc_info=True,
            )

    @staticmethod
    def _resolve_zaak_type(
        case: Zaak, *, client: CatalogiClient
    ) -> Callable[[Zaak], None] | None:
        """
        Resolve `case.zaaktype` (`str`) to a `ZaakType(ZGWModel)` object

        Note: the result of `fetch_single_case_type` is cached, hence a request
            is only made for new case type urls
        """
        if not isinstance(case.zaaktype, str):
            logger.debug("Case %s already has a resolved zaaktype", case.identificatie)
            return

        case_type = client.fetch_single_case_type(case.zaaktype)
        if not case_type:
            logger.error("Unable to resolve zaaktype for url: %s", case.zaaktype)
            return

        def setter(target_case: Zaak):
            target_case.zaaktype = case_type

        return setter

    @staticmethod
    def _resolve_status_and_status_type(
        case: Zaak, *, zaken_client: ZakenClient, catalogi_client: CatalogiClient
    ) -> Callable[[Zaak], None] | None:
        if not isinstance(case.status, str):
            logger.error(
                "`case.status` for case %s is not a str but %s",
                case.identificatie,
                type(case.status),
            )
            return

        status = zaken_client.fetch_single_status(case.status)
        if not status:
            logger.error(
                "Unable to resolve status %s for case %s",
                case.status,
                case.identificatie,
            )
            return None

        status_type = catalogi_client.fetch_single_status_type(status.statustype)
        if not status_type:
            logger.error(
                "Unable to resolve status_type %s for case %s",
                status.statustype,
                case.identificatie,
            )
            return None

        def setter(target_case: Zaak):
            target_case.status = status
            target_case.status.statustype = status_type

        return setter

    @staticmethod
    def _resolve_resultaat_and_resultaat_type(
        case: Zaak, *, zaken_client: ZakenClient, catalogi_client: CatalogiClient
    ) -> Callable[[Zaak], None] | None:
        if case.resultaat is None:
            return

        if not isinstance(case.resultaat, str):
            logger.error(
                "`case.resultaat` for case %s is not a str but %s",
                case.identificatie,
                type(case.resultaat),
            )
            return

        resultaat = zaken_client.fetch_single_result(case.resultaat)
        if not resultaat:
            logger.error("Unable to fetch resultaat for %s", case)
            return

        resultaattype = catalogi_client.fetch_single_resultaat_type(
            resultaat.resultaattype
        )
        if not resultaattype:
            logger.error(
                "Unable to resolve resultaattype for %s", resultaat.resultaattype
            )
            return

        def setter(target_case: Zaak):
            target_case.resultaat = resultaat
            target_case.resultaat.resultaattype = resultaattype

        return setter


class OuterCaseListView(
    OuterCaseAccessMixin, CommonPageMixin, BaseBreadcrumbMixin, TemplateView
):
    """View on the case list while content is loaded via htmx"""

    template_name = "pages/cases/list_outer.html"

    @cached_property
    def crumbs(self):
        return [
            (_("Mijn aanvragen"), reverse("cases:index")),
        ]

    def page_title(self):
        return _("Mijn aanvragen")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        statuses = self.request.GET.getlist("status")

        f_url = furl(reverse("cases:cases_content"))
        f_url.args.addlist("status", statuses)

        context["hxget"] = f_url.url
        return context


class InnerCaseListView(
    RequiresHtmxMixin,
    CommonPageMixin,
    CaseAccessMixin,
    CaseLogMixin,
    PaginationMixin,
    TemplateView,
):
    template_name = "pages/cases/list_inner.html"
    paginate_by = 9

    def page_title(self):
        return _("Mijn aanvragen")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        config = OpenZaakConfig.get_solo()
        case_service = CaseListService(self.request)
        context["filter_form_enabled"] = config.zaken_filter_enabled

        # update ctx with open submissions and cases (possibly fitered)
        open_submissions: list[UniformCase] = case_service.get_submissions()
        preprocessed_cases: list[UniformCase] = case_service.get_cases()

        if config.zaken_filter_enabled:
            case_status_frequencies = case_service.get_case_status_frequencies()
            # Separate frequency data from statusname
            context["status_freqs"] = [
                (status.value, frequency)
                for status, frequency in case_status_frequencies.items()
            ]

            # Validate statuses are valid according to the options enum
            statuses: list[CaseFilterFormOption] = []
            for status in self.request.GET.getlist("status"):
                try:
                    statuses.append(CaseFilterFormOption(status))
                except ValueError:
                    logger.error(
                        "Invalid data (%s) for case filtering by %s",
                        self.request.GET,
                        self.request.user,
                    )

            # Actually filter the submissions
            if statuses:
                open_submissions = (
                    open_submissions
                    if CaseFilterFormOption.OPEN_SUBMISSION in statuses
                    else []
                )
                preprocessed_cases = [
                    case
                    for case in preprocessed_cases
                    if case_service.get_case_filter_status(case.zaak) in statuses
                ]

        paginator_dict = self.paginate_with_context(
            [*open_submissions, *preprocessed_cases]
        )
        case_dicts = [case.process_data() for case in paginator_dict["object_list"]]

        context["cases"] = case_dicts
        context.update(paginator_dict)

        self.log_access_cases(case_dicts)

        # other data
        context["hxget"] = reverse("cases:cases_content")
        context["title_text"] = config.title_text

        return context
