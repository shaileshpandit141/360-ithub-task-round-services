"""URL configuration for subscription app."""

from django.urls import path
from .views import (
    subscription_payment_view,
    subscription_payment_callback_view
)

urlpatterns = [
    path("subscription/<int:service_id>/", subscription_payment_view, name="subscription"),
    path("payment/callback/", subscription_payment_callback_view, name="payment_callback"),
]
