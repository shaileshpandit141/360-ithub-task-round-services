import os
import django
from django.conf import settings  

# Configure Django settings before importing models
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'it_services.settings')
django.setup()

# Import models after Django is configured
from service_app.models import Service

sample_services = [
    {
        "name": "Website Development",
        "payment_terms": "50% advance, 50% on completion",
        "price": 20000,
        "package": "Basic", 
        "tax": 18,
        "image": "service_images/website_development.jpeg",
        "active": True
    },
    {
        "name": "Mobile App Development",
        "payment_terms": "40% advance, 60% on completion", 
        "price": 50000,
        "package": "Premium",
        "tax": 18,
        "image": "service_images/mobile_app.jpeg",
        "active": True
    },
    {
        "name": "Digital Marketing",
        "payment_terms": "Full payment upfront",
        "price": 10000,
        "package": "Basic",
        "tax": 15,
        "image": "service_images/digital_marketing.jpeg",
        "active": True
    },
    {
        "name": "Graphic Design",
        "payment_terms": "50% advance, 50% on approval",
        "price": 15000,
        "package": "Standard",
        "tax": 12,
        "image": "service_images/graphic_design.jpeg",
        "active": True
    },
    {
        "name": "SEO Services", 
        "payment_terms": "Monthly subscription",
        "price": 5000,
        "package": "Monthly",
        "tax": 18,
        "image": "service_images/seo_services.jpeg",
        "active": True
    },
    {
        "name": "Cloud Hosting",
        "payment_terms": "Annual subscription",
        "price": 25000,
        "package": "Annual",
        "tax": 18,
        "image": "service_images/cloud_hosting.jpeg",
        "active": True
    },
    {
        "name": "Technical Support",
        "payment_terms": "Hourly rate",
        "price": 1000,
        "package": "Hourly",
        "tax": 5,
        "image": "service_images/technical_support.jpeg",
        "active": True
    }
]

for service_data in sample_services:
    Service.objects.create(**service_data)

print("Sample data added successfully!")
