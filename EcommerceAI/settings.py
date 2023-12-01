"""
Django settings for EcommerceAI project.

Generated by 'django-admin startproject' using Django 3.2.22.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

#endpoints
auth_endpoint = os.environ.get('AUTH_SVC_ADDRESS') or '127.0.0.1:7777'
policy_endpoint = os.environ.get('POLICY_SVC_ADDRESS') or '127.0.0.1:9999'
product_endpoint = os.environ.get('PRODUCT_SVC_ADDRESS') or '127.0.0.1:5555'
search_endpoint = os.environ.get('SEARCH_SVC_ADDRESS') or '127.0.0.1:5550'
category_endpoint = os.environ.get('CATEGORY_SVC_ADDRESS') or '127.0.0.1:5500'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-e-b5r^vw!o=z^*b=fbh!_e*bmetilq8qouwvusfm%tz&j(oznl'

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = str(os.environ.get('DEBUG')) == "1"
DEBUG = True

#print(os.environ.get("DJANGO_ALLOWED_HOSTS").split(" "))
ALLOWED_HOSTS = ["*"]
#ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'base',
    'widget_tweaks',

]

LOGOUT_REDIRECT_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = 'login'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'EcommerceAI.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'EcommerceAI.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases




"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}"""

#postgres database

DB_DATABASE = 'igxvggzn'
DB_USERNAME = 'igxvggzn'
DB_PASSWORD = 'd1tAH70iAtxdJYrQuPSBICRvgcfhCdHs'
DB_HOST = 'surus.db.elephantsql.com'

DATABASES = {
    "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": DB_DATABASE,
            "USER": DB_USERNAME,
            "PASSWORD": DB_PASSWORD,
            'HOST': DB_HOST,
            'PORT': 5432, #default port you don't need to mention in docker-compose
            }
}



#mysql
'''
DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.mysql',  
        'NAME': 'molla',  
        'USER': 'root',  
        'PASSWORD': '',  
        'HOST': '127.0.0.1',  
        'PORT': '3306',  
        'OPTIONS': {  
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"  
        }  
    }  
}  
'''

DB_USERNAME = os.environ.get("POSTGRES_USER")
DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
DB_DATABASE = os.environ.get("POSTGRES_DB")
DB_HOST = os.environ.get("POSTGRES_HOST")
DB_PORT = os.environ.get("POSTGRES_PORT")
DB_IS_AVAIL = all([
    DB_USERNAME,
    DB_PASSWORD,
    DB_DATABASE,
    DB_HOST,
    DB_PORT
])


if DB_IS_AVAIL:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": DB_DATABASE,
            "USER": DB_USERNAME,
            "PASSWORD": DB_PASSWORD,
            'HOST': 'db',
            'PORT': 5432, #default port you don't need to mention in docker-compose
        }
    }




# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "EcommerceAI/MyStatic",
]
STATIC_ROOT = BASE_DIR / "static"

MEDIA_URL ='/media/'
MEDIA_ROOT =os.path.join(BASE_DIR,"media")

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

