# Generated by Django 4.2.11 on 2024-06-25 14:11

import django.db.models.deletion
from django.db import DataError, migrations, models


def validate_no_missing_service_fields(apps, schema_editor):
    ZGWApiGroupConfig = apps.get_model("openzaak", "ZGWApiGroupConfig")

    if rows_with_missing_services := ZGWApiGroupConfig.objects.filter(
        models.Q(drc_service__isnull=True)
        | models.Q(zrc_service__isnull=True)
        | models.Q(ztc_service__isnull=True)
    ).count():
        raise DataError(
            f"Your database contains {rows_with_missing_services} ZGWApiGroupConfig"
            " row(s) with missing ztc, drc, or ztc service fields. All these fields"
            " are now required, with the exception of your form field. Please manually"
            " update all the affected rows"
        )


class Migration(migrations.Migration):

    dependencies = [
        ("zgw_consumers", "0019_alter_service_uuid"),
        ("openzaak", "0053_zaaktypeconfig_catalogus_is_required"),
    ]

    operations = [
        migrations.RunPython(
            validate_no_missing_service_fields,
            reverse_code=lambda *args, **kwargs: None,
        ),
        migrations.AlterField(
            model_name="zgwapigroupconfig",
            name="drc_service",
            field=models.ForeignKey(
                limit_choices_to={"api_type": "drc"},
                on_delete=django.db.models.deletion.PROTECT,
                related_name="zgwset_drc_config",
                to="zgw_consumers.service",
                verbose_name="Documenten API",
            ),
        ),
        migrations.AlterField(
            model_name="zgwapigroupconfig",
            name="form_service",
            field=models.OneToOneField(
                blank=True,
                limit_choices_to={"api_type": "orc"},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="zgwset_orc_form_config",
                to="zgw_consumers.service",
                verbose_name="Form API",
            ),
        ),
        migrations.AlterField(
            model_name="zgwapigroupconfig",
            name="zrc_service",
            field=models.ForeignKey(
                limit_choices_to={"api_type": "zrc"},
                on_delete=django.db.models.deletion.PROTECT,
                related_name="zgwset_zrc_config",
                to="zgw_consumers.service",
                verbose_name="Zaken API",
            ),
        ),
        migrations.AlterField(
            model_name="zgwapigroupconfig",
            name="ztc_service",
            field=models.ForeignKey(
                limit_choices_to={"api_type": "ztc"},
                on_delete=django.db.models.deletion.PROTECT,
                related_name="zgwset_ztc_config",
                to="zgw_consumers.service",
                verbose_name="Catalogi API",
            ),
        ),
    ]
