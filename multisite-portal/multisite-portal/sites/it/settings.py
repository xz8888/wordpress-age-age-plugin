import socket
import os

if (socket.gethostname() == 'dcn-pr-am12'):
# QA
	DATABASES = {
	    'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'isobar_it',
		'USER': 'isobar_it',
		'PASSWORD': 'RgrMnLhPb',
		'HOST': 'localhost',
		'PORT': '',
	    }
	}
	CACHE_BACKEND = 'dummy://'
	CACHE_MIDDLEWARE_SECONDS = 0
	DEBUG = False
	DEV_MODE = False
	ANALYTICS = False
	AWS_STATE = 'qa'
	AWS_CLOUDFRONT_KEY = 'E2WOKEM8I0BWND'
	LINKED_SITE = 'isobar.gl3304.qa.glueisobar.com'
elif (socket.gethostname() == 'dcn-st-wb11'):
# Staging
	DATABASES = {
	    'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'isobar_it',
		'USER': 'isobar_it',
		'PASSWORD': 'RgrMnLhPb',
		'HOST': 'proddb',
		'PORT': '',
	    }
	}
	CACHE_BACKEND = 'dummy://'
	CACHE_MIDDLEWARE_SECONDS = 0
	DEBUG = False
	DEV_MODE = False
	ANALYTICS = False
	AWS_STATE = 'staging'
	AWS_CLOUDFRONT_KEY = 'E1GHOY26V29MER'
	LINKED_SITE = 'isobar.gl3304.staging.glueisobar.com'
else:
# Production
	DATABASES = {
	    'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'isobar_it',
		'USER': 'isobar_it',
		'PASSWORD': 'RgrMnLhPb',
		'HOST': 'proddb',
		'PORT': '',
	    }
	}
	CACHE_BACKEND = 'db://site_cache?timeout=3600&max_entries=5000'
	CACHE_MIDDLEWARE_SECONDS = 3600
	DEBUG = False
	DEV_MODE = False
	ANALYTICS = True
	AWS_STATE = 'prod'
	AWS_CLOUDFRONT_KEY = 'E1O54IUXZOY73J'
	LINKED_SITE = 'origin.isobar.com'

TIME_ZONE = 'Europe/London'

CACHE_MIDDLEWARE_KEY_PREFIX = 'isobar_it'

LANGUAGE_CODE = 'it'

LANGUAGES = (
    ('it', 'Italian'),
)

DEFAULT_LANGUAGE = 1

ROOT_URLCONF = 'isobar.sites.it.urls'
AGENCY_NAME = 'Isobar Italy'

LOCALE_PATHS = (
	os.path.dirname(__file__) + '/locale/',
)

EXTRA_APPS = (
	'apps.jobs',
)

FILEBROWSER_DIRECTORY = 'img/uploads/wysiwyg/it/'

ISOBAR_SITE_BOOL = False

SITE_TEMPLATE_DIRS = (
	os.path.dirname(__file__),
)

try:
   from local_settings import *
except ImportError:
   pass
