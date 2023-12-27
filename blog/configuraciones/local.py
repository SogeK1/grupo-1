from .settings import *
# from decouple import config, Csv

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'Tu secret key'

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'apps',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': 3306,
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST_USER = 'Correo electrónico'
EMAIL_HOST_PASSWORD = 'Contraseña'

SITE_NAME = 'Ferplant'