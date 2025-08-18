import os
from .base import *  #load toàn bộ mã trong base.py

environ.Env.read_env(os.path.join(BASE_DIR.parent.parent, "envs/develop.env"))

DEBUG = True
ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
