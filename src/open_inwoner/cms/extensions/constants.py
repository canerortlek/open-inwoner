from django.utils.translation import gettext_lazy as _

from djchoices import ChoiceItem, DjangoChoices


class IndicatorChoices(DjangoChoices):
    plan_new_contacts = ChoiceItem("plan_new_contacts", _("Plans > new contacts"))
    inbox_new_messages = ChoiceItem("inbox_new_messages", _("Inbox > new messages"))
