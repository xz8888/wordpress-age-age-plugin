import socket
import os
import sys

if (socket.gethostname() == 'GLUP319.local'):
# Chris H development
	DATABASES = {
	    'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'isobar_dev',
		'USER': 'root',
		'PASSWORD': 'root',
		'HOST': '127.0.0.1',
		'PORT': '8889',
	    }
	}
	DEBUG = False
	DEV_MODE = True
	SERVE_STATIC_FILES = False
	ANALYTICS = False
	AWS_STATE = 'local'
	AWS_CLOUDFRONT_KEY = ''
	LINKED_SITE = 'glup345.emea.media.global.loc:3002'
elif (socket.gethostname() == 'GLUP353'):
# Chris B development
	DATABASES = {
	    'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'isobar',
		'USER': 'root',
		'PASSWORD': '',
		'HOST': 'localhost',
		'PORT': '',
	    }
	}
	DEBUG = False
	DEV_MODE = True
	SERVE_STATIC_FILES = False
	ANALYTICS = False
	AWS_STATE = 'local'
	LINKED_SITE = 'glup345.emea.media.global.loc:3002'
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
	DEBUG = False
	DEV_MODE = True
	SERVE_STATIC_FILES = False
	ANALYTICS = False
	AWS_STATE = 'local'
	LINKED_SITE = 'glup345.emea.media.global.loc:3002'
elif (socket.gethostname() == 'seb-ashton.local'):
# Seb development
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.mysql',
			'NAME': 'isobar_dev',
			'USER': 'root',
			'PASSWORD': 'root',
			'HOST': 'localhost',
			'PORT': '3606',
		}
	}
	DEBUG = False
	DEV_MODE = True
	SERVE_STATIC_FILES = False
	ANALYTICS = False
	CDN_STREAMING_URL = 's90mm4vvoe7qc.cloudfront.net'
	CDN_DOWNLOAD_URL = 'd1q1cls6zd53i8.cloudfront.net'
	AWS_STATE = 'local'
	LINKED_SITE = 'glup345.emea.media.global.loc:3002'
else:
	DATABASES = {
	    'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': '',
		'USER': '',
		'PASSWORD': '',
		'HOST': 'proddb',
		'PORT': '',
	    }
	}
	DEBUG = False
	DEV_MODE = False
	ANALYTICS = True
	AWS_STATE = 'local'
	LINKED_SITE = 'glup345.emea.media.global.loc:3002'
TIME_ZONE = 'Europe/London'

LANGUAGE_CODE = 'en'

LANGUAGES = (
    ('en', 'English'),
    ('fr', 'French'),
)

DEFAULT_LANGUAGE = 1

ROOT_URLCONF = 'isobar.sites.dev.urls'
AGENCY_NAME = 'glue Isobar'

EXTRA_APPS = (
	'apps.jobs',
)

ISOBAR_SITE_BOOL = False

ROOT_PATH = os.path.dirname(__file__)

SITE_TEMPLATE_DIRS = (
	ROOT_PATH,
)
