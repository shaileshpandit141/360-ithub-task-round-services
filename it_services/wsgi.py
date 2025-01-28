"""WSGI config for it_services project."""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "it_services.settings")

application = get_wsgi_application()
