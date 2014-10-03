import socket
import os
if (socket.gethostname() == 'tor1isawdavid.americas.media.global.loc' or 
	   socket.gethostname() == 'TOR1ISAWDAVID.local'):
#Sean Local
	DATABASES = {
	    'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'isobar_us2',
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

elif (socket.gethostname() == 'roundarch-VirtualBox'):
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
	DEBUG = True
	DEV_MODE = True
	ANALYTICS = True
	AWS_STATE = 'qa'
	AWS_CLOUDFRONT_KEY = 'E2WOKEM8I0BWND'
	LINKED_SITE = 'isobar.gl3304.qa.glueisobar.com'
	CONTACT_BASEURL = 'http://contacts.gl3304.qa.glueisobar.com'


elif (socket.gethostname() == 'dcn-pr-am12'):
# QA
	DATABASES = {
	    'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'isobar_us2',
		'USER': 'isobar_us2',
		'PASSWORD': 'BZ7DqmV5A',
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
	CONTACT_BASEURL = 'http://contacts.gl3304.qa.glueisobar.com'

elif (socket.gethostname() == 'dcn-st-wb11'):
# Staging
	DATABASES = {
	    'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'isobar_us2',
		'USER': 'isobar_us2',
		'PASSWORD': 'BZ7DqmV5A',
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
	CONTACT_BASEURL = 'http://contacts.gl3304.staging.glueisobar.com'

else:
# Production
	DATABASES = {
	    'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'isobar_us2',
		'USER': 'isobar_us2',
		'PASSWORD': 'BZ7DqmV5A',
		'HOST': 'proddb',
		'PORT': '',
	    }
	}
	DEBUG = False
	DEV_MODE = False
	ANALYTICS = True
	AWS_STATE = 'prod'
	AWS_CLOUDFRONT_KEY = 'E1NQ8DHHCJREO9'
	LINKED_SITE = 'origin.isobar.com'
	CONTACT_BASEURL = 'http://contacts.isobar.com'

TIME_ZONE = 'America/Chicago'

CACHE_MIDDLEWARE_KEY_PREFIX = 'isobar_us2'

LANGUAGE_CODE = 'en'

LANGUAGES = (
    ('en', 'English'),
)

DEFAULT_LANGUAGE = 1

ROOT_URLCONF = 'isobar.sites.us2.urls'
AGENCY_NAME = 'roundarch isobar'

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

FILEBROWSER_DIRECTORY = 'img/uploads/wysiwyg/us2/'

ISOBAR_SITE_BOOL = False

LOCAL_CSS = 'css/us/local.css'

LOCAL_JS = 'js/us/local.js'

SERIALIZATION_MODULES = {
    'json': 'wadofstuff.django.serializers.json'
}

BLOG_URL = 'http://blog.roundarchisobar.com/'

BLOG_RSS = 'http://blog.roundarchisobar.com/?feed=rss'

FACEBOOK_RSS = 'http://www.facebook.com/feeds/page.php?format=atom10&id=174908152626053'

NAV_OVERRIDE = 'templates/nav.html'

CONTACT_DEFAULT = 'NORTH AMERICA'

CONTACT_FLYOUT = 'shelf_contact'

LOCAL_LOGO = 'roundarchisobar.jpg'

SHARE_DOMAIN = 'http://roundarchisobar.com'

SITE_TEMPLATE_DIRS = (
	os.path.dirname(__file__),
)

try:
   from local_settings import *
except ImportError:
   pass
