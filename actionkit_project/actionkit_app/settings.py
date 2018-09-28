import os

# Break out the given BASE_DIR var into two vars, based on Django docs' distinction between Apps and Projects
# The app root directory
APP_ROOT_DIR = os.path.dirname(__file__)
# The project root directory
PROJECT_ROOT_DIR = os.path.abspath(os.getcwd())

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'not4productiondothorse'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Need to list the app here in order for template tags to work
# https://docs.djangoproject.com/en/1.8/howto/custom-template-tags/
INSTALLED_APPS = ['actionkit_app', 'django.contrib.staticfiles']

MIDDLEWARE_CLASSES = []

ROOT_URLCONF = 'actionkit_app.urls'

TEMPLATE_HOMEPAGE = os.path.join(PROJECT_ROOT_DIR, 'template_set_homepage')
TEMPLATES_DIR = [TEMPLATE_HOMEPAGE]
if os.environ.get('TEMPLATE_DIR'):
    TEMPLATE_DIR_PATH = os.path.join(PROJECT_ROOT_DIR, os.environ.get('TEMPLATE_DIR'))
    TEMPLATES_DIR.append(TEMPLATE_DIR_PATH)
else:
    DEFAULT_TEMPLATES_PATH = os.path.join(PROJECT_ROOT_DIR, 'template_set_orig')
    TEMPLATES_DIR.append(DEFAULT_TEMPLATES_PATH)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': TEMPLATES_DIR
    },
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT_DIR, "staticfiles"), 
]
