from django.contrib.auth import logout
from django.shortcuts import redirect


def logout_view(request):
    """Logs out the current user and redirects to login page"""

    logout(request)
    return redirect("login")
