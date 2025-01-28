import random
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from utils.send_otp_email import send_otp_email

User = get_user_model()
otp_storage = {}


def register_view(request):
    """Handle user registration by collecting user details and initiating OTP verification."""

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Check if the username or email already exists
        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {"error": "Username already exists."})
        if User.objects.filter(email=email).exists():
            return render(request, "register.html", {"error": "Email already exists."})

        # Generate and store OTP for the email
        otp = random.randint(100000, 999999)
        otp_storage[email] = {"otp": otp, "username": username, "password": password}

        # Send OTP to the email
        send_otp_email(email, otp)

        return redirect("otp_email_verification", email=email)

    return render(request, "user_app/register.html")


def otp_email_verification_view(request, email):
    """Verify the OTP entered by user and create new user account if valid."""

    if request.method == "POST":
        entered_otp = request.POST.get("otp")
        stored_data = otp_storage.get(email)

        if stored_data and str(stored_data["otp"]) == entered_otp:
            # Creating the user after successful OTP verification
            User.objects.create_user(
                username=stored_data["username"],
                email=email,
                password=stored_data["password"]
            )
            # Remove the OTP entry after successful verification
            del otp_storage[email]

            return redirect("login")

        return render(request, "user_app/otp_email_verification.html", {"error": "Invalid OTP"})

    return render(request, "user_app/otp_email_verification.html")
