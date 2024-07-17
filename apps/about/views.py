from django.shortcuts import render
from apps.base.models import Our_chef, Base

# Create your views here.


def about(request):
    chef = Our_chef.objects.all().order_by("?")[:3]
    base = Base.objects.latest("id")
    return render(request, "base/about.html", locals())
