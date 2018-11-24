from .base import *

# shell commend ENV
# export DJANGO_SETTINGS_MODULE=config.settings.production
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

INSTALLED_APPS += []

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

WSGI_APPLICATION = 'config.wsgi.production.application'
