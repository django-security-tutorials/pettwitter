"""
Django settings for thesite project.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production

# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/ for a list of
# best practices. Figure out which ones we're violating in this project!

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "+ov#co3bkexs#f&8i3-kcbt1m+o!1wfij!72^b=64rl_96dtdc"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition
INSTALLED_APPS = (
    # Django-bundled modules
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Apps that are in this project
    "base_app",
    "communication_app",
)

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "thesite.urls"

WSGI_APPLICATION = "thesite.wsgi.application"

# https://docs.djangoproject.com/en/2.2/ref/settings/#session-cookie-httponly
SESSION_COOKIE_HTTPONLY = False

# When we upgraded to Django 2.1 and this setting was introduced, it broke some of our login mechanisms.  Let's just
# disable it. It's new, so I'm sure we don't need it.
# https://docs.djangoproject.com/en/2.2/ref/settings/#session-cookie-samesite
SESSION_COOKIE_SAMESITE = None

SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"

SESSION_SERIALIZER = "django.contrib.sessions.serializers.PickleSerializer"

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

if "DATABASE_URL" in os.environ:
    DATABASES["default"] = dj_database_url.config()

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, ".static-generated")

# https://docs.djangoproject.com/en/2.2/topics/templates/
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
            ]
        },
    }
]
