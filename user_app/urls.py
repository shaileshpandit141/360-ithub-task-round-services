from django.urls import path
from .views import (
    login_view,
    logout_view,
    register_view,
    otp_email_verification_view,
)

urlpatterns = [
    path("register/", register_view, name="register"),
    path(
        "otp-email-verification/<str:email>/",
        otp_email_verification_view,
        name="otp_verification"
    ),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
]
