from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import set_language
from django.conf.urls import handler404


handler404 = 'apps.base.views.errors'

urlpatterns = [
    path("admin/", admin.site.urls),
]

urlpatterns += i18n_patterns(
    path("", include("apps.base.urls")),
    path("", include("apps.about.urls")),
    path("", include("apps.contact.urls")),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
