"""
Django settings for tiempoTurco project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'o5+(*-5bus0e%28%j#%2-5*u3$dj508d01l*&z!1cjt%ca6=y@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True #Cuando pase a produccion hay que ponerlo como FALSE

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

#TCP definition
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
    'tiempoTurco.context_processors.basic',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)

#Grappelli customisation
GRAPPELLI_ADMIN_TITLE = 'Tiempo Turco'

# Application definition

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    #'django.contrib.comments', Despreciado en proximas versiones
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'social.apps.django_app.default',
    'authors',
    'comments',
    'gallery',
    'images',
    'keyWords',
    'news',
    'news_counter',
    'publisher',
    'subtopic',
    'topic',
    'userProfiles',
    'videos',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'tiempoTurco.urls'

WSGI_APPLICATION = 'tiempoTurco.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'tiempoTurco',
        'USER': 'root',
        'PASSWORD': 'Feyza2015',
        'HOST': '',
        'PORT': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-co' #Por defecto'en-us'

TIME_ZONE = 'America/Bogota'    #Por defecto es 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = os.sep.join(
    os.path.abspath(__file__).split(os.sep)[:-2] + ['media']
)
MEDIA_URL = '/media/'

#Backends
#AUTHENTICATION_BACKENDS = (
#    'django.contrib.auth.backends.ModelBackend',
#    'social.backends.google.GoogleOAuth2',
#    'social.backends.facebook.FacebookOAuth2'
#    'userProfiles.backends.EmailBackend',
#)