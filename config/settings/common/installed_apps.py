INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'storages',
]

LOCAL_APPS = [
    'apps.core',
    'apps.dendynotdead',
    'apps.music',
    'apps.news',
    'apps.users',
]

INSTALLED_APPS += LOCAL_APPS
