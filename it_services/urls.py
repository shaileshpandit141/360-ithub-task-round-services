"""URL configuration for it_services project."""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from service_app import urls as service_app_urls
from subscription_app import urls as subscription_app_urls
from user_app import urls as user_app_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(service_app_urls)),
    path("", include(subscription_app_urls)),
    path("", include(user_app_urls)),
]

# Enable serving of user-uploaded media files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
