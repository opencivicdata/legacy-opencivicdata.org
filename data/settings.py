from pupa.settings import *


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []

ADMINS = (
    ('Paul Tagliamonte', 'paultag@sunlightfoundation.com'),
)


FILE_UPLOAD_HANDLERS = (
    "django.core.files.uploadhandler.MemoryFileUploadHandler",
    "django.core.files.uploadhandler.TemporaryFileUploadHandler",
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
)

ROOT_URLCONF = 'data.urls'
WSGI_APPLICATION = 'data.wsgi.application'

# STATIC_ROOT = os.path.join(os.path.dirname(__file__), '../..', 'collected_static')
# STATIC_URL = '/media/'
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.abspath(os.path.join(os.path.dirname(__file__), '../', 'media')),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.csrf',
)

TEMPLATE_DIRS = (
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates')),
)


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'
LOGIN_URL = '/login/sunlight/'
LOGIN_REDIRECT_URL = '/upload/'


INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
    'opencivicdata',
    'upload',
    'website',
    'sfapp',
)

# Sunlighauth bits. This requires that django-sunlightauth is installed.

AUTHENTICATION_BACKENDS = (
    'sunlightauth.backends.SunlightBackend',
)

# SOCIAL_AUTH_SUNLIGHT_KEY = 'SET IN DJANGO LOCAL SETTINGS'
# SOCIAL_AUTH_SUNLIGHT_SECRET = 'SET IN DJANGO LOCAL SETTINGS'

try:
    from local_settings import *
except ImportError:
    pass
