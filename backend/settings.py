

"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/

"""

import os
from pathlib import Path
from datetime import timedelta
# import pymysql
# pymysql.install_as_MySQLdb()
import dj_database_url


from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent

# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# # settings.py

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'web/static'),
# ]
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# settings.py

BASE_DIR = Path(__file__).resolve().parent.parent

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'web/static'),
# ]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATICFILES_DIRS = []


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-t*wzc7!5=0f6iu-hdm_3vm_gwtm+$vo(v*)=#yu_@zk)=p+rlp"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = ['localhost', '127.0.0.1' , 'project-carwash.onrender.com', '87e4-5-28-177-153.ngrok-free.app']





# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'base.apps.BaseConfig',

    'rest_framework',
    'rest_framework_simplejwt.token_blacklist',
    'djoser',
    "corsheaders",
    'paypal.standard.ipn',
    'django_rest_passwordreset',
#     'paypal.standard',
# ]
]
REST_FRAMEWORK = {
# ---------------------------------------------
# 'DEFAULT_PERMISSION_CLASSES': 
# ('rest_framework.permission.IsAuthenticated',),
# ------------------------------------------------------

'DEFAULT_AUTHENTICATION_CLASSES': 
('rest_framework_simplejwt.authentication.JWTAuthentication',)
        
  

}




SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=90),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": False,

    "ALGORITHM": "HS256",
    "VERIFYING_KEY": None,
    "AUDIENCE": None,
    "ISSUER": None,
    "JSON_ENCODER": None,
    "JWK_URL": None,
    "LEEWAY": 0,

    "AUTH_HEADER_TYPES": ("Bearer",),
    # 'AUTH_HEADER_TYPES': ('JWT',),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",

    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    # "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",

    "JTI_CLAIM": "jti",

    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),

    # "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    # "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    # "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
    # "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
    # "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
    # "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
}


# # ------------------------------------------------------

# DJOSER ={
#     'LOGIN_FIELD': 'email',
#     'USER_CREATE_PASSWORD_RETYPE':True,
#     'ACTIVATION_URL':'/activate/{uid}/{token}',
#     'SEND_ACTIVATION_EMAIL':True,
#     'SEND_CONFIRMATION_EMAIL':True,
#     'PASSWORD_CHANGE_EMAIL_CONFIRMATION':True,
#     'PASSWORD_RESET_CONFIRM_URL':'password-reset/{uid}/{token}',
#     'SET_PASSWORD_RETYPE':True,
#     'PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND': True,
#     'TOKEN_MODEL': None,
#     'SERIALIZERS':{
#         'user_create': 'account.serializers.UserCreateSerializer',
#         'user': 'account.serializers.UserCreateSerializer',
#         'user_delete': 'account.serializers.UserCreateSerializer',
#     }
# }

DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': '#/password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': '#/username/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': '#/activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'SERIALIZERS': {},
}
  
    

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

     "corsheaders.middleware.CorsMiddleware",

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# ------------------------------------------------------

# DATABASES = {
#     'default': {
#             'ENGINE': 'django.db.backends.mysql',
#             'HOST': os.getenv("DB_HOST"),
#             'USER': os.getenv("DB_USERNAME"),
#             'PASSWORD': os.getenv("DATABASE_PASSWORD"),
#             'NAME': os.getenv("DB_DBNAME"),
#             'PORT': '',
#     }
# }

# # -------------------------------------------------------------
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'project_2',
#         'USER': 'root',
#         'PASSWORD': os.getenv("DATABASE_PASSWORD"),
#         'HOST': 'localhost',
#         'PORT': '3306'
#     }
# }



# import pymysql  # noqa: 402
# pymysql.install_as_MySQLdb()
# if os.getenv('GAE_APPLICATION', None):
#     # Running on production App Engine, so connect to Google Cloud SQL using
#     # the unix socket at /cloudsql/
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.mysql',
#             'HOST': os.getenv("DB_HOST"),
#             'USER': os.getenv("DB_USERNAME"),
#             'PASSWORD': os.getenv("DATABASE_PASSWORD"),
#             'NAME': os.getenv("DB_DBNAME"),
#             'PORT': '',

#         }
#     }
# else:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.mysql',
#             'HOST': 'localhost',
#             'PORT': '3306',
#             'USER': 'root',
#             'PASSWORD': os.getenv("DATABASE_PASSWORD"),
#             'NAME':'project_2',
#         }
#     }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}


DATABASES["default"]= dj_database_url.parse("postgres://shani:ZCEu7TEQyPLXe9KUkWBMSUjmCze166ja@dpg-ck9ge770vg2c738ssi9g-a.oregon-postgres.render.com/car_wash_wl6v")


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'shanilevi88761234@gmail.com'
# EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_HOST_PASSWORD = 'dnlxtvjnnwduywpi'
EMAIL_USE_TLS = True



# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

# USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# # -----------------------------------------
# AUTH_USER_MODEL = 'account.User'




CORS_ALLOW_ALL_ORIGINS = True

# ---------------------------------------------------------
# CORS_ALLOWED_ORIGINS  = [
#     "http://localhost:3000",
# "http://127.0.0.1:3000",
# ]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True


# PAYPAL_CLIENT_ID = os.getenv("PAYPAL_CLIENT_ID")
# PAYPAL_CLIENT_SECRET = os.getenv("PAYPAL_CLIENT_SECRET")
# PAYPAL_WEBHOOK_ID = os.getenv("PAYPAL_WEBHOOK_ID")



PAYPAL_CLIENT_ID = "AfbUGtEZE9rX77TgWCDqKGON5e5BuEiPxc5DEudSA88h-_7erNXkaEMruhvbOZtLiV6e1wRmCsr4ENIs"
PAYPAL_CLIENT_SECRET = "EBCRofzTNfD0jZugzAaVbD17Iq-TClCQfT1D9WqxWidTP8YKOUdlV13m1WfTTa0mkJpQOeWPHzi1DT5a"
PAYPAL_WEBHOOK_ID = "46N82677VJ8600301"

PAYPAL_TEST = True
PAYPAL_RECIVER_EMAIL = 'sb-7jvd4726700262@business.example.com'
