import logging
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

from requests import RequestException
from zds_client import ClientError
from zgw_consumers.api_models.base import Model, factory
from zgw_consumers.service import get_paginated_results

from open_inwoner.openzaak.clients import build_client

logger = logging.getLogger(__name__)


@dataclass
class OpenSubmission(Model):
    url: str
    uuid: str
    naam: str
    datum_laatste_wijziging: datetime
    vervolg_link: Optional[str] = None
    eind_datum_geldigheid: Optional[datetime] = None

    @property
    def identificatie(self):
        return f"{self.naam}: {self.uuid}"

    def process_data(self):
        return {
            "url": self.url,
            "uuid": self.uuid,
            "naam": self.naam,
            "identificatie": self.identificatie,
            "vervolg_link": self.vervolg_link,
            "datum_laatste_wijziging": self.datum_laatste_wijziging,
            "eind_datum_geldigheid": self.eind_datum_geldigheid or "Geen",
        }


def fetch_open_submissions(bsn: str) -> List[OpenSubmission]:
    if not bsn:
        return []

    client = build_client("form")

    if client is None:
        return []

    try:
        response = get_paginated_results(
            client,
            "opensubmission",
            request_kwargs={"params": {"bsn": bsn}},
        )
    except (RequestException, ClientError) as e:
        logger.exception("exception while making request", exc_info=e)
        return []

    results = factory(OpenSubmission, response)

    return results
