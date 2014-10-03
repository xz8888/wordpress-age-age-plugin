'''
Created on Jun 21, 2011

@author: arthurnn
'''
DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'isobar_ca',
    'USER': 'root',
    'PASSWORD': 'root',
    'HOST': '',
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
LINKED_SITE = 'localhost:8001'


#LANGUAGES = (
#    ('en', 'English'),
#    ('fr', 'French'),
#)