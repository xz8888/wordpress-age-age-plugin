import socket
import os

if (socket.gethostname() == 'dcn-pr-am12'):
# QA
	DATABASES = {
	    'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'isobar_de',
		'USER': 'isobar_de',
		'PASSWORD': 'pMVH0sbbF',
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
		'NAME': 'isobar_de',
		'USER': 'isobar_de',
		'PASSWORD': 'pMVH0sbbF',
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
		'NAME': 'isobar_de',
		'USER': 'isobar_de',
		'PASSWORD': 'pMVH0sbbF',
		'HOST': 'proddb',
		'PORT': '',
	    }
	}
	DEBUG = False
	DEV_MODE = False
	ANALYTICS = True
	AWS_STATE = 'prod'
	AWS_CLOUDFRONT_KEY = 'EO5EZJPDVEQRJ'
	LINKED_SITE = 'origin.isobar.com'

TIME_ZONE = 'Europe/London'

CACHE_MIDDLEWARE_KEY_PREFIX = 'isobar_de'

LANGUAGE_CODE = 'de'

LANGUAGES = (
    #('en', 'English'),
    ('de', 'German'),
)

DEFAULT_LANGUAGE = 1

ROOT_URLCONF = 'isobar.sites.de.urls'
AGENCY_NAME = 'Xenion Isobar'

LOCALE_PATHS = (
	os.path.dirname(__file__) + '/locale/',
)

EXTRA_APPS = (
	'apps.jobs',
)

FILEBROWSER_DIRECTORY = 'img/uploads/wysiwyg/de/'

ISOBAR_SITE_BOOL = False

SITE_TEMPLATE_DIRS = (
	os.path.dirname(__file__),
)

try:
   from local_settings import *
except ImportError:
   pass
