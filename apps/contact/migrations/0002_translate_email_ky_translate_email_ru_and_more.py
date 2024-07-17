# Generated by Django 5.0.6 on 2024-07-10 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contact", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="translate",
            name="email_ky",
            field=models.CharField(
                max_length=255, null=True, verbose_name="Официальная почта"
            ),
        ),
        migrations.AddField(
            model_name="translate",
            name="email_ru",
            field=models.CharField(
                max_length=255, null=True, verbose_name="Официальная почта"
            ),
        ),
        migrations.AddField(
            model_name="translate",
            name="hotline_ky",
            field=models.CharField(
                max_length=255, null=True, verbose_name="Горячая линия"
            ),
        ),
        migrations.AddField(
            model_name="translate",
            name="hotline_ru",
            field=models.CharField(
                max_length=255, null=True, verbose_name="Горячая линия"
            ),
        ),
        migrations.AddField(
            model_name="translate",
            name="our_location_ky",
            field=models.CharField(max_length=255, null=True, verbose_name="Локация"),
        ),
        migrations.AddField(
            model_name="translate",
            name="our_location_ru",
            field=models.CharField(max_length=255, null=True, verbose_name="Локация"),
        ),
        migrations.AddField(
            model_name="translate",
            name="title_ky",
            field=models.CharField(
                max_length=255, null=True, verbose_name="Заголовок баннера"
            ),
        ),
        migrations.AddField(
            model_name="translate",
            name="title_ru",
            field=models.CharField(
                max_length=255, null=True, verbose_name="Заголовок баннера"
            ),
        ),
    ]