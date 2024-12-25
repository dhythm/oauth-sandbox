"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 5.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-@%17f4!f-=ulje6!9bt=7_!%$_6z+a%(m)4-#ctnkp-_8*sl!b"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "corsheaders",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_vite",
    "inertia",
    "rest_framework",
    "oauth",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "inertia.middleware.InertiaMiddleware",
]

# https://pypi.org/project/django-cors-headers/
CORS_ALLOW_CREDENTIALS = False
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)

ROOT_URLCONF = "app.urls"

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

WSGI_APPLICATION = "app.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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

# AUTHLIB_OAUTH_CLIENTS = {
#     "sap": {
#         "client_id": os.getenv("SAP_CLIENT_ID", default="SAP client id"),
#         "client_secret": os.getenv("SAP_CLIENT_SECRET", default="SAP client secret"),
#         "access_token_url": os.getenv(
#             "SAP_ACCESS_TOKEN_URL",
#             default="",
#         ),
#         "access_token_params": None,
#         "refresh_token_url": None,
#         "authorize_url": os.getenv("SAP_AUTHORIZE_URL", default=""),
#         "api_base_url": os.getenv("SAP_API_BASE_URL", default=""),
#         "client_kwargs": {
#             "scope": os.getenv("SAP_OAUTH_SCOPE", default="openid profile address"),
#             "verify": os.getenv(
#                 "REQUESTS_CA_BUNDLE", default=False
#             ),  # NOTE: This configuration is for making requests to a self-signed certificate site.
#         },
#         "jwks_uri": os.getenv("SAP_JWKS_URI", default=""),
#         "redirect_uri": os.getenv("SAP_REDIRECT_URI", default=""),
#     }
# }

# SAP_API_ENDPOINT = os.getenv("SAP_API_ENDPOINT", default="")
# SAP_API_SERVICEID = os.getenv("SAP_API_SERVICEID", default="service_id")
# SAP_API_AUTHKEY = os.getenv("SAP_API_AUTHKEY", default="authentication_key")
# SAP_API_ROLE = os.getenv("SAP_API_ROLE", default="role")


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_ROOT = "static"
STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
