from typing import Any
from django.contrib import admin
from django.http import HttpRequest
from apps.contact.models import Translate
from modeltranslation.admin import TranslationAdmin

# Register your models here.


class TranslateAdmin(TranslationAdmin):
    model = Translate

    def get_fieldsets(self, request: HttpRequest, obj: Any = None):
        fieldsets = (
            (
                "Русская версия",
                {
                    "fields": ("title_ru", "hotline_ru", "our_location_ru", "email_ru"),
                },
            ),
            (
                "Кыргызская версия",
                {
                    "fields": ("title_ky", "hotline_ky", "our_location_ky", "email_ky"),
                },
            ),
        )
        return fieldsets


admin.site.register(Translate, TranslateAdmin)
