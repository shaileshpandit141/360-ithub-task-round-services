import razorpay
from django.conf import settings
from ..models import Subscription
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def subscription_payment_callback_view(request):
    """
    Callback view to handle Razorpay payment verification and subscription status updates.

    This view handles the callback from Razorpay after a payment is made. It verifies the 
    payment signature and updates the subscription payment status accordingly.
    """
    if request.method == "POST":
        # Extract payment details from POST request
        razorpay_order_id = request.POST.get("razorpay_order_id")
        razorpay_payment_id = request.POST.get("razorpay_payment_id")
        razorpay_signature = request.POST.get("razorpay_signature")

        # Initialize Razorpay client with credentials
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

        try:
            # Get utility instance for signature verification
            utility = getattr(client, "utility", None)
            if utility is None:
                raise Exception("Something is wrong please try again later")

            # Verify authenticity of payment using signature
            utility.verify_payment_signature({
                "razorpay_order_id": razorpay_order_id,
                "razorpay_payment_id": razorpay_payment_id,
                "razorpay_signature": razorpay_signature,
            })

            # Update subscription record with successful payment status
            subscription = Subscription.objects.get(transaction_id=razorpay_order_id)
            subscription.payment_status = "Success"
            subscription.save()
            print(subscription)
            return render(request, "subscription_app/subscription_payment_success.html", {"subscription": subscription})

        except Exception as error:
            return render(request, "subscription_app/subscription_payment_failure.html", {
                "error": str(error) or "Payment verification failed"
            })

    return render(request, "subscription_app/subscription_payment_failure.html", {
        "error": "Invalid request method"
    })
