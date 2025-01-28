from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models import Service
from subscription_app.models import Subscription


@login_required(login_url="login")
def home_view(request):
    """
    View function for the home page that displays services and their availability status.
    Requires user authentication.
    """
    # Query database for all services that are marked as active
    services = Service.objects.filter(active=True)

    # Get IDs of services that have successful subscription payments
    sold_service_ids = Subscription.objects.filter(
        payment_status="Success"
    ).values_list("service_id", flat=True)

    # Add is_sold attribute to each service object to indicate availability
    for service in services:
        service.is_sold = service.id in sold_service_ids

    return render(request, "service_app/home.html", {
        "services": services,
    })
