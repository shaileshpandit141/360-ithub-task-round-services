from django.contrib import admin
from .models import Subscription


# Register your models here.
@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'service', 'get_payment_status')

    def get_payment_status(self, obj):
        return obj.payment_status

    setattr(get_payment_status, "short_description", "Payment Status")
