# Generated by Django 4.2.10 on 2024-03-07 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="LapostaConfig",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "api_root",
                    models.URLField(
                        help_text="The root of the API with version number (e.g. https://api.laposta.nl/v2/).",
                        max_length=128,
                        verbose_name="API root",
                    ),
                ),
                (
                    "basic_auth_username",
                    models.CharField(
                        blank=True,
                        help_text="The username used to authenticate with the Laposta API.",
                        max_length=255,
                        verbose_name="Basic Authentication username",
                    ),
                ),
                (
                    "basic_auth_password",
                    models.CharField(
                        blank=True,
                        help_text="The password used to authenticate with the Laposta API",
                        max_length=255,
                        verbose_name="Basic Authentication password",
                    ),
                ),
            ],
            options={
                "verbose_name": "Laposta configuration",
            },
        ),
    ]
