from django.utils.translation import gettext_lazy as _

SECRET_KEY = ''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'rdmo'
    }
}

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

ALLOWED_HOSTS = ['rdmo.jochenklar.dev']

INSTALLED_APPS = [
    'rdmo_radar',
    'rdmo_zenodo',
    'rdmo_orcid',
    'rdmo_ror',
    'rdmo_gnd',
    'rdmo_wikidata',
    *INSTALLED_APPS
]

ADMINS = [('Jochen Klar', 'admin@jochenklar.de')]

INSTALLED_APPS = ['rdmo_jochenklar', *INSTALLED_APPS]

LANGUAGES = (
    ('en', _('English')),
    ('de', _('German')),
    ('fr', _('French')),
    ('it', _('Italian')),
    ('es', _('Spanish'))
)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.jochenklar.de'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'rdmo@jochenklar.de'
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
DEFAULT_FROM_EMAIL = 'noreply@jochenklar.de'

ACCOUNT = True
ACCOUNT_SIGNUP = False
ACCOUNT_TERMS_OF_USE = False

SOCIALACCOUNT = True
SOCIALACCOUNT_SIGNUP = True

INSTALLED_APPS += [
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.orcid',
]

AUTHENTICATION_BACKENDS.append('allauth.account.auth_backends.AuthenticationBackend')
MIDDLEWARE.append('allauth.account.middleware.AccountMiddleware')

PROJECT_SEND_ISSUE = True

EMAIL_RECIPIENTS_CHOICES = [('mail@jochenklar.de', 'Jochen Klar <mail@jochenklar.de>')]

PROJECT_CONTACT = True
PROJECT_CONTACT_RECIPIENTS = [('mail@jochenklar.de', 'Jochen Klar <mail@jochenklar.de>')]

PROJECT_VIEWS_SYNC = True
PROJECT_TASKS_SYNC = True

PROJECT_EXPORTS += [
    ('madmp', _('as maDMP JSON'), 'rdmo_plugins.exports.madmp.MaDMPExport'),
    ('datacite', _('as DataCite XML'), 'rdmo_plugins.exports.datacite.DataCiteExport'),
    ('radar-xml', _('as RADAR XML'), 'rdmo_radar.exports.RadarExport'),
    ('radar', _('directly to RADAR'), 'rdmo_radar.exports.RadarExportProvider'),
    ('zenodo', _('directly to Zenodo'), 'rdmo_zenodo.exports.ZenodoExportProvider')
]

PROJECT_IMPORTS += [
    ('madmp', _('from maDMP'), 'rdmo_plugins.imports.madmp.MaDMPImport'),
    ('datacite', _('from DataCite XML'), 'rdmo_plugins.imports.datacite.DataCiteImport'),
    ('radar', _('from RADAR XML'), 'rdmo_radar.imports.RadarImport'),
    ('url', _('from URL'), 'rdmo.projects.imports.URLImport'),
    ('github', _('from GitHub'), 'rdmo_github.providers.GitHubImport'),
    ('gitlab', _('from GitLab'), 'rdmo_gitlab.providers.GitLabImport')
]

PROJECT_IMPORTS_LIST = ['url', 'github', 'gitlab']

PROJECT_ISSUE_PROVIDERS = [
    ('github', _('GitHub Provider'), 'rdmo_github.providers.GitHubIssueProvider'),
    ('gitlab', _('GitLab Provider'), 'rdmo_gitlab.providers.GitLabIssueProvider'),
    ('openproject', _('OpenProject Provider'), 'rdmo_openproject.providers.OpenProjectIssueProvider'),
]

OPTIONSET_PROVIDERS = [
    ('re3data', _('Repositories from re3data'), 'rdmo_re3data.providers.Re3DataProvider'),
    ('mesh_descriptors', _('Medical Subject Headings (MeSH) descriptors'), 'rdmo_mesh.providers.DescriptorProvider'),
    ('mesh_qualifiers', _('Medical Subject Headings (MeSH) qualifiers'), 'rdmo_mesh.providers.QualifierProvider'),
    ('orcid', _('ORCID Provider'), 'rdmo_orcid.providers.OrcidProvider'),
    ('ror', _('ROR Provider'), 'rdmo_ror.providers.RorProvider'),
    ('gnd', _('GND Provider'), 'rdmo_gnd.providers.GNDProvider'),
    ('wikidata', _('Wikidata Provider'), 'rdmo_wikidata.providers.WikidataProvider'),
]

GITHUB_PROVIDER = {
    'client_id': '',
    'client_secret': ''
}

GITLAB_PROVIDER = {
    'gitlab_url': 'https://gitlab.com',
    'client_id': '',
    'client_secret': ''
}

RADAR_PROVIDER = {
    'radar_url': 'https://test.radar-service.eu',
    'client_id': '',
    'client_secret': '',
    'redirect_uri': 'https://rdmo.jochenklar.dev/services/oauth/radar/callback/'
}

ZENODO_PROVIDER = {
    'zenodo_url': 'https://zenodo.org',
    'client_id': '',
    'client_secret':  ''
}

OPENPROJECT_PROVIDER = {
    'openproject_url': 'https://openproject.jochenklar.dev',
    'client_id': '',
    'client_secret': ''
}

ORCID_PROVIDER_MAP = [
    {
        'orcid': 'https://rdmorganiser.github.io/terms/domain/project/dataset/creator/orcid',
        'given_name': 'https://rdmorganiser.github.io/terms/domain/project/dataset/creator/given_name',
        'family_name': 'https://rdmorganiser.github.io/terms/domain/project/dataset/creator/family_name',
        'affiliation': 'https://rdmorganiser.github.io/terms/domain/project/dataset/creator/affiliation',
    }
]

ORCID_PROVIDER_HEADERS = {
    'User-Agent': 'rdmo.jochenklar.dev/1.0 (admin@jochenklar.de) rdmo-plugins-orcid/1.0'
}

ROR_PROVIDER_MAP = [
    {
        'ror': 'https://rdmorganiser.github.io/terms/domain/project/partner/ror',
        'alias': 'https://rdmorganiser.github.io/terms/domain/project/partner/id',
        'acronym': 'https://rdmorganiser.github.io/terms/domain/project/partner/id',
        'name': 'https://rdmorganiser.github.io/terms/domain/project/partner/name',
    }
]

ROR_PROVIDER_HEADERS = {
    'User-Agent': 'rdmo.jochenklar.dev/1.0 (admin@jochenklar.de) rdmo-plugins-ror/1.0'
}

GND_PROVIDER_MAP = [
    {
        'gndIdentifier': 'https://rdmorganiser.github.io/terms/domain/project/research_question/keywords/gnd',
        'preferredName': 'https://rdmorganiser.github.io/terms/domain/project/research_question/keywords'
    }
]

GND_PROVIDER_HEADERS = {
    'User-Agent': 'rdmo.jochenklar.dev/1.0 (admin@jochenklar.de) rdmo-plugins-gnd/1.0'
}

WIKIDATA_PROVIDER_HEADERS = {
    'User-Agent': 'rdmo.jochenklar.dev/1.0 (admin@jochenklar.de) rdmo-plugins-wikidata/1.0'
}

LOGGING_PATH = '/var/log/django/rdmo'
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
