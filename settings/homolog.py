from .base import *

DEBUG = True

TEMPLATE_DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'oferclub',
        'USER': 'root',
        'PASSWORD': 'gloose*123',
    }
}

INSTALLED_APPS += (
    'debug_toolbar',
    'django_extensions',
)

STATIC_URL = '/static/'

STATIC_ROOT = '/home/ubuntu/statics/oferclub/static'

MEDIA_URL = '/media/'

MEDIA_ROOT = '/home/ubuntu/statics/oferclub/media'
