import socket
import os

if (socket.gethostname() == 'tor1isawdavid.americas.media.global.loc' or 
	   socket.gethostname() == 'TOR1ISAWDAVID.local'):
# QA
	DATABASES = {
	    'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'isobar_ca',
		'USER': 'root',
		'PASSWORD': '',
		'HOST': 'localhost',
		'PORT': '',
	    }
	}
	CACHE_BACKEND = 'dummy://'
	CACHE_MIDDLEWARE_SECONDS = 0
	DEBUG = True
	DEV_MODE = True
	SERVE_STATIC_FILES = False
	ANALYTICS = False
	AWS_STATE = 'local'
	AWS_CLOUDFRONT_KEY = ''
	LINKED_SITE = '127.0.0.1:8000' 
elif (socket.gethostname() == 'dcn-st-wb11'):
# Staging
	DATABASES = {
	    'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'isobar_no',
		'USER': 'isobar_no',
		'PASSWORD': 'sPLe1RqKg',
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
		'NAME': 'isobar_no',
		'USER': 'isobar_no',
		'PASSWORD': 'sPLe1RqKg',
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
	AWS_CLOUDFRONT_KEY = 'E2ORXUZMYQC7KU'
	LINKED_SITE = 'origin.isobar.com'

TIME_ZONE = 'Europe/London'

CACHE_MIDDLEWARE_KEY_PREFIX = 'isobar_no'

LANGUAGE_CODE = 'nb'

LANGUAGES = (
	('nb', 'Norwegian'),
    ('en', 'English'),
)

DEFAULT_LANGUAGE = 1

ROOT_URLCONF = 'isobar.sites.no.urls'
AGENCY_NAME = 'Isobar'

LOCALE_PATHS = (
	os.path.dirname(__file__) + '/locale/',
)

EXTRA_APPS = (
	'apps.jobs',
)

FILEBROWSER_DIRECTORY = 'img/uploads/wysiwyg/no/'

ISOBAR_SITE_BOOL = False

SITE_TEMPLATE_DIRS = (
	os.path.dirname(__file__),
)

try:
   from local_settings import *
except ImportError:
   pass
