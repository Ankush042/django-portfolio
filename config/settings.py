
from pathlib import Path

# BASE DIRECTORY
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY SETTINGS
SECRET_KEY = 'django-insecure-ankush-portfolio-development-key-change-before-deployment'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# APPLICATIONS
INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'portfolio',
]


# MIDDLEWARE
MIDDLEWARE = []


# ROOT URL CONFIGURATION
ROOT_URLCONF = 'config.urls'


# TEMPLATE CONFIGURATION
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [],
        },
    },
]


# WSGI CONFIGURATION
WSGI_APPLICATION = 'config.wsgi.application'


# DATABASE CONFIGURATION
# No database models are required for this portfolio.

DATABASES = {}


# PASSWORD VALIDATION
# Not required because authentication is not being used.


# INTERNATIONALIZATION
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# STATIC FILES CONFIGURATION

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]


# DEFAULT PRIMARY KEY
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
