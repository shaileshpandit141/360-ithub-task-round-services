"""URL configuration for it_services project."""

from django.contrib import admin
from django.urls import path, include
from service_app import urls as service_app_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(service_app_urls)),
]
