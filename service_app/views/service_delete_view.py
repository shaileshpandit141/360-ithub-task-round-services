from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import Service


@login_required(login_url="login")
def service_delete_view(request, pk):
    """
    View function to handle deletion of a Service.

    Requires user authentication. Displays a confirmation page on GET request
    and deletes the service on POST request.
    """
    # Get the service object or return 404 if not found
    service = get_object_or_404(Service, pk=pk)

    if request.method == "POST":
        # Delete the service object if POST request
        service.delete()
        # Redirect to the home page after successful deletion
        return redirect("service_list")

    # Display confirmation page for GET requests
    return render(request, "service_app/service_detail.html", {"service": service})
