import os
from datetime import date

from django.utils.translation import gettext_lazy as _


def _readfile(name):
    p = os.path.join(os.path.dirname(__file__), name)
    with open(p) as f:
        return f.read()


# mail-editor
MAIL_EDITOR_CONF = {
    "invite": {
        "name": _("Invitation Email"),
        "description": _(
            "This email is used to invite people to sing up to the website"
        ),
        "subject_default": "Uitnodiging voor {{ site_name }}",
        "body_default": _readfile("invite.html"),
        "subject": [
            {
                "name": "site_name",
                "description": _("Name of the site."),
            },
            {"name": "inviter_name", "description": _("Full name of the inviter")},
        ],
        "body": [
            {
                "name": "inviter_name",
                "description": _("Full name of the inviter"),
            },
            {
                "name": "site_name",
                "description": _("Name of the site"),
            },
            {
                "name": "invite_link",
                "description": _("Link to activate their account."),
            },
            {"name": "email", "description": _("Email of the invited user")},
            {
                "name": "contact_page",
                "description": _("The link to an existing contactpage"),
            },
            {
                "name": "contact_phonenumber",
                "description": _("The callable link to the configured phonenumber"),
                "example": "14010",
            },
        ],
    },
    "contact_approval": {
        "name": _("Contact Approval Email"),
        "description": _(
            "This email is used to notify people for pending approvals of new contacts"
        ),
        "subject_default": "Goedkeuring geven op {{ site_name }}: {{ sender_name }} wil u toevoegen als contactpersoon",
        "body_default": _readfile("contact_approval.html"),
        "subject": [
            {
                "name": "site_name",
                "description": _("Name of the site."),
            },
            {
                "name": "sender_name",
                "description": _("Full name of the inviter-sender"),
            },
        ],
        "body": [
            {
                "name": "sender_name",
                "description": _("Full name of the inviter-sender"),
            },
            {
                "name": "site_name",
                "description": _("Name of the site"),
            },
            {
                "name": "contacts_link",
                "description": _("Link to contact list page."),
            },
            {"name": "email", "description": _("Email of the receiver user")},
            {
                "name": "contact_page",
                "description": _("The link to an existing contactpage"),
            },
            {
                "name": "contact_phonenumber",
                "description": _("The callable link to the configured phonenumber"),
                "example": "14010",
            },
            {
                "name": "profile_notifications",
                "description": _(
                    "The link to the notifications and unsubscribe settings"
                ),
            },
        ],
    },
    "new_messages": {
        "name": _("New Message Email"),
        "description": _(
            "This email is used to inform users about the new messages in their inbox"
        ),
        "subject_default": "Nieuwe berichten op {{ site_name }}",
        "body_default": _readfile("new_messages.html"),
        "subject": [
            {
                "name": "site_name",
                "description": _("Name of the site."),
            },
        ],
        "body": [
            {
                "name": "total_messages",
                "description": _("Number of the new messages"),
            },
            {
                "name": "total_senders",
                "description": _("Number of the senders"),
            },
            {
                "name": "site_name",
                "description": _("Name of the site"),
            },
            {
                "name": "inbox_link",
                "description": _("Link to see the conversation."),
            },
            {
                "name": "contact_page",
                "description": _("The link to an existing contactpage"),
            },
            {
                "name": "contact_phonenumber",
                "description": _("The callable link to the configured phonenumber"),
                "example": "14010",
            },
            {
                "name": "profile_notifications",
                "description": _(
                    "The link to the notifications and unsubscribe settings"
                ),
            },
        ],
    },
    "expiring_action": {
        "name": _("Action end date today"),
        "description": _(
            "This email is used to remind users that there are actions that are ending today"
        ),
        "subject_default": "Acties verlopen vandaag op {{ site_name }}",
        "body_default": _readfile("expiring_action.html"),
        "subject": [
            {
                "name": "site_name",
                "description": _("Name of the site."),
            },
        ],
        "body": [
            {
                "name": "actions",
                "description": _("A list of actions that will expire today"),
            },
            {
                "name": "actions_link",
                "description": _("The link to your actions page."),
            },
            {
                "name": "site_name",
                "description": _("Name of the site"),
            },
            {
                "name": "contact_page",
                "description": _("The link to an existing contactpage"),
            },
            {
                "name": "contact_phonenumber",
                "description": _("The callable link to the configured phonenumber"),
                "example": "14010",
            },
            {
                "name": "profile_notifications",
                "description": _(
                    "The link to the notifications and unsubscribe settings"
                ),
            },
        ],
    },
    "expiring_plan": {
        "name": _("Plan end date today"),
        "description": _(
            "This email is used to remind users that there are plans that are ending today"
        ),
        "subject_default": "Plannen vervallen vandaag op {{ site_name }}",
        "body_default": _readfile("expiring_plan.html"),
        "subject": [
            {
                "name": "site_name",
                "description": _("Name of the site."),
            },
        ],
        "body": [
            {
                "name": "plans",
                "description": _("A list of plans that will expire today"),
            },
            {
                "name": "plan_list_link",
                "description": _("The link to your plans page."),
            },
            {
                "name": "site_name",
                "description": _("Name of the site"),
            },
            {
                "name": "contact_page",
                "description": _("The link to an existing contactpage"),
            },
            {
                "name": "contact_phonenumber",
                "description": _("The callable link to the configured phonenumber"),
                "example": "14010",
            },
            {
                "name": "profile_notifications",
                "description": _(
                    "The link to the notifications and unsubscribe settings"
                ),
            },
        ],
    },
    "plan_action_update": {
        "name": _("Plan action update"),
        "description": _(
            "This email is used to notify plan participants about the change in the plan action"
        ),
        "subject_default": "Samenwerkingsactie bijgewerkt op {{ site_name }}",
        "body_default": _readfile("plan_action_update.html"),
        "subject": [
            {
                "name": "site_name",
                "description": _("Name of the site."),
            },
        ],
        "body": [
            {
                "name": "action",
                "description": _("Action that was updated"),
            },
            {
                "name": "plan",
                "description": _("Plan the updated action belongs to"),
            },
            {
                "name": "plan_url",
                "description": _("The link to the plan."),
            },
            {
                "name": "site_name",
                "description": _("Name of the site"),
            },
            {
                "name": "contact_page",
                "description": _("The link to an existing contactpage"),
            },
            {
                "name": "contact_phonenumber",
                "description": _("The callable link to the configured phonenumber"),
                "example": "14010",
            },
            {
                "name": "profile_notifications",
                "description": _(
                    "The link to the notifications and unsubscribe settings"
                ),
            },
        ],
    },
    "case_status_notification": {
        "name": _("Case status update notification"),
        "description": _(
            "This email is used to notify people about a new status being set on their case"
        ),
        "subject_default": "Uw zaak is bijgewerkt op {{ site_name }}",
        "body_default": _readfile("case_status_notification.html"),
        "subject": [
            {
                "name": "site_name",
                "description": _("Name of the site."),
            },
        ],
        "body": [
            {
                "name": "identification",
                "description": _("The identification of the case"),
                "example": "ZAAK-1234",
            },
            {
                "name": "type_description",
                "description": _("The description of the type of the case"),
                "example": _("Casetype placeholder"),
            },
            {
                "name": "status_description",
                "description": _("The description of the status of the case"),
                "example": _("status placeholder"),
            },
            {
                "name": "end_date",
                "description": _("The planned final date of the case"),
                "example": date(2024, 5, 1),
            },
            {
                "name": "case_link",
                "description": _("The link to the case details."),
            },
            {
                "name": "site_name",
                "description": _("Name of the site"),
            },
            {
                "name": "contact_page",
                "description": _("The link to an existing contactpage"),
            },
            {
                "name": "contact_phonenumber",
                "description": _("The callable link to the configured phonenumber"),
            },
            {
                "name": "profile_notifications",
                "description": _(
                    "The link to the notifications and unsubscribe settings"
                ),
            },
            {
                "name": "profile_page",
                "description": _("The link to the user's profile page"),
            },
            {
                "name": "login_page",
                "description": _("The link to the login page"),
            },
        ],
    },
    "case_document_notification": {
        "name": _("Case document update notification"),
        "description": _(
            "This email is used to notify people that a new document was added to their case"
        ),
        "subject_default": "Uw zaak is bijgewerkt op {{ site_name }}",
        "body_default": _readfile("case_document_notification.html"),
        "subject": [
            {
                "name": "site_name",
                "description": _("Name of the site."),
            },
        ],
        "body": [
            {
                "name": "identification",
                "description": _("The identification of the case"),
                "example": "ZAAK-1234",
            },
            {
                "name": "type_description",
                "description": _("The description of the type of the case"),
                "example": _("Casetype placeholder"),
            },
            {
                "name": "start_date",
                "description": _("The start date of the case"),
                "example": date(2024, 5, 1),
            },
            {
                "name": "case_link",
                "description": _("The link to the case details."),
            },
            {
                "name": "site_name",
                "description": _("Name of the site"),
            },
            {
                "name": "contact_page",
                "description": _("The link to an existing contactpage"),
            },
            {
                "name": "contact_phonenumber",
                "description": _("The callable link to the configured phonenumber"),
            },
            {
                "name": "profile_notifications",
                "description": _(
                    "The link to the notifications and unsubscribe settings"
                ),
            },
        ],
    },
    "case_status_notification_action_required": {
        "name": _("Case status update notification (action required)"),
        "description": _(
            "This email is used to notify people about a new status being set on their case "
            "that requires action on their part."
        ),
        "subject_default": "Uw zaak is bijgewerkt op {{ site_name }} (actie vereist)",
        "body_default": _readfile("case_status_notification_action_required.html"),
        "subject": [
            {
                "name": "site_name",
                "description": _("Name of the site."),
            },
        ],
        "body": [
            {
                "name": "identification",
                "description": _("The identification of the case"),
                "example": "ZAAK-1234",
            },
            {
                "name": "type_description",
                "description": _("The description of the type of the case"),
                "example": _("Casetype placeholder"),
            },
            {
                "name": "status_description",
                "description": _("The description of the status of the case"),
                "example": _("status placeholder"),
            },
            {
                "name": "case_link",
                "description": _("The link to the case details."),
            },
            {
                "name": "end_date",
                "description": _("The planned final date of the case"),
                "example": date(2024, 5, 1),
            },
            {
                "name": "site_name",
                "description": _("Name of the site"),
            },
            {
                "name": "contact_page",
                "description": _("The link to an existing contactpage"),
            },
            {
                "name": "contact_phonenumber",
                "description": _("The callable link to the configured phonenumber"),
            },
            {
                "name": "profile_notifications",
                "description": _(
                    "The link to the notifications and unsubscribe settings"
                ),
            },
        ],
    },
    "contactform_confirmation": {
        "name": _("Contact form confirmation notification"),
        "description": _("This email is used to inform on a contact form reply"),
        "subject_default": "Vraag ontvangen op {{ site_name }}",
        "body_default": _readfile("contactform_confirmation.html"),
        "subject": [
            {
                "name": "site_name",
                "description": _("Name of the site."),
            },
        ],
        "body": [
            {
                "name": "subject",
                "description": _("Onderwerp"),
                "example": "Placeholder onderwerp",
            },
            {
                "name": "site_name",
                "description": _("Naam van de site"),
            },
            {
                "name": "contact_page",
                "description": _("De link naar een bestaande contactpagina"),
            },
            {
                "name": "contact_phonenumber",
                "description": _("Telefoonnummer van de organisatie"),
            },
            {
                "name": "profile_notifications",
                "description": _("De link naar de notificatievoorkeuren pagina"),
            },
        ],
    },
    "contactform_registration": {
        "name": _("Contact form registration notification"),
        "description": _("This email is used to register a contact form submission"),
        "subject_default": "Contact formulier inzending vanaf {{ site_name }}",
        "body_default": _readfile("contactform_registration.html"),
        "subject": [
            {
                "name": "site_name",
                "description": _("Name of the site."),
            },
        ],
        "body": [
            {
                "name": "subject",
                "description": _("Onderwerp"),
            },
            {
                "name": "name",
                "description": _("Naam"),
            },
            {
                "name": "email",
                "description": _("E-mailadres"),
            },
            {
                "name": "phonenumber",
                "description": _("Telefoonnummer"),
            },
            {
                "name": "question",
                "description": _("Vraag"),
            },
        ],
    },
    "daily_email_digest": {
        "name": _("Inform admin about failed emails"),
        "description": _(
            "This email is used to periodically inform an admin about failed emails"
        ),
        "subject_default": "Gefaalde emails voor {{ site_name }} ({{ date }})",
        "body_default": _readfile("daily_email_digest.html"),
        "subject": [
            {
                "name": "site_name",
                "description": _("Name of the site."),
            },
            {
                "name": "date",
                "description": _("The date for which failed emails are reported"),
            },
        ],
        "body": [
            {
                "name": "date",
                "description": _("The date for which failed emails are reported"),
            },
            {
                "name": "failed_emails",
                "description": _("List of failed emails"),
            },
        ],
    },
    "email_verification": {
        "name": _("Email address verification"),
        "description": _("This email is used by users to verify their email address"),
        "subject_default": _("Bevestig je e-mailadres voor {{ site_name }}"),
        "body_default": _readfile("email_verification.html"),
        "subject": [
            {
                "name": "site_name",
                "description": _("Name of the site."),
            },
        ],
        "body": [
            {
                "name": "verification_link",
                "description": _("Link to confirm email address"),
            },
            {
                "name": "site_name",
                "description": _("Name of the site"),
            },
        ],
    },
}
MAIL_EDITOR_BASE_CONTEXT = {"site_name": "Open Inwoner Platform"}
MAIL_EDITOR_DYNAMIC_CONTEXT = "open_inwoner.mail.context.mail_context"
