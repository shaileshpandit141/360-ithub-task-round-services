from django.core.mail import send_mail

def send_otp_email(email, otp):
    subject = "Your OTP for Registration"
    message = f"""Hi! Welcome, your OTP verification code is: {otp}.
    Please use this code to complete your registration. Do not share this code with anyone."""
    send_mail(subject, message, "itservicesemail@gmail.com", [email])
