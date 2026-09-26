"""
Django settings for the ``chatbot_project`` project.

This project wires ChatterBot into Django so that the bot's knowledge
(statements and responses) is stored in the Django database through
ChatterBot's ``DjangoStorageAdapter``. Users talk to the bot from the
terminal with ``python manage.py chat``.

Docs:
    https://docs.djangoproject.com/en/5.2/topics/settings/
    https://chatterbot.readthedocs.io/en/stable/django/index.html
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / "subdir".
BASE_DIR = Path(__file__).resolve().parent.parent


# ---------------------------------------------------------------------------
# Security
# ---------------------------------------------------------------------------
# Best practice: never hard-code secrets in source control. The secret key is
# read from an environment variable; the fallback is only for local
# development of this terminal-only assignment.
SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "dev-only-insecure-key-change-me-in-production",
)

# DEBUG is off unless explicitly enabled with DJANGO_DEBUG=1.
DEBUG = os.environ.get("DJANGO_DEBUG", "0") == "1"

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]


# ---------------------------------------------------------------------------
# Applications
# ---------------------------------------------------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # ChatterBot's Django integration: provides the Statement and Tag models
    # (and their migrations) used by DjangoStorageAdapter.
    "chatterbot.ext.django_chatterbot",
    # Our app: contains the bot factory, training data and the
    # ``train_bot`` / ``chat`` management commands.
    "chat",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "chatbot_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "chatbot_project.wsgi.application"


# ---------------------------------------------------------------------------
# Database
# ---------------------------------------------------------------------------
# SQLite keeps the project zero-configuration. ChatterBot stores everything
# it learns in this database through the Django ORM.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# ---------------------------------------------------------------------------
# ChatterBot configuration
# ---------------------------------------------------------------------------
# The bot's display name. It is kept outside the CHATTERBOT dict because
# ChatterBot's Django extension overwrites CHATTERBOT["name"] with its own
# default ("ChatterBot") when it is imported.
CHATBOT_NAME = "TerminalBot"

# These values are passed straight to ``chatterbot.ChatBot`` by
# ``chat.bot.get_chatbot()``.
CHATTERBOT = {
    # Persist the bot's knowledge in Django's database.
    "storage_adapter": "chatterbot.storage.DjangoStorageAdapter",
    # BestMatch picks the known response whose input is closest to what the
    # user typed. If the confidence is too low, the default response is used.
    "logic_adapters": [
        {
            "import_path": "chatterbot.logic.BestMatch",
            "default_response": "I am sorry, but I do not understand. "
                                "Could you rephrase that?",
            "maximum_similarity_threshold": 0.90,
        },
    ],
}


# ---------------------------------------------------------------------------
# Password validation
# ---------------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation."
             "UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# ---------------------------------------------------------------------------
# Internationalisation
# ---------------------------------------------------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# ---------------------------------------------------------------------------
# Static files
# ---------------------------------------------------------------------------
STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
