from django.shortcuts import get_object_or_404
from ..models import Service
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url="login")
def service_update_view(request, pk):
    """
    View for updating an existing service.

    Allows authorized users to modify service details including name, payment terms,
    price, package, tax, image and active status. Requires user authentication.
    """

    # Get service object or return 404 if not found
    service = get_object_or_404(Service, pk=pk)

    if request.method == "POST":
        try:
            # Update service fields from form data
            service.name = request.POST.get("name")
            service.payment_terms = request.POST.get("payment_terms")
            service.price = request.POST.get("price")
            service.package = request.POST.get("package")
            service.tax = request.POST.get("tax")

            # Only update image if a new one was uploaded
            if request.FILES.get("image"):
                service.image = request.FILES.get("image")

            # Convert checkbox value to boolean
            service.active = request.POST.get("active") == "on"

            service.save()  # Save changes to database
            return redirect("service_detail", pk=service.pk)

        except Exception as error:
            # Log error and show error message to user
            print(f"Error updating service: {str(error)}")
            return render(request, "service_app/service_update.html", {
                "service": service,
                "error": "Error updating service"
            })

    # Display form for GET requests
    return render(request, "service_app/service_update.html", {"service": service})
