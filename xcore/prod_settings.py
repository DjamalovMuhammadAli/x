from pathlib import Path
from .settings import BASE_DIR

SECRET_KEY = 'django-insecure-*7rcnv=abdan&szjd#$k*ipg*u6yrju=hi2p2599lwvpl-j!*_'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'domein', 'www.domain.uz']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'x_db',
        'USER': 'postgres',
        'PASSWORD': 'ali',
        'HOST': 'localhost',
        'port': '5432',
    }
}

STATIC_DIR = Path(BASE_DIR, 'static')
# STATICFILES_DIRS = [STATIC_DIR]
STATIC_ROOT = Path(BASE_DIR, 'static')
