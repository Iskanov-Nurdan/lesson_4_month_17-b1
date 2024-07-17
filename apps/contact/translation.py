from modeltranslation.translator import register, TranslationOptions
from apps.contact.models import Translate
from django.utils.translation import get_language


@register(Translate)
class TranslateTranslations(TranslationOptions):
    fields = ("title", "hotline", "our_location", "email")
