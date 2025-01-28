import razorpay
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from ..models import Service, Subscription
from django.contrib.auth.decorators import login_required


@login_required(login_url="login")
def subscription_payment_view(request, service_id):
    """
    Handle subscription creation and payment processing via Razorpay.

    This view processes subscription requests for services, calculates pricing with GST,
    creates Razorpay orders, and handles the payment flow. It requires user authentication.
    """
    service = get_object_or_404(Service, id=service_id)

    # Calculate net price including GST (Goods and Services Tax)
    net_price = float(service.price) + (float(service.price) * (float(service.tax) / 100))
    setattr(service, "net_price", net_price)

    if request.method == "POST":
        address = request.POST.get("address")
        user = request.user

        try:
            # Initialize Razorpay client with API credentials
            client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

            # Get order interface and validate it exists
            order = getattr(client, "order", None)
            if order is None:
                raise Exception("Something is not correct. Please try again later")

            # Create new Razorpay order with amount in paise (1 INR = 100 paise)
            razorpay_order = order.create({
                "amount": int(net_price * 100),
                "currency": "INR",
                "payment_capture": "1",
            })

            print("Net Price (with GST):", net_price)

            # Create subscription record in database with pending payment status
            Subscription.objects.create(
                user=user,
                service=service,
                address=address,
                amount=net_price,
                payment_status="Pending",
                transaction_id=razorpay_order["id"]
            )

            # Prepare context data for payment gateway integration
            context = {
                "service": service,
                "razorpay_order_id": razorpay_order["id"],
                "razorpay_key_id": settings.RAZORPAY_KEY_ID,
                "amount": net_price,
                "callback_url": request.build_absolute_uri("/payment/callback/"),
            }
            return render(request, "subscription_app/subscription_payment_callback.html", context)

        except Exception as error:
            return render(request, "subscription_app/subscription_payment.html", {
                "service": service,
                "error": f"Razorpay error: {str(error)}"
            })

    setattr(service, "amount", net_price)
    return render(request, "subscription_app/subscription_payment.html", {"service": service})
