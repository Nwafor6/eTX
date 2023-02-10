"""
Django settings for main_project project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path
from decouple import config


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('DJANGO_SECRET_KEY', default='django-insecure-ze#orz@61tav545j33$^sv#j4ke3h*yye%)l7=fr2p^@lkuyw%')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DJANGO_DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = ["etx.pythonanywhere.com", "127.0.0.1",'192.168.180.32']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # myapps
    "mainapp.apps.MainappConfig",
    'accounts.apps.AccountsConfig',
    'frontendapp.apps.FrontendappConfig',

    # Third party
    'rest_framework',
    'import_export',
    'drf_yasg',
    'corsheaders',
    "pwa",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]
# production settings
# CSRF_COOKIE_SECURE=True
# SESSION_COOKIE_SECURE=True
# SECURE_SSL_REDIRECT=True
# SESSION_EXPIRE_AT_BROWSER_CLOSE=True
# SECURE_HSTS_SECONDS =True
# SECURE_HSTS_INCLUDE_SUBDOMAINS =True
# SECURE_HSTS_PRELOAD =True

CORS_ORIGIN_ALLOW_ALL=False


CSRF_TRUSTED_ORIGINS = [
    
]
ROOT_URLCONF = 'main_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
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

WSGI_APPLICATION = 'main_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'Transcript_db',
#         'USER': 'nwaforglory6@gmail.com',
#         'PASSWORD': 'Nwafor6.com',
#         'HOST': '181.215.242.78',
#         'PORT': '13873',
#     }
# }
AUTH_USER_MODEL="accounts.CustomUser"
IMPORT_EXPORT_USE_TRANSACTIONS = True
# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# pwa setup
PWA_APP_NAME = "electronic transcript generator"
PWA_APP_DESCRIPTION = "eTX PWA" #app description
PWA_APP_THEME_COLOR = "#000000" # theme color
PWA_APP_BACKGROUND_COLOR = "#ffffff"
PWA_APP_DISPLAY = "standalone"
PWA_APP_SCOPE = "/"
PWA_APP_ORIENTATION = "any"
PWA_APP_START_URL = "/"
PWA_APP_STATUS_BAR_COLOR = "default"
# PWA_APP_ICONS = [{"src": "static/images/app.jpeg", "sizes": "160x160"}]
PWA_APP_ICONS = [{"src": "static/images/eTX-LOGO-ICON.png", "sizes": "640x640"}] # app icon
# PWA_APP_ICONS_APPLE = [{"src": "static/images/app.jpeg", "sizes": "160x160"}]
PWA_APP_ICONS_APPLE = [{"src": "static/images/eTX-LOGO-ICON.png", "sizes": "640x640"}] # app icon apple
PWA_APP_SPLASH_SCREEN = [
    {
        "src": "static/images/eTX-LOGO-ICON.png",
        "media": "(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)",
    }
] # when your app open (splash screen)
PWA_APP_DIR = "ltr"
PWA_APP_LANG = "en-US"


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATICFILES_DIRS =[os.path.join(BASE_DIR, 'static'),]
STATIC_ROOT = os.path.join(BASE_DIR / "staticfiles")
STATIC_URL='/static/'
MEDIA_URL='/media/'
MEDIA_ROOT= os.path.join( BASE_DIR/'media/')
PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, "static/js", "serviceworker.js")

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
