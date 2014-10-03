from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from isobar.urls import urlpatterns

admin.autodiscover()

contactpatterns = patterns('isobar.apps.contact.views',
	url(r'^contact/', 'index', name='contact_view'),
)

urlpatterns += contactpatterns