from django.shortcuts import get_object_or_404
from django.shortcuts import render
from ..models import Service
from django.contrib.auth.decorators import login_required


@login_required(login_url="login")
def service_detail_view(request, pk):
    """Display the detailed view of a service including its calculated net price."""
    
    # Get service or return 404 if not found
    service = get_object_or_404(Service, pk=pk)

    # Calculate net price with tax included
    net_price = float(service.price) + (float(service.price) * (float(service.tax) / 100))
    setattr(service, "amount", net_price)

    return render(request, "service_app/service_detail.html", {"service": service})
