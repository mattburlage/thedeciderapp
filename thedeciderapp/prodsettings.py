from thedeciderapp.settings import *

SECRET_KEY = os.environ.get('DJANGO_KEY')

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mattsmithburlage$decider',
        'USER': 'mattsmithburlage',
        'PASSWORD': os.environ.get('DATABASE_PW'),
        'HOST': 'mattsmithburlage.mysql.pythonanywhere-services.com',
    }
}

ALLOWED_HOSTS = [
    'decider.msb.dev',
]
