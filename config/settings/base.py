from django.utils.translation import gettext_lazy as _

INSTALLED_APPS = ['rdmo_jochenklar', *INSTALLED_APPS]

LANGUAGES = (
    ('en', _('English')),
    ('de', _('German')),
    ('fr', _('French')),
    ('it', _('Italian')),
    ('es', _('Spanish'))
)

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

VENDOR_CDN = False
