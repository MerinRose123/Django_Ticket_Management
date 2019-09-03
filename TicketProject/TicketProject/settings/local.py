from .settings import *

# Allowing all users in the network to access the site.
ALLOWED_HOSTS = ['*']

# changing the default user model to custom user model
AUTH_USER_MODEL = 'user_management.User'

# Changing The database backend to postgres.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ticketdb',
        'USER': 'admin',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
        'TEST': {
                    'NAME': 'test',
                },
            }
}

# To include static files to the project from static folder
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')

'''
# setting logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
            'console': {
                'format': '%(name)-12s %(levelname)-8s %(message)s'
            },
            'file': {
                'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
            }
            },
    'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'console'
            },
            'file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'formatter': 'file',
                'filename': '../debug.log'
            }
        },
    'loggers': {
            '': {
                'level': 'DEBUG',
                'handlers': ['console', 'file']
            }
        }
    }

'''