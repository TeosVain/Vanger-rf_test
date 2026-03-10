from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from slider.views import slider_page

urlpatterns = [
    path("", slider_page, name="slider-page"),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
