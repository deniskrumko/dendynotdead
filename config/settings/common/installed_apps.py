INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'storages',
    'adminsortable',
    'django_object_actions',
    'ckeditor',
]

LOCAL_APPS = [
    'apps.about',
    'apps.core',
    'apps.dendynotdead',
    'apps.music',
    'apps.news',
    'apps.search',
    'apps.users',
]

INSTALLED_APPS += LOCAL_APPS
