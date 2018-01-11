#encoding: utf-8
#用于单元测试
from settings import *

DEBUG = True
UNITTEST = True
#UNITTEST = False

# Database settings
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:"
    }
}

# # Session Cache settings
# CACHES = {
#     "default": {
#         "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
#         "LOCATION": "127.0.0.1:11211"
#     }
# }

#BROKER_URL = "redis://127.0.0.1:6379/8"
# CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/9'
#CELERYD_CONCURRENCY = 10

# Log settings
#LOGGING = None
