import socket
import os

if (socket.gethostname() == 'dcn-pr-am12'):
# QA
	DATABASES = {
	    'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'isobar_<country_code>',
		'USER': 'isobar_<country_code>',
		'PASSWORD': '<db_password>',
		'HOST': 'localhost',
		'PORT': '',
	    }
	}
	CACHE_BACKEND = 'dummy://'
	CACHE_MIDDLEWARE_SECONDS = 0
	DEBUG = True
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
		'NAME': 'isobar_<country_code>',
		'USER': 'isobar_<country_code>',
		'PASSWORD': '<db_password>',
		'HOST': 'proddb',
		'PORT': '',
	    }
	}
	CACHE_BACKEND = 'dummy://'
	CACHE_MIDDLEWARE_SECONDS = 0
	DEBUG = True
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
		'NAME': 'isobar_<country_code>',
		'USER': 'isobar_<country_code>',
		'PASSWORD': '<db_password>',
		'HOST': 'proddb',
		'PORT': '',
	    }
	}
	DEBUG = False
	DEV_MODE = False
	ANALYTICS = True
	AWS_STATE = 'prod'
	AWS_CLOUDFRONT_KEY = '<cloudfront_id>'
	LINKED_SITE = 'origin.isobar.com'

TIME_ZONE = 'Europe/London'

CACHE_MIDDLEWARE_KEY_PREFIX = 'isobar_<country_code>'

LANGUAGE_CODE = '<primary_language_code>'

LANGUAGES = (
<language_codes>)

DEFAULT_LANGUAGE = 1

ROOT_URLCONF = 'isobar.sites.<country_code>.urls'
AGENCY_NAME = '<agency_name>'

LOCALE_PATHS = (
	os.path.dirname(__file__) + '/locale/',
)

EXTRA_APPS = (
	'apps.jobs',
)

FILEBROWSER_DIRECTORY = 'img/uploads/wysiwyg/<country_code>/'

ISOBAR_SITE_BOOL = False

SITE_TEMPLATE_DIRS = (
	os.path.dirname(__file__),
)

try:
   from local_settings import *
except ImportError:
   pass