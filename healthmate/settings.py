"""
Django settings for healthmate project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import ast
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i90zpn6_07z3q$nau-)zbtoffmbl%ikq$g&u7kzqb$&lf$4x5z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = ast.literal_eval(os.environ.get('DEBUG', 'False'))

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.gis',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Third party
    'django_markdown',
    'leaflet',
    'floppyforms',
    'storages',
    'djgeojson',

    # Local apps
    'healthmate',
    'healthmate.services',
)

# Sites framework
SITE_ID = 1

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # this is default
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'healthmate.urls'

WSGI_APPLICATION = 'healthmate.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'healthmate-website',
        'USER': "healthmate-website",
        'PASSWORD': "h34lthm4t3",
        'HOST': "nothostedyet",
        'PORT': "5432",
    },
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Templates
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.messages.context_processors.messages',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader'
)

NODE_BIN = os.path.join(BASE_DIR, 'node_modules', '.bin')
LESS_BIN = os.path.join(NODE_BIN, "lessc")

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "../static")
MEDIA_ROOT = os.path.join(BASE_DIR, "../media")

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

LEAFLET_CONFIG = {
    'MIN_ZOOM': 3,
    'MAX_ZOOM': 18,
    'RESET_VIEW': False,
}

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME': os.environ.get('TDDIUM_DB_NAME') or os.environ.get('USER'),
            'USER': os.environ.get('TDDIUM_DB_USER') or os.environ.get('USER'),
            'PASSWORD': os.environ.get('TDDIUM_DB_PASSWORD'),
        }
    }
    DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
