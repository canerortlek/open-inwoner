# Generated by Django 4.2.11 on 2024-04-22 14:05

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("laposta", "0004_delete_subscription"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lapostaconfig",
            name="limit_list_selection_to",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=255),
                blank=True,
                default=list,
                help_text="If configured, users will only be able to choose from this selection of lists to subscribe to. Note: the list of newsletters is cached, so it may take up to 15 minutes before newly added newsletters show up here.",
                size=None,
                verbose_name="Limit list selection to",
            ),
        ),
    ]
