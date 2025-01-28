from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import Service


@login_required(login_url="login")
def service_create_view(request):
    """
    View function for creating a new service.

    Handles both GET and POST requests:
        GET: Displays an empty service creation form
        POST: Processes the submitted form data to create a new service
    """
    if request.method == "POST":
        # Extract and validate form data for creating a new service
        name = request.POST.get("name")
        payment_terms = request.POST.get("payment_terms")
        price = request.POST.get("price")
        package = request.POST.get("package")
        tax = request.POST.get("tax")
        image = request.FILES.get("image")
        active = request.POST.get("active") == "on"

        # Validate that all required fields are provided
        if not all([name, payment_terms, price, package]):
            return render(request, "service_app/service_create.html", {
                "error": "Name, Payment Terms, Price and Package are required fields."
            })

        # Convert price and tax strings to float values
        try:
            price = float(price)
            tax = float(tax) if tax else 0.0
        except ValueError:
            return render(request, "service_app/service_create.html", {
                "error": "Price and tax must be valid numbers."
            })

        # Create new service instance in the database
        Service.objects.create(
            name=name,
            payment_terms=payment_terms,
            price=price,
            package=package,
            tax=tax,
            image=image,
            active=active,
        )

        # Redirect to home page after successful creation
        return redirect("service_list")

    # Display empty service creation form
    return render(request, "service_app/service_create.html")
