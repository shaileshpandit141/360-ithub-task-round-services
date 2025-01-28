"""Django settings for it_services project."""

from pathlib import Path
from decouple import config, Csv

# BASE_DIR Configuration Settings
# -------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY Configuration Settings
# ---------------------------------
SECRET_KEY = config("SECRET_KEY", cast=str)

# DEBUG Configuration Settings
# ----------------------------
DEBUG = config("DEBUG", cast=bool, default=False)

# ALLOWED_HOSTS Configuration Settings
# ------------------------------------
ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())

# Django Application installed here
# ---------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

# User Applications installed here
# ----------------------------
INSTALLED_APPS += [
    "service_app.apps.ServiceAppConfig",
    "subscription_app.apps.SubscriptionAppConfig"
]

# Third-party Applications Configuration Settings
# -----------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Application URL Configuration Settings
# --------------------------------------
ROOT_URLCONF = "it_services.urls"

# Configure templates and HTML files and related settings
# -------------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# WSGI Configuration Settings
# ---------------------------
WSGI_APPLICATION = "it_services.wsgi.application"

# Database  Configuration Settings
# --------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation Configuration Settings
# ------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization Configuration Settings
# -------------------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# STATIC AND MEDIA FILES Configuration Settings
# ---------------------------------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]

# Configure media files (User-uploaded files)
# -------------------------------------------
MEDIA_ROOT = BASE_DIR / "uploads"
MEDIA_URL = "/media/"

# Default primary key field type
# ------------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# EMAIL Configuration Settings
# ----------------------------
EMAIL_BACKEND = config("EMAIL_BACKEND", cast=str)
EMAIL_HOST = config("EMAIL_HOST", cast=str)
EMAIL_PORT = config("EMAIL_PORT", cast=int)
EMAIL_USE_TLS = config("EMAIL_USE_TLS", cast=bool, default=True)
EMAIL_USE_SSL = config("EMAIL_USE_SSL", cast=bool, default=False)
EMAIL_HOST_USER = config("EMAIL_HOST_USER", cast=str)
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", cast=str)
DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL", cast=str, default=EMAIL_HOST_USER)

# Razorpay API keys Configuration Settings
# ----------------------------------------
RAZORPAY_KEY_ID=config("RAZORPAY_KEY_ID")
RAZORPAY_KEY_SECRET=config("RAZORPAY_KEY_SECRET")
