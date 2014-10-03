import socket
import os

if (socket.gethostname() == 'roundarch-VirtualBox'):
# LOCAL
	DATABASES = {
	    'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'isobar_roundarch',
		'USER': 'root',
		'PASSWORD': 'roundarch',
		'HOST': '',
		'PORT': '',
	    }
	}

	CACHE_BACKEND = 'dummy://'
	CACHE_MIDDLEWARE_SECONDS = 0
	DEBUG = False
	DEV_MODE = True
	ANALYTICS = True
	AWS_STATE = 'qa'
	AWS_CLOUDFRONT_KEY = 'E2WOKEM8I0BWND'
	LINKED_SITE = 'isobar.gl3304.qa.glueisobar.com'
	
elif (socket.gethostname() == 'dcn-pr-am12'):
# QA
	DATABASES = {
	    'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'isobar_roundarch',
		'USER': 'isobar_roundarch',
		'PASSWORD': 'Owp7ChiUy',
		'HOST': '',
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
		'NAME': 'isobar_roundarch',
		'USER': 'isobar_roundarch',
		'PASSWORD': 'Owp7ChiUy',
		'HOST': '',
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
		'NAME': 'isobar_roundarch',
		'USER': 'root',
		'PASSWORD': 'roundarch',
		'HOST': '',
		'PORT': '',
	    }
	}
	DEBUG = False
	DEV_MODE = False
	ANALYTICS = False
	AWS_STATE = 'prod'
	AWS_CLOUDFRONT_KEY = 'E1BUNRJMQEZL35'
	LINKED_SITE = 'origin.isobar.com'

TIME_ZONE = 'America/Chicago'

CACHE_MIDDLEWARE_KEY_PREFIX = 'isobar_roundarch'

LANGUAGE_CODE = 'en'

LANGUAGES = (
    ('en', 'English'),
)

DEFAULT_LANGUAGE = 1

ROOT_URLCONF = 'isobar.sites.roundarch.urls'
AGENCY_NAME = 'roundarch Isobar'

LOCALE_PATHS = (
	os.path.dirname(__file__) + '/locale/',
)

EXTRA_APPS = (
	'apps.aboutisobar',
	'apps.contactisobar',
	'apps.workisobar',
	'apps.labsisobar',
	'apps.video_promo',
	'apps.homeisobar',
	'apps.careerisobar',
)

FILEBROWSER_DIRECTORY = 'img/uploads/wysiwyg/roundarch/'

ISOBAR_SITE_BOOL = False

LOCAL_CSS = 'css/us/local.css'

SERIALIZATION_MODULES = {
    'json': 'wadofstuff.django.serializers.json'
}

BLOG_URL = 'http://172.18.52.56/'

BLOG_RSS = 'http://172.18.52.56/?feed=rss'

FACEBOOK_RSS = 'http://www.facebook.com/feeds/page.php?format=atom10&id=174908152626053'

NAV_OVERRIDE = 'templates/nav.html'

CONTACT_DEFAULT = 'NORTH AMERICA'

SHARE_DOMAIN = 'http://roundarchisobar.com'

SITE_TEMPLATE_DIRS = (
	os.path.dirname(__file__),
)

try:
	from local_settings import *
except ImportError:
	pass
