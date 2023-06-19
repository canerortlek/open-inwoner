# Generated by Django 3.2.15 on 2023-06-29 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("configurations", "0045_alter_siteconfiguration_footer_visiting_phonenumber"),
    ]

    operations = [
        migrations.AddField(
            model_name="siteconfiguration",
            name="cookie_info_text",
            field=models.CharField(
                blank=True,
                default="Wij gebruiken cookies om onze website en dienstverlening te verbeteren.",
                help_text="The text that displays inside the cookie banner. Supplying this makes the cookie banner visible.",
                max_length=255,
                verbose_name="Cookie info text",
            ),
        ),
        migrations.AddField(
            model_name="siteconfiguration",
            name="cookie_link_text",
            field=models.CharField(
                blank=True,
                default="Lees meer over ons cookiebeleid.",
                help_text="The text that is displayed as the link to the cookie policy.",
                max_length=255,
                verbose_name="Cookie link text",
            ),
        ),
        migrations.AddField(
            model_name="siteconfiguration",
            name="cookie_link_url",
            field=models.CharField(
                blank=True,
                default="/pages/privacyverklaring/",
                help_text="The link to the cookie policy page.",
                max_length=255,
                verbose_name="Privacy page link",
            ),
        ),
    ]
