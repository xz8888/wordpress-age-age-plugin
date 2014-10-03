import socket
import os
print("the host name is %s"%socket.gethostname())
#added by sean to run local client
if (socket.gethostname() == 'tor1isawdavid.americas.media.global.loc' or 
	   socket.gethostname() == 'TOR1ISAWDAVID.local'):
#Sean Local
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

elif (socket.gethostname() == 'dcn-pr-am12'):
# QA
	DATABASES = {
	    'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'isobar_ca',
		'USER': 'isobar_ca',
		'PASSWORD': 'zAVFxfGRy',
		'HOST': 'localhost',
		'PORT': '',
	    }
	}
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
		'NAME': 'isobar_ca',
		'USER': 'isobar_ca',
		'PASSWORD': 'zAVFxfGRy',
		'HOST': 'proddb',
		'PORT': '',
	    }
	}
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
		'NAME': 'isobar_ca',
		'USER': 'isobar_ca',
		'PASSWORD': 'zAVFxfGRy',
		'HOST': 'proddb',
		'PORT': '',
	    }
	}
	DEBUG = False
	DEV_MODE = False
	ANALYTICS = True
	AWS_STATE = 'prod'
	AWS_CLOUDFRONT_KEY = 'E2VWH1JAOC4WI4'
	LINKED_SITE = 'origin.isobar.com'

TIME_ZONE = 'Europe/London'

CACHE_MIDDLEWARE_KEY_PREFIX = 'isobar_ca'

LANGUAGE_CODE = 'en'

LANGUAGES = (
    ('en', 'English'),
    ('fr', 'French'),
)

DEFAULT_LANGUAGE = 1

ROOT_URLCONF = 'isobar.sites.ca.urls'
AGENCY_NAME = 'mindblossom Isobar'

LOCALE_PATHS = (
	os.path.dirname(__file__) + '/locale/',
)

EXTRA_APPS = (
	'apps.jobs',
)

FILEBROWSER_DIRECTORY = 'img/uploads/wysiwyg/ca/'

ISOBAR_SITE_BOOL = False

SITE_TEMPLATE_DIRS = (
	os.path.dirname(__file__),
)

try:
   from local_settings import *
except ImportError:
   pass
