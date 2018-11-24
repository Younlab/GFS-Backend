from .base import *

# shell commend ENV
# export DJANGO_SETTINGS_MODULE=config.settings.dev
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INSTALLED_APPS += [
    'debug_toolbar',
    'django_extensions',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': secrets['DEV_DB_HOST'],
        'PORT': secrets['DEV_DB_PORT'],
        'USER': secrets['DEV_DB_USER'],
        'PASSWORD': secrets['DEV_DB_PASSWORD'],
        'NAME': secrets['DEV_DB_NAME'],
    }
}

# debug toolbar setting
INTERNAL_IPS = ('127.0.0.1',)

WSGI_APPLICATION = 'config.wsgi.dev.application'
MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]
