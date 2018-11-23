from .base import *

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
