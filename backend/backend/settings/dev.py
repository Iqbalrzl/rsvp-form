from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@7c$&tf%-3e^1p4==5a@11opo2r@oqs9e26fb6+m_rni4wh@)h'

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'rsvp',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': '03092002'
    }
}
