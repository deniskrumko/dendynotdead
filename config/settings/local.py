from .common import *  # noqa

import dj_database_url


SECRET_KEY = 'example'

DEBUG = True

DATABASES = {
    'default': dj_database_url.config(
        default='postgres://postgres:@localhost:5432/dendynotdead'
    )
}

AUTH_PASSWORD_VALIDATORS = []

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
