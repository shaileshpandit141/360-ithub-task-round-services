"""URL configuration for service app."""

from django.urls import path
from .views import (
    service_list_view,
    service_create_view,
    service_detail_view,
    service_update_view,
    service_delete_view
)

urlpatterns = [
    path('', service_list_view, name='service_list'),
    path('service/create/', service_create_view, name='service_create'),
    path('service/<int:pk>/', service_detail_view, name='service_detail'),
    path('service/<int:pk>/update/', service_update_view, name='service_update'),
    path('service/<int:pk>/delete/', service_delete_view, name='service_delete'),
]
