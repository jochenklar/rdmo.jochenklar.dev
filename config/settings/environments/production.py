DEBUG = False

SECRET_KEY = ''

ALLOWED_HOSTS = ['localhost', 'ip6-localhost', '127.0.0.1', '[::1]',
                 'rdmo.jochenklar.de', 'rdmo.jochenklar.dev']

ADMINS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'rdmo'
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = ''
EMAIL_PORT = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = ''
EMAIL_USE_SSL = ''
DEFAULT_FROM_EMAIL = ''

EMAIL_RECIPIENTS_CHOICES = [('mail@jochenklar.de', 'Jochen Klar <mail@jochenklar.de>')]

GITHUB_PROVIDER = {
    'client_id': '',
    'client_secret': ''
}

GITLAB_PROVIDER = {
    'gitlab_url': '',
    'client_id': '',
    'client_secret': ''
}

RADAR_PROVIDER = {
    'radar_url': '',
    'client_id': '',
    'client_secret': ''
}

ZENODO_PROVIDER = {
    'zenodo_url': '',
    'client_id': '',
    'client_secret': ''
}

OPENPROJECT_PROVIDER = {
    'openproject_url': '',
    'client_id': '',
    'client_secret': ''
}

LOGGING_PATH = '/var/log/rdmo'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue'
        }
    },
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s: %(message)s'
        },
        'name': {
            'format': '[%(asctime)s] %(levelname)s %(name)s: %(message)s'
        },
        'console': {
            'format': '[%(asctime)s] %(message)s'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'error_log': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': f'{LOGGING_PATH}/error.log',
            'formatter': 'default'
        },
        'rdmo_log': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': f'{LOGGING_PATH}/rdmo.log',
            'formatter': 'name'
        },
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins', 'error_log'],
            'level': 'ERROR',
            'propagate': True
        },
        'rdmo': {
            'handlers': ['rdmo_log'],
            'level': 'DEBUG',
            'propagate': False
        }
    }
}
