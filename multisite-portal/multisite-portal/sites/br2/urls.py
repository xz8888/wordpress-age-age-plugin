from django.conf.urls.defaults import *
from django.contrib import admin
from isobar.urls import urlpatterns

admin.autodiscover()

localpatterns = patterns('contact.views',
	url(r'^contact/', 'index', name='contact_view'),
)

urlpatterns = localpatterns + urlpatterns