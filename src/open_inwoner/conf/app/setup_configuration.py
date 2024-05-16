from ..utils import config

SETUP_CONFIGURATION_STEPS = [
    "open_inwoner.configurations.bootstrap.zgw.ZakenAPIConfigurationStep",
    "open_inwoner.configurations.bootstrap.zgw.CatalogiAPIConfigurationStep",
    "open_inwoner.configurations.bootstrap.zgw.DocumentenAPIConfigurationStep",
    "open_inwoner.configurations.bootstrap.zgw.FormulierenAPIConfigurationStep",
    "open_inwoner.configurations.bootstrap.zgw.ZGWAPIsConfigurationStep",
    "open_inwoner.configurations.bootstrap.kic.KlantenAPIConfigurationStep",
    "open_inwoner.configurations.bootstrap.kic.ContactmomentenAPIConfigurationStep",
    "open_inwoner.configurations.bootstrap.kic.KICAPIsConfigurationStep",
    "open_inwoner.configurations.bootstrap.siteconfig.SiteConfigurationStep",
    "open_inwoner.configurations.bootstrap.auth.DigiDOIDCConfigurationStep",
    "open_inwoner.configurations.bootstrap.auth.eHerkenningOIDCConfigurationStep",
    "open_inwoner.configurations.bootstrap.auth.AdminOIDCConfigurationStep",
    "open_inwoner.configurations.bootstrap.auth.DigiDConfigurationStep",
    "open_inwoner.configurations.bootstrap.auth.eHerkenningConfigurationStep",
]
OIP_ORGANIZATION = config("OIP_ORGANIZATION", "")

# ZGW configuration variables
ZGW_ENABLE = config("ZGW_ENABLE", default=True)
ZGW_SERVER_CERTIFICATE_LABEL = config("ZGW_CONFIG_SERVER_CERTIFICATE_LABEL", "")
ZGW_SERVER_CERTIFICATE_TYPE = config("ZGW_CONFIG_SERVER_CERTIFICATE_TYPE", "")
ZGW_SERVER_CERTIFICATE_PUBLIC_CERTIFICATE = (
    "ZGW_CONFIG_SERVER_CERTIFICATE_PUBLIC_CERTIFICATE", None,
)
ZGW_ZAAK_SERVICE_API_ROOT = config("ZGW_ZAAK_SERVICE_API_ROOT", "")
if ZGW_ZAAK_SERVICE_API_ROOT and not ZGW_ZAAK_SERVICE_API_ROOT.endswith("/"):
    ZGW_ZAAK_SERVICE_API_ROOT = f"{ZGW_ZAAK_SERVICE_API_ROOT.strip()}/"
ZGW_ZAKEN_OAS_URL = ZGW_ZAAK_SERVICE_API_ROOT  # this is still required by the form, but not actually used
ZGW_ZAAK_SERVICE_API_CLIENT_ID = config("ZGW_ZAAK_SERVICE_API_CLIENT_ID", "")
ZGW_ZAAK_SERVICE_API_SECRET = config("ZGW_ZAAK_SERVICE_API_SECRET", "")
ZGW_CATALOGI_SERVICE_API_ROOT = config("ZGW_CATALOGI_SERVICE_API_ROOT", "")
if ZGW_CATALOGI_SERVICE_API_ROOT and not ZGW_CATALOGI_SERVICE_API_ROOT.endswith("/"):
    ZGW_CATALOGI_SERVICE_API_ROOT = f"{ZGW_CATALOGI_SERVICE_API_ROOT.strip()}/"
ZGW_CATALOGI_OAS_URL = ZGW_CATALOGI_SERVICE_API_ROOT  # this is still required by the form, but not actually used
ZGW_CATALOGI_SERVICE_API_CLIENT_ID = config("ZGW_CATALOGI_SERVICE_API_CLIENT_ID", "")
ZGW_CATALOGI_SERVICE_API_SECRET = config("ZGW_CATALOGI_SERVICE_API_SECRET", "")
ZGW_DOCUMENTEN_SERVICE_API_ROOT = config("ZGW_DOCUMENTEN_SERVICE_API_ROOT", "")
if ZGW_DOCUMENTEN_SERVICE_API_ROOT and not ZGW_DOCUMENTEN_SERVICE_API_ROOT.endswith(
    "/"
):
    ZGW_DOCUMENTEN_SERVICE_API_ROOT = f"{ZGW_DOCUMENTEN_SERVICE_API_ROOT.strip()}/"
ZGW_DOCUMENTEN_OAS_URL = ZGW_DOCUMENTEN_SERVICE_API_ROOT  # this is still required by the form, but not actually used
ZGW_DOCUMENTEN_SERVICE_API_CLIENT_ID = config(
    "ZGW_DOCUMENTEN_SERVICE_API_CLIENT_ID", ""
)
ZGW_DOCUMENTEN_SERVICE_API_SECRET = config("ZGW_DOCUMENTEN_SERVICE_API_SECRET", "")
ZGW_FORM_SERVICE_API_ROOT = config("ZGW_FORM_SERVICE_API_ROOT", "")
if ZGW_FORM_SERVICE_API_ROOT and not ZGW_FORM_SERVICE_API_ROOT.endswith("/"):
    ZGW_FORM_SERVICE_API_ROOT = f"{ZGW_FORM_SERVICE_API_ROOT.strip()}/"
ZGW_FORMULIEREN_OAS_URL = ZGW_FORM_SERVICE_API_ROOT  # this is still required by the form, but not actually used
ZGW_FORM_SERVICE_API_CLIENT_ID = config("ZGW_FORM_SERVICE_API_CLIENT_ID", "")
ZGW_FORM_SERVICE_API_SECRET = config("ZGW_FORM_SERVICE_API_SECRET", "")
# ZGW config options
ZGW_ZAAK_MAX_CONFIDENTIALITY = config("ZGW_ZAAK_MAX_CONFIDENTIALITY", None)
ZGW_DOCUMENT_MAX_CONFIDENTIALITY = config("ZGW_DOCUMENT_MAX_CONFIDENTIALITY", None)
ZGW_ACTION_REQUIRED_DEADLINE_DAYS = config("ACTION_REQUIRED_DEADLINE_DAYS", None)
ZGW_ALLOWED_FILE_EXTENSIONS = config("ZGW_ALLOWED_FILE_EXTENSIONS", None)
ZGW_MIJN_AANVRAGEN_TITLE_TEXT = config("ZGW_MIJN_AANVRAGEN_TITLE_TEXT", None)
ZGW_ENABLE_CATEGORIES_FILTERING_WITH_ZAKEN = config(
    "ZGW_ENABLE_CATEGORIES_FILTERING_WITH_ZAKEN", None
)
ZGW_SKIP_NOTIFICATION_STATUSTYPE_INFORMEREN = config(
    "ZGW_SKIP_NOTIFICATION_STATUSTYPE_INFORMEREN", None
)
ZGW_REFORMAT_ESUITE_ZAAK_IDENTIFICATIE = config(
    "ZGW_REFORMAT_ESUITE_ZAAK_IDENTIFICATIE", None
)
ZGW_FETCH_EHERKENNING_ZAKEN_WITH_RSIN = config(
    "ZGW_FETCH_EHERKENNING_ZAKEN_WITH_RSIN", None
)

# KIC configuration variables
KIC_ENABLE = config("KIC_ENABLE", default=True)
KIC_KLANTEN_SERVICE_API_ROOT = config("KIC_KLANTEN_SERVICE_API_ROOT", "")
if KIC_KLANTEN_SERVICE_API_ROOT and not KIC_KLANTEN_SERVICE_API_ROOT.endswith("/"):
    KIC_KLANTEN_SERVICE_API_ROOT = f"{KIC_KLANTEN_SERVICE_API_ROOT.strip()}/"
KIC_KLANTEN_OAS_URL = KIC_KLANTEN_SERVICE_API_ROOT  # this is still required by the form, but not actually used
KIC_KLANTEN_SERVICE_API_CLIENT_ID = config("KIC_KLANTEN_SERVICE_API_CLIENT_ID", "")
KIC_KLANTEN_SERVICE_API_SECRET = config("KIC_KLANTEN_SERVICE_API_SECRET", "")
KIC_CONTACTMOMENTEN_SERVICE_API_ROOT = config(
    "KIC_CONTACTMOMENTEN_SERVICE_API_ROOT", ""
)
if (
    KIC_CONTACTMOMENTEN_SERVICE_API_ROOT
    and not KIC_CONTACTMOMENTEN_SERVICE_API_ROOT.endswith("/")
):
    KIC_CONTACTMOMENTEN_SERVICE_API_ROOT = (
        f"{KIC_CONTACTMOMENTEN_SERVICE_API_ROOT.strip()}/"
    )
KIC_CONTACTMOMENTEN_OAS_URL = KIC_CONTACTMOMENTEN_SERVICE_API_ROOT  # this is still required by the form, but not actually used
KIC_CONTACTMOMENTEN_SERVICE_API_CLIENT_ID = config(
    "KIC_CONTACTMOMENTEN_SERVICE_API_CLIENT_ID", ""
)
KIC_CONTACTMOMENTEN_SERVICE_API_SECRET = config(
    "KIC_CONTACTMOMENTEN_SERVICE_API_SECRET", ""
)
KIC_REGISTER_EMAIL = config("KIC_REGISTER_EMAIL", None)
KIC_REGISTER_CONTACT_MOMENT = config("KIC_REGISTER_CONTACT_MOMENT", None)
KIC_REGISTER_BRONORGANISATIE_RSIN = config("KIC_REGISTER_BRONORGANISATIE_RSIN", None)
KIC_REGISTER_CHANNEL = config("KIC_REGISTER_CHANNEL", None)
KIC_REGISTER_TYPE = config("KIC_REGISTER_TYPE", None)
KIC_REGISTER_EMPLOYEE_ID = config("KIC_REGISTER_EMPLOYEE_ID", None)
KIC_USE_RSIN_FOR_INNNNPID_QUERY_PARAMETER = config(
    "KIC_USE_RSIN_FOR_INNNNPID_QUERY_PARAMETER", None
)


#
# SiteConfiguration variables
#
SITE_CONFIG_ENABLE = config("SITE_CONFIG_ENABLE", True)
SITE_NAME = config("SITE_NAME", None)
SITE_PRIMARY_COLOR = config("SITE_PRIMARY_COLOR", None)
SITE_SECONDARY_COLOR = config("SITE_SECONDARY_COLOR", None)
SITE_ACCENT_COLOR = config("SITE_ACCENT_COLOR", None)
SITE_PRIMARY_FONT_COLOR = config("SITE_PRIMARY_FONT_COLOR", None)
SITE_SECONDARY_FONT_COLOR = config("SITE_SECONDARY_FONT_COLOR", None)
SITE_ACCENT_FONT_COLOR = config("SITE_ACCENT_FONT_COLOR", None)
SITE_WARNING_BANNER_ENABLED = config("SITE_WARNING_BANNER_ENABLED", None)
SITE_WARNING_BANNER_TEXT = config("SITE_WARNING_BANNER_TEXT", None)
SITE_WARNING_BANNER_BACKGROUND_COLOR = config(
    "SITE_WARNING_BANNER_BACKGROUND_COLOR", None
)
SITE_WARNING_BANNER_FONT_COLOR = config("SITE_WARNING_BANNER_FONT_COLOR", None)
SITE_HERO_IMAGE_LOGIN = config("SITE_HERO_IMAGE_LOGIN", None)
SITE_LOGIN_SHOW = config("SITE_LOGIN_SHOW", None)
SITE_LOGIN_ALLOW_REGISTRATION = config("SITE_LOGIN_ALLOW_REGISTRATION", None)
SITE_LOGIN_2FA_SMS = config("SITE_LOGIN_2FA_SMS", None)
SITE_LOGIN_TEXT = config("SITE_LOGIN_TEXT", None)
SITE_REGISTRATION_TEXT = config("SITE_REGISTRATION_TEXT", None)
SITE_HOME_WELCOME_TITLE = config("SITE_HOME_WELCOME_TITLE", None)
SITE_HOME_WELCOME_INTRO = config("SITE_HOME_WELCOME_INTRO", None)
SITE_HOME_THEME_TITLE = config("SITE_HOME_THEME_TITLE", None)
SITE_HOME_THEME_INTRO = config("SITE_HOME_THEME_INTRO", None)
SITE_THEME_TITLE = config("SITE_THEME_TITLE", None)
SITE_THEME_INTRO = config("SITE_THEME_INTRO", None)
SITE_HOME_MAP_TITLE = config("SITE_HOME_MAP_TITLE", None)
SITE_HOME_MAP_INTRO = config("SITE_HOME_MAP_INTRO", None)
SITE_HOME_QUESTIONNAIRE_TITLE = config("SITE_HOME_QUESTIONNAIRE_TITLE", None)
SITE_HOME_QUESTIONNAIRE_INTRO = config("SITE_HOME_QUESTIONNAIRE_INTRO", None)
SITE_HOME_PRODUCT_FINDER_TITLE = config("SITE_HOME_PRODUCT_FINDER_TITLE", None)
SITE_HOME_PRODUCT_FINDER_INTRO = config("SITE_HOME_PRODUCT_FINDER_INTRO", None)
SITE_SELECT_QUESTIONNAIRE_TITLE = config("SITE_SELECT_QUESTIONNAIRE_TITLE", None)
SITE_SELECT_QUESTIONNAIRE_INTRO = config("SITE_SELECT_QUESTIONNAIRE_INTRO", None)
SITE_PLANS_INTRO = config("SITE_PLANS_INTRO", None)
SITE_PLANS_NO_PLANS_MESSAGE = config("SITE_PLANS_NO_PLANS_MESSAGE", None)
SITE_PLANS_EDIT_MESSAGE = config("SITE_PLANS_EDIT_MESSAGE", None)
SITE_FOOTER_LOGO_TITLE = config("SITE_FOOTER_LOGO_TITLE", None)
SITE_FOOTER_LOGO_URL = config("SITE_FOOTER_LOGO_URL", None)
SITE_HOME_HELP_TEXT = config("SITE_HOME_HELP_TEXT", None)
SITE_THEME_HELP_TEXT = config("SITE_THEME_HELP_TEXT", None)
SITE_PRODUCT_HELP_TEXT = config("SITE_PRODUCT_HELP_TEXT", None)
SITE_SEARCH_HELP_TEXT = config("SITE_SEARCH_HELP_TEXT", None)
SITE_ACCOUNT_HELP_TEXT = config("SITE_ACCOUNT_HELP_TEXT", None)
SITE_QUESTIONNAIRE_HELP_TEXT = config("SITE_QUESTIONNAIRE_HELP_TEXT", None)
SITE_PLAN_HELP_TEXT = config("SITE_PLAN_HELP_TEXT", None)
SITE_SEARCH_FILTER_CATEGORIES = config("SITE_SEARCH_FILTER_CATEGORIES", None)
SITE_SEARCH_FILTER_TAGS = config("SITE_SEARCH_FILTER_TAGS", None)
SITE_SEARCH_FILTER_ORGANIZATIONS = config("SITE_SEARCH_FILTER_ORGANIZATIONS", None)
SITE_EMAIL_NEW_MESSAGE = config("SITE_EMAIL_NEW_MESSAGE", None)
SITE_RECIPIENTS_EMAIL_DIGEST = config("SITE_RECIPIENTS_EMAIL_DIGEST", None)
SITE_CONTACT_PHONENUMBER = config("SITE_CONTACT_PHONENUMBER", None)
SITE_CONTACT_PAGE = config("SITE_CONTACT_PAGE", None)
SITE_GTM_CODE = config("SITE_GTM_CODE", None)
SITE_GA_CODE = config("SITE_GA_CODE", None)
SITE_MATOMO_URL = config("SITE_MATOMO_URL", None)
SITE_MATOMO_SITE_ID = config("SITE_MATOMO_SITE_ID", None)
SITE_SITEIMPROVE_ID = config("SITE_SITEIMPROVE_ID", None)
SITE_COOKIE_INFO_TEXT = config("SITE_COOKIE_INFO_TEXT", None)
SITE_COOKIE_LINK_TEXT = config("SITE_COOKIE_LINK_TEXT", None)
SITE_COOKIE_LINK_URL = config("SITE_COOKIE_LINK_URL", None)
SITE_KCM_SURVEY_LINK_TEXT = config("SITE_KCM_SURVEY_LINK_TEXT", None)
SITE_KCM_SURVEY_LINK_URL = config("SITE_KCM_SURVEY_LINK_URL", None)
SITE_OPENID_CONNECT_LOGIN_TEXT = config("SITE_OPENID_CONNECT_LOGIN_TEXT", None)
SITE_OPENID_DISPLAY = config("SITE_OPENID_DISPLAY", None)
SITE_REDIRECT_TO = config("SITE_REDIRECT_TO", None)
SITE_ALLOW_MESSAGES_FILE_SHARING = config("SITE_ALLOW_MESSAGES_FILE_SHARING", None)
SITE_HIDE_CATEGORIES_FROM_ANONYMOUS_USERS = config(
    "SITE_HIDE_CATEGORIES_FROM_ANONYMOUS_USERS", None
)
SITE_HIDE_SEARCH_FROM_ANONYMOUS_USERS = config(
    "SITE_HIDE_SEARCH_FROM_ANONYMOUS_USERS", None
)
SITE_DISPLAY_SOCIAL = config("SITE_DISPLAY_SOCIAL", None)
SITE_THEME_STYLESHEET = config("SITE_THEME_STYLESHEET", None)
SITE_EHERKENNING_ENABLED = config("SITE_EHERKENNING_ENABLED", None)


# Authentication configuration variables
# NOTE variables are namespaced with `DIGID_OIDC`, but some model field names also have `oidc_...` in them
DIGID_OIDC_CONFIG_ENABLE = config("DIGID_OIDC_CONFIG_ENABLE", True)
DIGID_OIDC_IDENTIFIER_CLAIM_NAME = config("DIGID_OIDC_IDENTIFIER_CLAIM_NAME", None)
DIGID_OIDC_OIDC_RP_CLIENT_ID = config("DIGID_OIDC_OIDC_RP_CLIENT_ID", None)
DIGID_OIDC_OIDC_RP_CLIENT_SECRET = config("DIGID_OIDC_OIDC_RP_CLIENT_SECRET", None)
DIGID_OIDC_OIDC_RP_SIGN_ALGO = config("DIGID_OIDC_OIDC_RP_SIGN_ALGO", None)
DIGID_OIDC_OIDC_RP_SCOPES_LIST = config("DIGID_OIDC_OIDC_RP_SCOPES_LIST", None)
DIGID_OIDC_OIDC_OP_DISCOVERY_ENDPOINT = config(
    "DIGID_OIDC_OIDC_OP_DISCOVERY_ENDPOINT", None
)
DIGID_OIDC_OIDC_OP_JWKS_ENDPOINT = config("DIGID_OIDC_OIDC_OP_JWKS_ENDPOINT", None)
DIGID_OIDC_OIDC_OP_AUTHORIZATION_ENDPOINT = config(
    "DIGID_OIDC_OIDC_OP_AUTHORIZATION_ENDPOINT", None
)
DIGID_OIDC_OIDC_OP_TOKEN_ENDPOINT = config("DIGID_OIDC_OIDC_OP_TOKEN_ENDPOINT", None)
DIGID_OIDC_OIDC_OP_USER_ENDPOINT = config("DIGID_OIDC_OIDC_OP_USER_ENDPOINT", None)
DIGID_OIDC_OIDC_RP_IDP_SIGN_KEY = config("DIGID_OIDC_OIDC_RP_IDP_SIGN_KEY", None)
DIGID_OIDC_USERINFO_CLAIMS_SOURCE = config("DIGID_OIDC_USERINFO_CLAIMS_SOURCE", None)
DIGID_OIDC_OIDC_OP_LOGOUT_ENDPOINT = config("DIGID_OIDC_OIDC_OP_LOGOUT_ENDPOINT", None)
DIGID_OIDC_ERROR_MESSAGE_MAPPING = config("DIGID_OIDC_ERROR_MESSAGE_MAPPING", None)
DIGID_OIDC_OIDC_KEYCLOAK_IDP_HINT = config("DIGID_OIDC_OIDC_KEYCLOAK_IDP_HINT", None)
DIGID_OIDC_OIDC_USE_NONCE = config("DIGID_OIDC_OIDC_USE_NONCE", None)
DIGID_OIDC_OIDC_NONCE_SIZE = config("DIGID_OIDC_OIDC_NONCE_SIZE", None)
DIGID_OIDC_OIDC_STATE_SIZE = config("DIGID_OIDC_OIDC_STATE_SIZE", None)
DIGID_OIDC_OIDC_EXEMPT_URLS = config("DIGID_OIDC_OIDC_EXEMPT_URLS", None)

# NOTE variables are namespaced with `EHERKENNING_OIDC`, but some model field names also have `oidc_...` in them
EHERKENNING_OIDC_CONFIG_ENABLE = config("EHERKENNING_OIDC_CONFIG_ENABLE", True)
EHERKENNING_OIDC_IDENTIFIER_CLAIM_NAME = config(
    "EHERKENNING_OIDC_IDENTIFIER_CLAIM_NAME", None
)
EHERKENNING_OIDC_OIDC_RP_CLIENT_ID = config("EHERKENNING_OIDC_OIDC_RP_CLIENT_ID", None)
EHERKENNING_OIDC_OIDC_RP_CLIENT_SECRET = config(
    "EHERKENNING_OIDC_OIDC_RP_CLIENT_SECRET", None
)
EHERKENNING_OIDC_OIDC_RP_SIGN_ALGO = config("EHERKENNING_OIDC_OIDC_RP_SIGN_ALGO", None)
EHERKENNING_OIDC_OIDC_RP_SCOPES_LIST = config(
    "EHERKENNING_OIDC_OIDC_RP_SCOPES_LIST", None
)
EHERKENNING_OIDC_OIDC_OP_DISCOVERY_ENDPOINT = config(
    "EHERKENNING_OIDC_OIDC_OP_DISCOVERY_ENDPOINT", None
)
EHERKENNING_OIDC_OIDC_OP_JWKS_ENDPOINT = config(
    "EHERKENNING_OIDC_OIDC_OP_JWKS_ENDPOINT", None
)
EHERKENNING_OIDC_OIDC_OP_AUTHORIZATION_ENDPOINT = config(
    "EHERKENNING_OIDC_OIDC_OP_AUTHORIZATION_ENDPOINT", None
)
EHERKENNING_OIDC_OIDC_OP_TOKEN_ENDPOINT = config(
    "EHERKENNING_OIDC_OIDC_OP_TOKEN_ENDPOINT", None
)
EHERKENNING_OIDC_OIDC_OP_USER_ENDPOINT = config(
    "EHERKENNING_OIDC_OIDC_OP_USER_ENDPOINT", None
)
EHERKENNING_OIDC_OIDC_RP_IDP_SIGN_KEY = config(
    "EHERKENNING_OIDC_OIDC_RP_IDP_SIGN_KEY", None
)
EHERKENNING_OIDC_USERINFO_CLAIMS_SOURCE = config(
    "EHERKENNING_OIDC_USERINFO_CLAIMS_SOURCE", None
)
EHERKENNING_OIDC_OIDC_OP_LOGOUT_ENDPOINT = config(
    "EHERKENNING_OIDC_OIDC_OP_LOGOUT_ENDPOINT", None
)
EHERKENNING_OIDC_ERROR_MESSAGE_MAPPING = config(
    "EHERKENNING_OIDC_ERROR_MESSAGE_MAPPING", None
)
EHERKENNING_OIDC_OIDC_KEYCLOAK_IDP_HINT = config(
    "EHERKENNING_OIDC_OIDC_KEYCLOAK_IDP_HINT", None
)
EHERKENNING_OIDC_OIDC_USE_NONCE = config("EHERKENNING_OIDC_OIDC_USE_NONCE", None)
EHERKENNING_OIDC_OIDC_NONCE_SIZE = config("EHERKENNING_OIDC_OIDC_NONCE_SIZE", None)
EHERKENNING_OIDC_OIDC_STATE_SIZE = config("EHERKENNING_OIDC_OIDC_STATE_SIZE", None)
EHERKENNING_OIDC_OIDC_EXEMPT_URLS = config("EHERKENNING_OIDC_OIDC_EXEMPT_URLS", None)

# NOTE variables are namespaced with `ADMIN_OIDC`, but some model field names also have `oidc_...` in them
ADMIN_OIDC_CONFIG_ENABLE = config("ADMIN_OIDC_CONFIG_ENABLE", default=True)
ADMIN_OIDC_OIDC_RP_CLIENT_ID = config("ADMIN_OIDC_OIDC_RP_CLIENT_ID", None)
ADMIN_OIDC_OIDC_RP_CLIENT_SECRET = config("ADMIN_OIDC_OIDC_RP_CLIENT_SECRET", None)
ADMIN_OIDC_OIDC_RP_SCOPES_LIST = config("ADMIN_OIDC_OIDC_RP_SCOPES_LIST", None)
ADMIN_OIDC_OIDC_RP_SIGN_ALGO = config("ADMIN_OIDC_OIDC_RP_SIGN_ALGO", None)
ADMIN_OIDC_OIDC_RP_IDP_SIGN_KEY = config("ADMIN_OIDC_OIDC_RP_IDP_SIGN_KEY", None)
ADMIN_OIDC_OIDC_OP_DISCOVERY_ENDPOINT = config(
    "ADMIN_OIDC_OIDC_OP_DISCOVERY_ENDPOINT", None
)
ADMIN_OIDC_OIDC_OP_JWKS_ENDPOINT = config("ADMIN_OIDC_OIDC_OP_JWKS_ENDPOINT", None)
ADMIN_OIDC_OIDC_OP_AUTHORIZATION_ENDPOINT = config(
    "ADMIN_OIDC_OIDC_OP_AUTHORIZATION_ENDPOINT", None
)
ADMIN_OIDC_OIDC_OP_TOKEN_ENDPOINT = config("ADMIN_OIDC_OIDC_OP_TOKEN_ENDPOINT", None)
ADMIN_OIDC_OIDC_OP_USER_ENDPOINT = config("ADMIN_OIDC_OIDC_OP_USER_ENDPOINT", None)
ADMIN_OIDC_USERNAME_CLAIM = config("ADMIN_OIDC_USERNAME_CLAIM", None)
ADMIN_OIDC_GROUPS_CLAIM = config("ADMIN_OIDC_GROUPS_CLAIM", None)
ADMIN_OIDC_CLAIM_MAPPING = config("ADMIN_OIDC_CLAIM_MAPPING", None)
ADMIN_OIDC_SYNC_GROUPS = config("ADMIN_OIDC_SYNC_GROUPS", None)
ADMIN_OIDC_SYNC_GROUPS_GLOB_PATTERN = config(
    "ADMIN_OIDC_SYNC_GROUPS_GLOB_PATTERN", None
)
ADMIN_OIDC_DEFAULT_GROUPS = config("ADMIN_OIDC_DEFAULT_GROUPS", None)
ADMIN_OIDC_MAKE_USERS_STAFF = config("ADMIN_OIDC_MAKE_USERS_STAFF", None)
ADMIN_OIDC_SUPERUSER_GROUP_NAMES = config("ADMIN_OIDC_SUPERUSER_GROUP_NAMES", None)
ADMIN_OIDC_OIDC_USE_NONCE = config("ADMIN_OIDC_OIDC_USE_NONCE", None)
ADMIN_OIDC_OIDC_NONCE_SIZE = config("ADMIN_OIDC_OIDC_NONCE_SIZE", None)
ADMIN_OIDC_OIDC_STATE_SIZE = config("ADMIN_OIDC_OIDC_STATE_SIZE", None)
ADMIN_OIDC_OIDC_EXEMPT_URLS = config("ADMIN_OIDC_OIDC_EXEMPT_URLS", None)
ADMIN_OIDC_USERINFO_CLAIMS_SOURCE = config("ADMIN_OIDC_USERINFO_CLAIMS_SOURCE", None)

DIGID_CONFIG_ENABLE = config("DIGID_CONFIG_ENABLE", default=True)
DIGID_CERTIFICATE_LABEL = config("DIGID_CERTIFICATE_LABEL", None)
DIGID_CERTIFICATE_TYPE = config("DIGID_CERTIFICATE_TYPE", None)
DIGID_CERTIFICATE_PUBLIC_CERTIFICATE = config(
    "DIGID_CERTIFICATE_PUBLIC_CERTIFICATE", None
)
DIGID_CERTIFICATE_PRIVATE_KEY = config("DIGID_CERTIFICATE_PRIVATE_KEY", None)
DIGID_METADATA_FILE_SOURCE = config("DIGID_METADATA_FILE_SOURCE", None)
DIGID_WANT_ASSERTIONS_SIGNED = config("DIGID_WANT_ASSERTIONS_SIGNED", None)
DIGID_WANT_ASSERTIONS_ENCRYPTED = config("DIGID_WANT_ASSERTIONS_ENCRYPTED", None)
DIGID_ARTIFACT_RESOLVE_CONTENT_TYPE = config(
    "DIGID_ARTIFACT_RESOLVE_CONTENT_TYPE", None
)
DIGID_KEY_PASSPHRASE = config("DIGID_KEY_PASSPHRASE", None)
DIGID_SIGNATURE_ALGORITHM = config("DIGID_SIGNATURE_ALGORITHM", None)
DIGID_DIGEST_ALGORITHM = config("DIGID_DIGEST_ALGORITHM", None)
DIGID_ENTITY_ID = config("DIGID_ENTITY_ID", None)
DIGID_BASE_URL = config("DIGID_BASE_URL", None)
DIGID_SERVICE_NAME = config("DIGID_SERVICE_NAME", None)
DIGID_SERVICE_DESCRIPTION = config("DIGID_SERVICE_DESCRIPTION", None)
DIGID_TECHNICAL_CONTACT_PERSON_TELEPHONE = config(
    "DIGID_TECHNICAL_CONTACT_PERSON_TELEPHONE", None
)
DIGID_TECHNICAL_CONTACT_PERSON_EMAIL = config(
    "DIGID_TECHNICAL_CONTACT_PERSON_EMAIL", None
)
DIGID_ORGANIZATION_URL = config("DIGID_ORGANIZATION_URL", None)
DIGID_ORGANIZATION_NAME = config("DIGID_ORGANIZATION_NAME", None)
DIGID_ATTRIBUTE_CONSUMING_SERVICE_INDEX = config(
    "DIGID_ATTRIBUTE_CONSUMING_SERVICE_INDEX", None
)
DIGID_REQUESTED_ATTRIBUTES = config("DIGID_REQUESTED_ATTRIBUTES", None)
DIGID_SLO = config("DIGID_SLO", None)

EHERKENNING_ENABLE = config("EHERKENNING_ENABLE", default=True)
EHERKENNING_CERTIFICATE_LABEL = config("EHERKENNING_CERTIFICATE_LABEL", None)
EHERKENNING_CERTIFICATE_TYPE = config("EHERKENNING_CERTIFICATE_TYPE", None)
EHERKENNING_CERTIFICATE_PUBLIC_CERTIFICATE = config(
    "EHERKENNING_CERTIFICATE_PUBLIC_CERTIFICATE", None
)
EHERKENNING_CERTIFICATE_PRIVATE_KEY = config(
    "EHERKENNING_CERTIFICATE_PRIVATE_KEY", None
)
EHERKENNING_METADATA_FILE_SOURCE = config("EHERKENNING_METADATA_FILE_SOURCE", None)
EHERKENNING_WANT_ASSERTIONS_SIGNED = config("EHERKENNING_WANT_ASSERTIONS_SIGNED", None)
EHERKENNING_WANT_ASSERTIONS_ENCRYPTED = config(
    "EHERKENNING_WANT_ASSERTIONS_ENCRYPTED", None
)
EHERKENNING_ARTIFACT_RESOLVE_CONTENT_TYPE = config(
    "EHERKENNING_ARTIFACT_RESOLVE_CONTENT_TYPE", None
)
EHERKENNING_KEY_PASSPHRASE = config("EHERKENNING_KEY_PASSPHRASE", None)
EHERKENNING_SIGNATURE_ALGORITHM = config("EHERKENNING_SIGNATURE_ALGORITHM", None)
EHERKENNING_DIGEST_ALGORITHM = config("EHERKENNING_DIGEST_ALGORITHM", None)
EHERKENNING_ENTITY_ID = config("EHERKENNING_ENTITY_ID", None)
EHERKENNING_BASE_URL = config("EHERKENNING_BASE_URL", None)
EHERKENNING_SERVICE_NAME = config("EHERKENNING_SERVICE_NAME", None)
EHERKENNING_SERVICE_DESCRIPTION = config("EHERKENNING_SERVICE_DESCRIPTION", None)
EHERKENNING_TECHNICAL_CONTACT_PERSON_TELEPHONE = config(
    "EHERKENNING_TECHNICAL_CONTACT_PERSON_TELEPHONE", None
)
EHERKENNING_TECHNICAL_CONTACT_PERSON_EMAIL = config(
    "EHERKENNING_TECHNICAL_CONTACT_PERSON_EMAIL", None
)
EHERKENNING_ORGANIZATION_URL = config("EHERKENNING_ORGANIZATION_URL", None)
EHERKENNING_ORGANIZATION_NAME = config("EHERKENNING_ORGANIZATION_NAME", None)
EHERKENNING_EH_LOA = config("EHERKENNING_EH_LOA", None)
EHERKENNING_EH_ATTRIBUTE_CONSUMING_SERVICE_INDEX = config(
    "EHERKENNING_EH_ATTRIBUTE_CONSUMING_SERVICE_INDEX", None
)
EHERKENNING_EH_REQUESTED_ATTRIBUTES = config(
    "EHERKENNING_EH_REQUESTED_ATTRIBUTES", None
)
EHERKENNING_EH_SERVICE_UUID = config("EHERKENNING_EH_SERVICE_UUID", None)
EHERKENNING_EH_SERVICE_INSTANCE_UUID = config(
    "EHERKENNING_EH_SERVICE_INSTANCE_UUID", None
)
EHERKENNING_EIDAS_LOA = config("EHERKENNING_EIDAS_LOA", None)
EHERKENNING_EIDAS_ATTRIBUTE_CONSUMING_SERVICE_INDEX = config(
    "EHERKENNING_EIDAS_ATTRIBUTE_CONSUMING_SERVICE_INDEX", None
)
EHERKENNING_EIDAS_REQUESTED_ATTRIBUTES = config(
    "EHERKENNING_EIDAS_REQUESTED_ATTRIBUTES", None
)
EHERKENNING_EIDAS_SERVICE_UUID = config("EHERKENNING_EIDAS_SERVICE_UUID", None)
EHERKENNING_EIDAS_SERVICE_INSTANCE_UUID = config(
    "EHERKENNING_EIDAS_SERVICE_INSTANCE_UUID", None
)
EHERKENNING_OIN = config("EHERKENNING_OIN", None)
EHERKENNING_NO_EIDAS = config("EHERKENNING_NO_EIDAS", None)
EHERKENNING_PRIVACY_POLICY = config("EHERKENNING_PRIVACY_POLICY", None)
EHERKENNING_MAKELAAR_ID = config("EHERKENNING_MAKELAAR_ID", None)
EHERKENNING_SERVICE_LANGUAGE = config("EHERKENNING_SERVICE_LANGUAGE", None)
