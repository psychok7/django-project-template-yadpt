from .base import *

BASE_URL = 'http://localhost:8000'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'dorothy_postgis',
        'PORT': '5432',
    }
}

# BROKER_URL = 'redis://prio_redis:6379/0'
# COMPRESS_ENABLED = False