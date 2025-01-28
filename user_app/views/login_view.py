from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render


def login_view(request):
    """
    Handle user login functionality.

    If a POST request is received, attempt to authenticate the user with the provided
    credentials. On successful authentication, log the user in and redirect to the home page.
    If authentication fails, re-render the login page with an error message.
    For GET requests, simply display the login form.
    """
    if request.method == "POST":
        # Extract credentials from POST data
        username = request.POST["username"]
        password = request.POST["password"]
        # Attempt to authenticate user
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("home")
        return render(request, "user_app/login.html", {"error": "Invalid credentials"})
    return render(request, "user_app/login.html")
