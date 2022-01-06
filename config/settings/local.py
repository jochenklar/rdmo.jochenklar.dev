import os
from email.utils import getaddresses

from django.utils.translation import ugettext_lazy as _

from rdmo.core.settings import INSTALLED_APPS, AUTHENTICATION_BACKENDS, PROJECT_EXPORTS, PROJECT_IMPORTS, QUESTIONS_WIDGETS


DEBUG = os.getenv('DEBUG', '').upper() == 'TRUE'
SECRET_KEY = os.getenv('SECRET_KEY')
ALLOWED_HOSTS = ['localhost', 'ip6-localhost', '127.0.0.1', '[::1]', 'rdmo.jochenklar.dev']

if os.getenv('ADMINS'):
    ADMINS = getaddresses([value.strip() for value in os.getenv('ADMINS').split(',')])

LANGUAGE_CODE = 'de-de'
TIME_ZONE = 'Europe/Berlin'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'rdmo'
    }
}

VENDOR_CDN = False

INSTALLED_APPS = [
    'rdmo_jochenklar',
    'rdmo_plugins',
    'rdmo_mesh'
] + INSTALLED_APPS

LANGUAGES = (
    ('en', _('English')),
    ('de', _('German')),
    ('fr', _('French')),
    ('it', _('Italian'))
)

if os.getenv('EMAIL_HOST'):
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = os.getenv('EMAIL_HOST')
    EMAIL_PORT = os.getenv('EMAIL_PORT')
    EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
    EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', '').upper() == 'TRUE'
    EMAIL_USE_SSL = os.getenv('EMAIL_USE_SSL', '').upper() == 'TRUE'
    DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')

ACCOUNT = True
ACCOUNT_SIGNUP = True
ACCOUNT_TERMS_OF_USE = False

SOCIALACCOUNT = True
SOCIALACCOUNT_SIGNUP = True

INSTALLED_APPS += [
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.gitlab',
    'allauth.socialaccount.providers.orcid',
]

AUTHENTICATION_BACKENDS.append('allauth.account.auth_backends.AuthenticationBackend')

PROJECT_SEND_ISSUE = True

if os.getenv('EMAIL_RECIPIENTS_CHOICES'):
    EMAIL_RECIPIENTS_CHOICES = [
        (email, '{} <{}>'.format(realname, email))
        for realname, email in getaddresses([value.strip() for value in os.getenv('ADMINS').split(',')])
    ]

PROJECT_QUESTIONS_AUTOSAVE = True

PROJECT_EXPORTS += [
    ('madmp', _('as maDMP JSON'), 'rdmo_plugins.exports.madmp.MaDMPExport'),
    ('datacite', _('as DataCite XML'), 'rdmo_plugins.exports.datacite.DataCiteExport'),
    ('radar', _('as RADAR XML'), 'rdmo_plugins.exports.radar.RadarExport')
]

PROJECT_IMPORTS += [
    ('madmp', _('from maDMP'), 'rdmo_plugins.imports.madmp.MaDMPImport'),
    ('datacite', _('from DataCite XML'), 'rdmo_plugins.imports.datacite.DataCiteImport'),
    ('radar', _('from RADAR XML'), 'rdmo_plugins.imports.radar.RadarImport'),
]

OPTIONSET_PROVIDERS = [
    ('re3data', _('Repositories from re3data'), 'rdmo_re3data.providers.Re3DataProvider'),
    ('mesh_descriptors', _('Medical Subject Headings (MeSH) descriptors'), 'rdmo_mesh.providers.DescriptorProvider'),
    ('mesh_qualifiers', _('Medical Subject Headings (MeSH) qualifiers'), 'rdmo_mesh.providers.QualifierProvider')
]

SERVICE_PROVIDERS = [
    ('github', _('GitHub'), 'rdmo.services.providers.GitHubProvider'),
    ('gitlab', _('GitLab'), 'rdmo.services.providers.GitLabProvider')
]

GITHUB_PROVIDER = {
    'client_id': os.getenv('GITHUB_PROVIDER_CLIENT_ID'),
    'client_secret': os.getenv('GITHUB_PROVIDER_CLIENT_SECRET')
}

GITLAB_PROVIDER = {
    'client_id': os.getenv('GITLAB_PROVIDER_CLIENT_ID'),
    'client_secret': os.getenv('GITLAB_PROVIDER_CLIENT_SECRET')
}

QUESTIONS_WIDGETS += [
    ('mesh_descriptor', _('MeSH descriptor'), 'rdmo_mesh.widgets.DescriptorWidget'),
    ('mesh_qualifier', _('MeSH qualifier'), 'rdmo_mesh.widgets.QualifierWidget')
]

LOGGING_DIR = os.getenv('LOGGING_DIR', 'log')
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
            'class':'logging.FileHandler',
            'filename': os.path.join(LOGGING_DIR, 'error.log'),
            'formatter': 'default'
        },
        'rdmo_log': {
            'level': 'DEBUG',
            'class':'logging.FileHandler',
            'filename': os.path.join(LOGGING_DIR, 'rdmo.log'),
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
