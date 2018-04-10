from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'snippet_db',
        'USER': 'postgres',
        'PASSWORD': 'ammg1998',
        'HOST': 'localhost',
        'PORT': '5432',
	}
}


STATICFILES_DIRS = [
	os.path.join(BASE_DIR, "static"),
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'