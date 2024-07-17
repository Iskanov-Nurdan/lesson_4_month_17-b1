from modeltranslation.translator import register, TranslationOptions
from apps.base.models import Our_advantages
from django.utils.translation import get_language


@register(Our_advantages)
class Our_advantagesTramslation(TranslationOptions):
    fields = ("title", "description")
