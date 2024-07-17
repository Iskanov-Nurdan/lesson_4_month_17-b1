from django.urls import path
from apps.contact.views import translate

urlpatterns = [path("contact/", translate, name="translate")]
