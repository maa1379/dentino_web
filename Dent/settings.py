# import os
# from pathlib import Path
#
# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
#
# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/
#
# # SECURITY WARNING: keep the secret key used in production secret!
#
# SECRET_KEY = "django-insecure-sn3o(16=tb3e^jg^r$$b0jl7y5gbd+7*)-32k+=-s2@2v#t8=y"
#
# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
#
# ALLOWED_HOSTS = []
#
# # Application definition
#
# INSTALLED_APPS = [
#     "django.contrib.auth",
#     "django.contrib.contenttypes",
#     "django.contrib.sessions",
#     "django.contrib.messages",
#     "django.contrib.staticfiles",
#     # local
#     "config.apps.ConfigConfig",
#     "clinic.apps.ClinicConfig",
#     "doctor.apps.DoctorConfig",
#     "account.apps.AccountConfig",
#     "location.apps.LocationConfig",
#     "reservation.apps.ReservationConfig",
#     "blog.apps.BlogConfig",
#     "partial.apps.PartialConfig",
#     "shop.apps.ShopConfig",
#     "order.apps.OrderConfig",
#     # third_party
#     "jalali_date",
#     "rest_framework",
#     "widget_tweaks",
#     "ckeditor",
#     "mptt",
#     "django_jalali",
#     "djreservation",
#     "django_filters",
#     "django.contrib.admin",
#     "rest_framework_simplejwt",
#     "commoncourse.apps.CommoncourseConfig",
#     "jdatetime",
#     "minio_storage",
# ]
#
# MIDDLEWARE = [
#     "django.middleware.security.SecurityMiddleware",
#     "django.contrib.sessions.middleware.SessionMiddleware",
#     "django.middleware.common.CommonMiddleware",
#     "django.middleware.csrf.CsrfViewMiddleware",
#     "django.contrib.auth.middleware.AuthenticationMiddleware",
#     "django.contrib.messages.middleware.MessageMiddleware",
#     "django.middleware.clickjacking.XFrameOptionsMiddleware",
# ]
#
# ROOT_URLCONF = "Dent.urls"
#
# TEMPLATES = [
#     {
#         "BACKEND": "django.template.backends.django.DjangoTemplates",
#         "DIRS": [BASE_DIR / "templates"],
#         "APP_DIRS": True,
#         "OPTIONS": {
#             "context_processors": [
#                 "django.template.context_processors.debug",
#                 "django.template.context_processors.request",
#                 "django.contrib.auth.context_processors.auth",
#                 "django.contrib.messages.context_processors.messages",
#             ],
#         },
#     },
# ]
#
# WSGI_APPLICATION = "Dent.wsgi.application"
#
# # Database
# # https://docs.djangoproject.com/en/3.2/ref/settings/#databases
#
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }
#
# # Password validation
# # https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators
#
# AUTH_PASSWORD_VALIDATORS = [
#     {
#         "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
#     },
# ]
#
# # Internationalization
# # https://docs.djangoproject.com/en/3.2/topics/i18n/
#
# LANGUAGE_CODE = "en-us"
#
# TIME_ZONE = "UTC"
#
# USE_I18N = True
#
# USE_L10N = True
#
# USE_TZ = True
#
# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/3.2/howto/static-files/
#
# STATIC_URL = "/static/"
#
# # Default primary key field type
# # https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
#
# DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
#
# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/3.2/howto/static-files/
#
#
# # Default primary key field type
# # https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
#
#
# STATICFILES_DIRS = [
#     BASE_DIR / "assets",
# ]
#
# STATIC_ROOT = BASE_DIR / "static_cdn" / "static"
# # STATIC_ROOT = BASE_DIR / "/home/dentinoa/public_html/static"
#
# MEDIA_URL = "/media/"
#
# MEDIA_ROOT = BASE_DIR / "static_cdn" / "media"
#
# # MEDIA_ROOT = BASE_DIR / "home/dentinoa/public_html/static"
#
# # ckeditor
# CKEDITOR_CONFIGS = {
#     "default": {
#         "toolbar": "full",
#     },
# }
#
# CKEDITOR_UPLOAD_PATH = "editor/uploads/"
#
# LOGIN_URL = "config:login"
#
# # default settings
# JALALI_DATE_DEFAULTS = {
#     "Strftime": {
#         "date": "%y/%m/%d",
#         "datetime": "%H:%M:%S _ %y/%m/%d",
#     },
#     "Static": {
#         "js": [
#             # loading datepicker
#             "admin/js/django_jalali.min.js",
#             # OR
#             # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.core.js',
#             # 'admin/jquery.ui.datepicker.jalali/scripts/calendar.js',
#             # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.datepicker-cc.js',
#             # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.datepicker-cc-fa.js',
#             # 'admin/js/main.js',
#         ],
#         "css": {
#             "all": [
#                 "admin/jquery.ui.datepicker.jalali/themes/base/jquery-ui.min.css",
#             ]
#         },
#     },
# }
# DEFAULT_FROM_EMAIL = "mail@example.com"
# EMAIL_HOST = "localhost"
# EMAIL_PORT = "1025"
#
# REST_FRAMEWORK = {
#     "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
#     "DEFAULT_AUTHENTICATION_CLASSES": (
#         "rest_framework_simplejwt.authentication.JWTAuthentication",
#     ),
# }
#
# from datetime import timedelta
#
# ...
#
# SIMPLE_JWT = {
#     "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
#     "REFRESH_TOKEN_LIFETIME": timedelta(days=180),
#     "ROTATE_REFRESH_TOKENS": False,
#     "BLACKLIST_AFTER_ROTATION": False,
#     "UPDATE_LAST_LOGIN": False,
#     "ALGORITHM": "HS256",
#     "SIGNING_KEY": SECRET_KEY,
#     "VERIFYING_KEY": None,
#     "AUDIENCE": None,
#     "ISSUER": None,
#     "JWK_URL": None,
#     "LEEWAY": 0,
#     "AUTH_HEADER_TYPES": ("Bearer",),
#     "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
#     "USER_ID_FIELD": "id",
#     "USER_ID_CLAIM": "user_id",
#     "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
#     "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
#     "TOKEN_TYPE_CLAIM": "token_type",
#     "JTI_CLAIM": "jti",
#     "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
#     "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
#     "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
# }

# """
#
#
# Generated by 'django-admin startproject' using Django 3.2.9.
#
# For more information on this file, see
# https://docs.djangoproject.com/en/3.2/topics/settings/
#
# For the full list of settings and their values, see
# https://docs.djangoproject.com/en/3.2/ref/settings/
# # """
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["dentino.app", "dentino-app.darkube.app"]

# Application definition

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # local
    "config.apps.ConfigConfig",
    "clinic.apps.ClinicConfig",
    "doctor.apps.DoctorConfig",
    "account.apps.AccountConfig",
    "location.apps.LocationConfig",
    "reservation.apps.ReservationConfig",
    "blog.apps.BlogConfig",
    "partial.apps.PartialConfig",
    "shop.apps.ShopConfig",
    "cart.apps.CartConfig",
    "order.apps.OrderConfig",
    # third_party
    "jalali_date",
    "rest_framework",
    "widget_tweaks",
    "ckeditor",
    "mptt",
    'minio_storage',
    "django_jalali",
    "djreservation",
    "django_filters",
    "django.contrib.admin",
    "rest_framework_simplejwt",
    "commoncourse.apps.CommoncourseConfig",
    "jdatetime",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "Dent.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "Dent.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field


STATICFILES_DIRS = [
    BASE_DIR / "assets",
]

# STATIC_ROOT = BASE_DIR / "static_cdn" / "static"
STATIC_ROOT = BASE_DIR / "/home/dentinoa/public_html/static"

MEDIA_URL = "/media/"

# MEDIA_ROOT = BASE_DIR / "static_cdn" / "media"

MEDIA_ROOT = BASE_DIR / "home/dentinoa/public_html/static"

# ckeditor
CKEDITOR_CONFIGS = {
    "default": {
        "toolbar": "full",
    },
}

CKEDITOR_UPLOAD_PATH = "editor/uploads/"

LOGIN_URL = "config:login"

JALALI_DATE_DEFAULTS = {
    "Strftime": {
        "date": "%y/%m/%d",
        "datetime": "%H:%M:%S _ %y/%m/%d",
    },
    "Static": {
        "js": [
            # loading datepicker
            "admin/js/django_jalali.min.js",
            # OR
            # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.core.js',
            # 'admin/jquery.ui.datepicker.jalali/scripts/calendar.js',
            # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.datepicker-cc.js',
            # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.datepicker-cc-fa.js',
            # 'admin/js/main.js',
        ],
        "css": {
            "all": [
                "admin/jquery.ui.datepicker.jalali/themes/base/jquery-ui.min.css",
            ]
        },
    },
}
DEFAULT_FROM_EMAIL = "mail@example.com"
EMAIL_HOST = "localhost"
EMAIL_PORT = "1025"

REST_FRAMEWORK = {
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
}

REST_FRAMEWORK = {
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}

from datetime import timedelta

...

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=180),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=180),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": None,
    "AUDIENCE": None,
    "ISSUER": None,
    "JWK_URL": None,
    "LEEWAY": 0,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "JTI_CLAIM": "jti",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
}

EXPIRED_TIME = 900
#
DEFAULT_FILE_STORAGE = "minio_storage.storage.MinioMediaStorage"
STATICFILES_STORAGE = "minio_storage.storage.MinioStaticStorage"
MINIO_STORAGE_ENDPOINT = "dentinostorage-mohammadaa1379-qtg7akj7.darkube.app"
MINIO_STORAGE_ACCESS_KEY = "CkOrLJLEWPKV5Tcw"
MINIO_STORAGE_SECRET_KEY = "JKcTs0uavE0c0vou"
MINIO_STORAGE_USE_HTTPS = True
MINIO_STORAGE_MEDIA_BUCKET_NAME = "media"
MINIO_STORAGE_AUTO_CREATE_MEDIA_BUCKET = True
MINIO_STORAGE_STATIC_BUCKET_NAME = "static"
MINIO_STORAGE_AUTO_CREATE_STATIC_BUCKET = True




FRONT_END_URL = "dentino.app/app/"
APP_SCHEME = "dentino"

