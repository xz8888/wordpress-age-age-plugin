import os
import socket

print socket.gethostname()
#added by sean to run local client
if (socket.gethostname() == 'tor1isawdavid.americas.media.global.loc' or 
	   socket.gethostname() == 'TOR1ISAWDAVID.local'):
#Sean Local
	DATABASES = {
	    'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'isobar_isobar',
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
	LINKED_SITE = '127.0.0.1:8000' 
elif (socket.gethostname() == 'GLUP319.local'):
# Chris H development
	DATABASES = {
	    'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'isobar_isobar',
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
	LINKED_SITE = ''
elif (socket.gethostname() == 'chrisblackburn'):
# Chris B development
	DATABASES = {
	    'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'isobar',
		'USER': 'root',
		'PASSWORD': 'test',
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
	LINKED_SITE = ''
elif (socket.gethostname() == 'GLUP345'):
# JC development
	DATABASES = {
	    'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'isobar_isobar',
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
	AWS_CLOUDFRONT_KEY = ''
	LINKED_SITE = ''
elif (socket.gethostname() == 'seb-ashton.local'):
# Seb development
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.mysql',
			'NAME': 'isobar_isobar',
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
	LINKED_SITE = ''
elif (socket.gethostname() == 'dcn-pr-am12'):
# QA
	DATABASES = {
	    'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'isobar_isobar',
		'USER': 'isobar_isobar',
		'PASSWORD': 'QEBawra4',
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
	LINKED_SITE = ''
elif (socket.gethostname() == 'dcn-st-wb11'):
# Staging
	DATABASES = {
	    'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'isobar_isobar',
		'USER': 'isobar_isobar',
		'PASSWORD': 'QEBawra4',
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
	AWS_CLOUDFRONT_KEY = 'E1GHOY26V29MER '
	LINKED_SITE = ''
else:
# Production
	DATABASES = {
	    'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'isobar_isobar',
		'USER': 'isobar_isobar',
		'PASSWORD': 'QEBawra4',
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
	LINKED_SITE = ''

TIME_ZONE = 'Europe/London'

LANGUAGE_CODE = 'en'

LANGUAGES = (
    ('en', 'English'),
)

LOCALE_PATHS = (
	os.path.dirname(__file__) + '/locale/',
)

DEFAULT_LANGUAGE = 1

CACHE_MIDDLEWARE_KEY_PREFIX = 'isobar_isobar'

ROOT_URLCONF = 'isobar.sites.isobar.urls'
AGENCY_NAME = 'Isobar'

EXTRA_APPS =  (
	'sites.isobar.location',
	'sites.isobar.cloudfront',
)

HIDE_NETWORK_BAR = 'True'

ISOBAR_SITE = 'True'

ISOBAR_SITE_BOOL = True

FILEBROWSER_DIRECTORY = 'img/uploads/wysiwyg/isobar/'

SITE_TEMPLATE_DIRS = (
	os.path.dirname(__file__),
)
