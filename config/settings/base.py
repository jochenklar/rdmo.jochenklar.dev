# add theme

INSTALLED_APPS = [
    'rdmo_jochenklar',
    *INSTALLED_APPS
]

# enable allauth

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
