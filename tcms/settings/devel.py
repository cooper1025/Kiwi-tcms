# pylint: disable=wildcard-import, unused-wildcard-import
"""
    Django settings for devel env.
"""

import os
from .product import *  # noqa: F403

# Debug settings
DEBUG = True

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'kiwi',
        'USER': 'postgres',
        'PASSWORD': 'root',
        'HOST': '',
        'PORT': '',
    }
}

# django-debug-toolbar settings

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']  # noqa: F405

INSTALLED_APPS += ['debug_toolbar', 'django_extensions']  # noqa: F405

MEDIA_ROOT = os.path.join(TCMS_ROOT_PATH, '..', 'uploads')  # noqa: F405

# Needed by django.template.context_processors.debug:
# See:
# http://docs.djangoproject.com/en/dev/ref/templates/api/#django-template-context-processors-debug
INTERNAL_IPS = ('127.0.0.1', )
