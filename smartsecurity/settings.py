import os, sys
from unipath import Path

PROJECT_ROUTE = Path(__file__).ancestor(2)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Daniel Sibaja', 'siba2893@gmail.com'),
)

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

MANAGERS = ADMINS


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
       'NAME': 'd8v50cj8njrlsi',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'ktovcwkvvupmmm',
        'PASSWORD': 'zSrymCI0WxaL3AIWSDNegOmSwa',
        'HOST': 'ec2-184-73-254-144.compute-1.amazonaws.com',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
       'PORT': '5432',                      # Set to empty string for default.
    }
}

ALLOWED_HOSTS = ['*']

TIME_ZONE = 'UTC'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Static asset configuration

STATIC_ROOT = ''
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    PROJECT_ROUTE.child('static'),
)

TEMPLATE_DIRS = (
    PROJECT_ROUTE.child('templates'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '+5xle%ru*0!r5^!l^-107saa)#deoi&k$=e*7nnb++47m=@ybe'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'smartsecurity.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'smartsecurity.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_admin_bootstrapped.bootstrap3',
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'bootstrapform',
    'cloudinary',
    'home',
    'gallery',
    'contact',
)

CLOUDINARY = {
    'cloud_name': 'dwl0jrki8',
    'api_key': '675453694475986',
    'api_secret': 'PlVRVrDY55rPUGpv566mnSCkrEI',
}

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
