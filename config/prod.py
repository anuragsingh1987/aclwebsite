from config.common import *
import os

SECRET_KEY = os.environ['SECRET_KEY']
DJANGO_SETTINGS_MODULE = os.environ['DJANGO_SETTINGS_MODULE']
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1','localhost']
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_SES_REGION_NAME = os.environ['AWS_SES_REGION_NAME']
AWS_SES_REGION_ENDPOINT = os.environ['AWS_SES_REGION_ENDPOINT']
AWS_DEFAULT_REGION = os.environ['AWS_DEFAULT_REGION']
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
AWS_S3_CUSTOM_DOMAIN = os.environ['AWS_S3_CUSTOM_DOMAIN']
AWS_LOCATION = os.environ['AWS_LOCATION']
DEFAULT_FROM_EMAIL = os.environ['DEFAULT_FROM_EMAIL']
WSGI_APPLICATION = 'config.wsgi.application'
AWS_DEFAULT_ACL = None
# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':  os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASS'],
        'HOST' : os.environ['HOST'],
        'PORT' : os.environ['PORT'],
    }
}

EMAIL_BACKEND = 'django_amazon_ses.EmailBackend'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'configcio.storage_backends.MediaStorage'
