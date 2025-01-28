from django.db import models
from django.contrib.auth import get_user_model
from service_app.models import Service

User = get_user_model()


# Model for managing user subscriptions to services, including payment and transaction tracking
class Subscription(models.Model):
    """
    A model representing user subscriptions to services.

    This model tracks the relationship between users and services they subscribe to,
    along with payment status, transaction details and delivery address information.
    """

    # Overwriting Meta class configurations
    class Meta:
        db_table = "subscription"
        verbose_name = "subscription"
        verbose_name_plural = "subscriptions"
        ordering = ["-id"]

    # Specify the Model Objects Manager
    objects = models.Manager()

    # Payment status choices
    PAYMENT_STATUS_PENDING = "pending"
    PAYMENT_STATUS_SUCCESS = "success"
    PAYMENT_STATUS_FAILED = "failed"
    PAYMENT_STATUS_CANCELLED = "cancelled"
    PAYMENT_STATUS_REFUNDED = "refunded"

    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, "Pending"),
        (PAYMENT_STATUS_SUCCESS, "Success"),
        (PAYMENT_STATUS_FAILED, "Failed"),
        (PAYMENT_STATUS_CANCELLED, "Cancelled"),
        (PAYMENT_STATUS_REFUNDED, "Refunded"),
    ]

    # Defining all requirement fields
    # -------------------------------
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        primary_key=False,
        related_name="+",
        related_query_name=None,
        limit_choices_to={},
        parent_link=False,
        null=False,
        blank=False,
        db_index=True,
        db_constraint=True,
        error_messages={
            "invalid": "Invalid user selection",
            "invalid_choice": "Selected user is not valid",
            "null": "User selection is required",
            "blank": "User selection is required",
            "does_not_exist": "Selected user does not exist"
        }
    )
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        primary_key=False,
        related_name="+",
        related_query_name=None,
        limit_choices_to={},
        parent_link=False,
        null=False,
        blank=False,
        db_index=True,
        db_constraint=True,
        error_messages={
            "invalid": "Invalid service selection",
            "invalid_choice": "Selected service is not valid",
            "null": "Service selection is required",
            "blank": "Service selection is required",
            "does_not_exist": "Selected service does not exist"
        }
    )
    address = models.TextField(
        null=True,
        blank=True,
        db_index=False,
        default="",
        error_messages={
            "invalid": "Please enter a valid address"
        }
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False,
        db_index=False,
        error_messages={
            "invalid": "Please enter a valid amount",
            "null": "Amount is required",
            "blank": "Amount is required",
            "max_digits": "Amount cannot exceed 10 digits in total",
            "decimal_places": "Amount cannot have more than 2 decimal places",
            "max_whole_digits": "Amount cannot exceed 8 digits before decimal"
        }
    )
    payment_status = models.CharField(
        max_length=20,
        unique=False,
        null=False,
        blank=False,
        db_index=False,
        default=PAYMENT_STATUS_PENDING,
        choices=PAYMENT_STATUS_CHOICES,
        error_messages={
            "invalid": "Invalid payment status",
            "invalid_choice": "Please select a valid payment status",
            "null": "Payment status is required",
            "blank": "Payment status is required",
            "max_length": "Payment status cannot exceed 20 characters"
        }
    )
    transaction_id = models.CharField(
        max_length=255,
        unique=False,
        null=True,
        blank=True,
        db_index=False,
        default="",
        error_messages={
            "invalid": "Invalid transaction ID",
            "max_length": "Transaction ID cannot exceed %(limit_value)d characters"
        }
    )

    def __str__(self) -> str:
        return str(self.user)
