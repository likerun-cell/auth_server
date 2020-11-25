from .default import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2vahiewp55m9lkz*q!hi5i^nyt&vu#7slol0tm##8i2qynhkrr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "postgres",
#         "USER": "postgres",
#         "HOST": "db",
#         "PORT": 5432
#     }
# }

# 创建日志记录器
logger = logging.getLogger('django')

# django-statsd setting
STATSD_HOST = "15.144.16.203"
STATSD_PORT = 8125
