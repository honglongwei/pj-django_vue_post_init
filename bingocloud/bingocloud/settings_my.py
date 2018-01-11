#encoding: utf-8
from settings import *


# CACHES = {
#     "default": {
#         "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
#         "LOCATION": "127.0.0.1:11211"
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "",
        "USER":"",
        "PASSWORD":"",
        "HOST":"127.0.0.1",
        "PORT":"3306"
    }
}

BROKER_URL = "redis://127.0.0.1:6379/8"
# CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/9'
CELERYD_CONCURRENCY = 10
