"""URL configuration for service app."""

from django.urls import path
from .views import list_service_view

urlpatterns = [
    path("", list_service_view, name="list_service"),
]
