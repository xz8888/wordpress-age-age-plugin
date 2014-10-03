from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from isobar.urls import urlpatterns
from django.views.generic.simple import direct_to_template

admin.autodiscover()

localpatterns = patterns('contact.views',
	url(r'^contact/', 'index', name='contact_view'),
	
	url(r'^holiday2011/$', direct_to_template, {'template': 'holiday2011/index.html'} ),
)

urlpatterns = localpatterns + urlpatterns


#if settings.DEV_MODE:
urlpatterns += patterns('',
	(r'^holiday2011/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT+'us_holiday2011/'}),
)