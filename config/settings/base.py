from django.utils.translation import gettext_lazy as _

INSTALLED_APPS = ['rdmo_jochenklar', 'rdmo_plugins', *INSTALLED_APPS]

LANGUAGES = (
    ('en', _('English')),
    ('de', _('German')),
    ('fr', _('French')),
    ('it', _('Italian'))
)

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
MIDDLEWARE.append('allauth.account.middleware.AccountMiddleware')

PROJECT_SEND_ISSUE = True

PROJECT_QUESTIONS_AUTOSAVE = True

PROJECT_EXPORTS += [
    ('madmp', _('as maDMP JSON'), 'rdmo_plugins.exports.madmp.MaDMPExport'),
    ('datacite', _('as DataCite XML'), 'rdmo_plugins.exports.datacite.DataCiteExport'),
    ('radar-xml', _('as RADAR XML'), 'rdmo_plugins.exports.radar.RadarExport'),
    ('radar', _('directly to RADAR'), 'rdmo_plugins.exports.radar.RadarExportProvider'),
    ('zenodo', _('directly to Zenodo'), 'rdmo_plugins.exports.zenodo.ZenodoExportProvider')
]

PROJECT_IMPORTS += [
    ('madmp', _('from maDMP'), 'rdmo_plugins.imports.madmp.MaDMPImport'),
    ('datacite', _('from DataCite XML'), 'rdmo_plugins.imports.datacite.DataCiteImport'),
    ('radar', _('from RADAR XML'), 'rdmo_plugins.imports.radar.RadarImport'),
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
    ('mesh_qualifiers', _('Medical Subject Headings (MeSH) qualifiers'), 'rdmo_mesh.providers.QualifierProvider')
]
