from .base import *
import dj_database_url
# Override base.py settings here

DEBUG = False

ALLOWED_HOSTS = ['.herokuapp.com']

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)