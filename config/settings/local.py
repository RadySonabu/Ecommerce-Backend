from .base import *

DEBUG = True

# INTERNAL_IPS = [
#     "127.0.0.1",
# ]

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": os.path.join(os.path.dirname(BASE_DIR), "db.sqlite3"),
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'OPTIONS': {
            'options': '-c search_path=trashtok-api'
        },
        'NAME': 'vzijcxwv',
        'USER': 'vzijcxwv',
        'HOST': 'satao.db.elephantsql.com',
        'PASSWORD': 'cpoctX16shRe_c6U6L56W8OS-SlxXzPU',
        'PORT': '5432',
    }
}

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 10,
}
CORS_ORIGIN_ALLOW_ALL = True
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static")

# AWS CONFIG
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'staticfiles-ardy'
AWS_QUERYSTRING_AUTH = False
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
# AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = 'public-read'
AWS_LOCATION = 'static'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# DEFAULT_FILE_STORAGE = 'config.settings.storages.MediaStore'

# AWS_S3_VERIFY = True
# AWS_S3_SIGNATURE_VERSION = 's3v4'
# STATICFILES_DIRS = (os.path.join(os.path.dirname(BASE_DIR), "static"),)
# STATIC_URL = "/static/"
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATIC_ROOT = ""
# print(STATIC_ROOT )
# MEDIA_URL = ''
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')