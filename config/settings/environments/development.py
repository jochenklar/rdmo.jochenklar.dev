DEBUG = True

SECRET_KEY = 'not a secret key'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'rdmo_jochenklar'
    }
}

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
