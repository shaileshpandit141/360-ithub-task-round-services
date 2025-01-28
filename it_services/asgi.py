"""ASGI config for it_services project."""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "it_services.settings")

application = get_asgi_application()
