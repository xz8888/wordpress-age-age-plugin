from django.conf.urls.defaults import *
from apps.transurlvania.defaults import *
from django.contrib import admin
from isobar.urls import urlpatterns

admin.autodiscover()

localpatterns = lang_prefixed_patterns('',
	url(r'^contact/(?P<country>[a-zA-Z0-9-]+)/(?P<agency>[a-zA-Z0-9-]+)/$', 'sites.isobar.location.views.agency', name='agency_view'),
	url(r'^contact/(?P<country>[a-zA-Z0-9-]+)/(?P<agency>[a-zA-Z0-9-]+).ajax$', 'sites.isobar.location.views.agency', {'ajax': True}, name='agency_view_ajax'),
	url(r'^contact/(?P<country>[a-zA-Z0-9-]+)/$', 'sites.isobar.location.views.country', name='country_view'),
	url(r'^contact/$', 'sites.isobar.location.views.index', name="contact_view"),
)

localpatterns += patterns('',
	url(r'^admin/cloudfront/distribution/$', 'sites.isobar.cloudfront.views.distribution', name="cloudfront_distribution_view"),
	url(r'^admin/cloudfront/distribution/add/', 'sites.isobar.cloudfront.views.distribution_add', name="cloudfront_distribution_add_view"),
	url(r'^admin/cloudfront/schedule-cache-clear/', 'sites.isobar.cloudfront.views.schedule_cache_clear', name="cloudfront_schedule_cache_clear"),
	
	url(r'^receive-casestudy/$', 'apps.work.views.recieve_casestudy', name='receive_casestudy_view'),
	url(r'^receive-newsstory/$', 'apps.news.views.recieve_newsstory', name='receive_newsstory_view'),
	url(r'^receive-relatedlinks/$', 'apps.news.views.recieve_relatedlinks', name='recieve_relatedlinks_view'),
)

urlpatterns = localpatterns + urlpatterns