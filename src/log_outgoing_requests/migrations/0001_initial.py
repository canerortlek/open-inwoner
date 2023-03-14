# Generated by Django 3.2.15 on 2023-03-14 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="OutgoingRequestsLog",
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
                    "hostname",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="The hostname part of the url.",
                        max_length=255,
                        verbose_name="Hostname",
                    ),
                ),
                (
                    "path",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="The path part of the url.",
                        max_length=255,
                        verbose_name="Path",
                    ),
                ),
                (
                    "params",
                    models.TextField(
                        blank=True,
                        help_text="The parameters (if they exist).",
                        verbose_name="Parameters",
                    ),
                ),
                (
                    "query_params",
                    models.TextField(
                        blank=True,
                        help_text="The query parameters part of the url (if they exist).",
                        verbose_name="Query parameters",
                    ),
                ),
                (
                    "status_code",
                    models.PositiveIntegerField(
                        blank=True,
                        help_text="The status code of the response.",
                        null=True,
                    ),
                ),
                (
                    "method",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="The type of request method.",
                        max_length=10,
                    ),
                ),
                (
                    "response_ms",
                    models.PositiveIntegerField(
                        blank=True,
                        default=0,
                        help_text="This is the response time in ms.",
                        verbose_name="Response in ms",
                    ),
                ),
                (
                    "timestamp",
                    models.DateTimeField(
                        help_text="This is the date and time the API call was made.",
                        verbose_name="Timestamp",
                    ),
                ),
                (
                    "trace",
                    models.TextField(
                        blank=True,
                        help_text="Text providing information in case of request failure.",
                        null=True,
                        verbose_name="Trace",
                    ),
                ),
            ],
            options={
                "verbose_name": "Outgoing Requests Log",
                "verbose_name_plural": "Outgoing Requests Logs",
            },
        ),
    ]
