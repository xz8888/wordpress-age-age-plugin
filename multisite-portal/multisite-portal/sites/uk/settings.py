import socket
import os

if (socket.gethostname() == 'GLUP319.local'):
# Chris H development
	DATABASES = {
	    'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'isobar_uk',
		'USER': 'root',
		'PASSWORD': 'root',
		'HOST': '127.0.0.1',
		'PORT': '8889',
	    }
	}
	CACHE_BACKEND = 'dummy://'
	CACHE_MIDDLEWARE_SECONDS = 0
	DEBUG = False
	DEV_MODE = True
	SERVE_STATIC_FILES = False
	ANALYTICS = False
	AWS_STATE = 'local'
	AWS_CLOUDFRONT_KEY = ''
	LINKED_SITE = 'glup345.emea.media.global.loc:3002'
elif (socket.gethostname() == 'chrisblackburn'):
# Chris B development
	DATABASES = {
	    'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'isobar_uk',
		'USER': 'root',
		'PASSWORD': 'test',
		'HOST': 'localhost',
		'PORT': '',
	    }
	}
	CACHE_BACKEND = 'dummy://'
	CACHE_MIDDLEWARE_SECONDS = 3600
	DEBUG = False
	DEV_MODE = True
	SERVE_STATIC_FILES = False
	ANALYTICS = False
	AWS_STATE = 'local'
	AWS_CLOUDFRONT_KEY = 'E2WOKEM8I0BWND'
	LINKED_SITE = 'localhost:8001'
elif (socket.gethostname() == 'GLUP345'):
# JC development
	DATABASES = {
	    'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'isobar_uk',
		'USER': 'root',
		'PASSWORD': '',
		'HOST': 'localhost',
		'PORT': '',
	    }
	}
	CACHE_BACKEND = 'dummy://'
	CACHE_MIDDLEWARE_SECONDS = 0
	DEBUG = False
	DEV_MODE = True
	SERVE_STATIC_FILES = False
	ANALYTICS = False
	AWS_STATE = 'local'
	AWS_CLOUDFRONT_KEY = ''
	LINKED_SITE = 'glup345.emea.media.global.loc:3002'
elif (socket.gethostname() == 'seb-ashton.local'):
# Seb development
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.mysql',
			'NAME': 'isobar_uk',
			'USER': 'root',
			'PASSWORD': 'root',
			'HOST': 'localhost',
			'PORT': '3606',
		}
	}
	CACHE_BACKEND = 'dummy://'
	CACHE_MIDDLEWARE_SECONDS = 0
	DEBUG = False
	DEV_MODE = True
	SERVE_STATIC_FILES = False
	ANALYTICS = False
	AWS_STATE = 'local'
	AWS_CLOUDFRONT_KEY = ''
	LINKED_SITE = 'glup345.emea.media.global.loc:3002'
elif (socket.gethostname() == 'dcn-pr-am12'):
# QA
	DATABASES = {
	    'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'isobar_uk',
		'USER': 'isobar_uk',
		'PASSWORD': 'dEKa9ahE',
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
		'NAME': 'isobar_uk',
		'USER': 'isobar_uk',
		'PASSWORD': 'dEKa9ahE',
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
		'NAME': 'isobar_uk',
		'USER': 'isobar_uk',
		'PASSWORD': 'dEKa9ahE',
		'HOST': 'proddb',
		'PORT': '',
	    }
	}
	CACHE_BACKEND = 'dummy://'
	CACHE_MIDDLEWARE_SECONDS = 3600
	DEBUG = False
	DEV_MODE = False
	ANALYTICS = True
	AWS_STATE = 'prod'
	AWS_CLOUDFRONT_KEY = 'E1VZ9NVISLWJCK'
	LINKED_SITE = 'origin.isobar.com'

TIME_ZONE = 'Europe/London'

CACHE_MIDDLEWARE_KEY_PREFIX = 'isobar_uk'

LANGUAGE_CODE = 'en'

LANGUAGES = (
    ('en', 'English'),
)

DEFAULT_LANGUAGE = 1

ROOT_URLCONF = 'isobar.sites.uk.urls'
AGENCY_NAME = 'glue Isobar'

LOCALE_PATHS = (
	os.path.dirname(__file__) + '/locale/',
)

EXTRA_APPS = (
	'apps.jobs',
)

FILEBROWSER_DIRECTORY = 'img/uploads/wysiwyg/uk/'

ISOBAR_SITE_BOOL = False

SITE_TEMPLATE_DIRS = (
	os.path.dirname(__file__),
)

try:
   from local_settings import *
except ImportError:
   pass
