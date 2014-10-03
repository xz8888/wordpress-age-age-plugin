import os
import sys

SITE_ID = 1
SITE = os.environ.get('SITE')
SITE_MODULE = "sites.%s" % str.strip(SITE)
exec "from %s.settings import *" % (SITE_MODULE)

POST_AUTH = 'swub7Pe6AgUb3qe2u4EwUganuThegEst'

ADMINS = (
    ('Chris Gyorffy', 'christopher.gyorffy@isobar.com'),
)

MANAGERS = ADMINS


ROOT_PATH = os.path.dirname(__file__)

APP_PATH = ROOT_PATH + '/apps/'

sys.path.insert(0, os.path.join(APP_PATH))

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True
	
# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ROOT_PATH + '/../docroot/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/static/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'htlrx$)azn$n_hy_9+l08k&re2x268nzu@+)907@7oj+ee+v$^'

# Amazon AWS details
AWS_ACCESS_KEY = 'AKIAIFAX5IAXF4MDE65A'
AWS_SECRET_KEY = '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'
AWS_URL = 'https://s3-eu-west-1.amazonaws.com/'
AWS_BUCKET = 'isobar'
AWS_CLOUDFRONT_CDN_KEY = 'E3AW1L63L482Z9'
AWS_CLOUDFRONT_STREAMING_KEY = 'EBEJ2XS6FL22K'
CDN_STREAMING_URL = 'streaming.cdn.isobar.com'
CDN_DOWNLOAD_URL = 'cdn.isobar.com'

# Zencoder
ZENCODER_API_KEY = 'f73ef7af1942447849dc7ba6b819a004'

CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True

CACHE_BACKEND = 'dummy://'
CACHE_MIDDLEWARE_SECONDS = 3600

APPEND_SLASH = False

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'apps.common.middleware.ForceDefaultLanguageMiddleware',
    'transurlvania.middleware.URLCacheResetMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'multilingual.middleware.DefaultLanguageMiddleware',
    'transurlvania.middleware.URLTransMiddleware',
    'transurlvania.middleware.LangInPathMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'context_processors.settings',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'multilingual.context_processors.multilingual',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'transurlvania.context_processors.translate',
)

TEMPLATE_DIRS = (
	ROOT_PATH + '/templates/',
	APP_PATH,
)

# Prepend a list of site-specific template directories to the TEMPLATE_DIRS
try:
	TEMPLATE_DIRS = SITE_TEMPLATE_DIRS + TEMPLATE_DIRS
except NameError:
	pass
    
TINYMCE_DEFAULT_CONFIG = {
	'plugins': "spellchecker,paste",
	'theme': "advanced",
	'theme_advanced_styles': "Intro=intro",
	'theme_advanced_buttons1': 'bold,italic,formatselect,styleselect,|,undo,redo,|,bullist,numlist,|,link,unlink,|,image,|,removeformat,charmap,|,cleanup,code',
	'theme_advanced_blockformats': "h2,h3,p,blockquote",
	'theme_advanced_buttons2': '',
	'theme_advanced_buttons3': '',
	'theme_advanced_toolbar_location': "top",
	'theme_advanced_toolbar_align': "left",
	'cleanup_on_startup': True,
	'custom_undo_redo_levels': 10,
	'height': "400",
	'file_browser_callback': 'CustomFileBrowser',
	'relative_urls': False,
	'remove_script_host': True,
	'extended_valid_elements': 'iframe[src|width|height|name|align|frameborder]',
}

BASE_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.messages',
	'django.contrib.admin',
	'django.contrib.flatpages',
	'apps.multilingual',
	'apps.tinymce',
	'apps.filebrowser',
	'apps.common',
	'apps.home',
	'apps.work',
	'apps.about',
	'apps.people',
	'apps.footer',
	'apps.contact',
	'apps.news',
	'apps.social',
	'apps.about',
    'apps.transurlvania',
    'apps.south',
)

INSTALLED_APPS = BASE_APPS + EXTRA_APPS
