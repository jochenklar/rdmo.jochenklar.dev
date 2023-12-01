from os import environ
from pathlib import Path

from split_settings.tools import include, optional

from rdmo.core.settings import *

DJANGO_ENV = environ.get('DJANGO_ENV')

BASE_DIR = Path(__file__).parent.parent.parent
MEDIA_ROOT = BASE_DIR / 'media_root'
STATIC_ROOT = BASE_DIR / 'static_root'
STATICFILES_DIRS = [BASE_DIR / 'vendor']

include(
    'base.py',
    optional(f'environments/{DJANGO_ENV}.py'),
    optional('local.py')
)
