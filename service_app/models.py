from django.db import models


# Model for managing service offerings with pricing, payment terms, and package details
class Service(models.Model):
    """Service model to store information about service offerings."""

    objects = models.Manager()

    # Overwriting Meta class configurations
    class Meta:
        db_table = "service"
        verbose_name = "service"
        verbose_name_plural = "services"
        ordering = ["-id"]

    # Specify the Model Objects Manager
    objects = models.Manager()

    # Defining all requirement fields
    # -------------------------------
    name = models.CharField(
        max_length=255,
        unique=False,
        null=False,
        blank=False,
        db_index=False,
        default="",
        error_messages={
            "invalid": "Please enter a valid name",
            "null": "Name field is required",
            "blank": "Name field cannot be empty",
            "max_length": "Name must be 255 characters or fewer"
        }
    )
    payment_terms = models.TextField(
        null=False,
        blank=False,
        db_index=False,
        error_messages={
            "invalid": "Please enter valid payment terms",
            "null": "Payment terms are required",
            "blank": "Payment terms cannot be empty",
        }
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False,
        db_index=False,
        error_messages={
            "invalid": "Please enter a valid price",
            "null": "Price is required",
            "blank": "Price cannot be empty",
            "max_digits": "Price cannot exceed 10 digits in total",
            "max_decimal_places": "Price cannot have more than 2 decimal places",
            "max_whole_digits": "Price cannot exceed 8 digits before the decimal"
        }
    )
    package = models.CharField(
        max_length=255,
        unique=False,
        null=False,
        blank=False,
        db_index=False,
        error_messages={
            "invalid": "Please enter a valid package name",
            "null": "Package name is required",
            "blank": "Package name cannot be empty",
            "max_length": "Package name must be 255 characters or fewer"
        }
    )
    tax = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        db_index=False,
        default=0.0,
        error_messages={
            "invalid": "Please enter a valid tax amount",
            "max_digits": "Tax amount cannot exceed 10 digits in total",
            "max_decimal_places": "Tax amount cannot have more than 2 decimal places",
            "max_whole_digits": "Tax amount cannot exceed 8 digits before the decimal"
        }
    )

    image = models.ImageField(
        upload_to="service_images/",
        height_field=None,
        width_field=None,
        max_length=100,
        null=True,
        blank=True,
        storage=None,
        db_index=False,
        default=None,
        error_messages={
            "invalid": "Please upload a valid image file",
            "invalid_image": "The uploaded file is not a valid image",
            "missing": "Please select an image to upload",
            "empty": "The uploaded file is empty",
            "max_length": "Image filename must be 100 characters or fewer"
        }
    )
    active = models.BooleanField(
        default=models.NOT_PROVIDED,
        null=False,
        db_index=False,
        error_messages={
            "invalid": "Please select either True or False",
            "null": "Active status is required"
        }
    )

    def __str__(self) -> str:
        return str(self.name)

    def save(self, *args, **kwargs):
        if self.active is None:
            self.active = True
        return super().save(*args, **kwargs)
