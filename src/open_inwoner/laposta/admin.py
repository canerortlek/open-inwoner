from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from solo.admin import SingletonModelAdmin

from .models import LapostaConfig


@admin.register(LapostaConfig)
class LapostaConfigAdmin(SingletonModelAdmin):
    fieldsets = (
        (
            _("Basic"),
            {
                "fields": ("api_root",),
            },
        ),
        (
            _("Authentication"),
            {
                "fields": [
                    "basic_auth_username",
                    "basic_auth_password",
                ]
            },
        ),
    )
