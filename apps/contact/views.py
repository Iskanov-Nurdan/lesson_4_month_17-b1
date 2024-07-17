from django.shortcuts import render
from apps.contact.models import Translate
from apps.base.models import Base

# Create your views here.


def translate(request):
    translate = Translate.objects.all
    base = Base.objects.latest("id")

    return render(request, "base/contact-dark.html", locals())
