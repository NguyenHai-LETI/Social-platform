import os
from .base import *  #load toàn bộ mã trong base.py

environ.Env.read_env(os.path.join(BASE_DIR.parent.parent, "envs/develop.env"))

DEBUG = True
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',  # Phải trước middleware khác
] + MIDDLEWARE

# Chỉ hiện toolbar cho localhost
INTERNAL_IPS = [
    '127.0.0.1',
    'localhost',
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
