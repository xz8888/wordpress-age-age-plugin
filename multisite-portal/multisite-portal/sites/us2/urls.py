from django.conf.urls.defaults import *
from django.contrib import admin
from isobar.urls import urlpatterns
from isobar.apps.transurlvania.defaults import *
from django.views.generic.simple import direct_to_template
from isobar.apps.work.models import *
from isobar.apps.contact.models import *
from isobar.apps.about.models import *
from isobar.apps.home.models import *
from isobar.apps.people.models import Person as PeoplePerson
from isobar.apps.people.models import Department
from django.contrib.flatpages.models import *

# remove older models in favor of new ones so the old ones don't show up on the admin panel:
# example: work vs workisobar, about vs aboutisobar
admin.site.unregister(About)
admin.site.unregister(CaseStudy)
admin.site.unregister(Person)
admin.site.unregister(Location)
admin.site.unregister(Link)
admin.site.unregister(Map)
admin.site.unregister(Department)
admin.site.unregister(PeoplePerson)
admin.site.unregister(Layout)

admin.site.unregister(FlatPage)

localpatterns = lang_prefixed_patterns('aboutisobar.views',
	url(r'^about/services/$', 'services', name='service_view'),
	url(r'^about/services/ajax/$', 'services_ajax', name='service_ajax'),
	url(r'^about/profiles/$', 'profiles', name='profile_view'),
	url(r'^about/partners/$', 'partners', name='partner_view'),
  url(r'^about/partners/ajax/$', 'partners_ajax', name='partner_ajax'),
  url(r'^about/profiles/ajax/$', 'profiles_ajax', name='profile_ajax'),
	url(r'^about/$', 'profiles', name='profile_view'),
)

localpatterns += lang_prefixed_patterns('workisobar.views',
    url(r'^work/$', 'index', name="work_view"),
    url(r'^work/casestudy/(?P<slug>[a-zA-Z0-9-_]*)/$', 'index', name="specific_work_view"),
    url(r'^work/clients/$', 'clients', name="work_clients_view"),
    url(r'^work/clients/json/$', 'clients_json', name="work_clients_json"),
    url(r'^work/clients/ajax/$', 'clients_ajax', name="work_clients_ajax"),
    url(r'^work/casestudies/ajax/$', 'index_ajax', name="work_ajax"),
)

localpatterns += lang_prefixed_patterns('contactisobar.views',  
    #url(r'^contact/$', 'index_proxy_contact', name='index_contact_proxy'),                      
    #url(r'^contact/(?P<location>[a-zA-Z-_,. ]+)/$', 'index_proxy_contact', name='index_contact_proxy'),
    url(r'^contact/$', 'index', name='index'),
    url(r'^contact/(?P<location>[a-zA-Z-_,. ]+)/$', 'index', name='index'),
    url(r'^contact_test/(?P<location>[a-zA-Z-_,. ]+)/$', 'index', name='index_contact_test'),
	url(r'^contact_data/(?P<location>[a-zA-Z-_,. ]+)/$', 'contact_data', name='contact_data_view'),  
    url(r'^common_contact/$', 'common_contact', name='common_contact_view'),
    url(r'^shelf_proxy/$', 'shelf_proxy_contact', name='shelf_contact_proxy'),
    url(r'^shelf_contact/$', 'shelf_contact', name='shelf_contact_view'),
	url(r'^office_contact/(?P<name>[a-zA-Z-_,. ]+)/$', 'office_contact', name='office_contact_view'),
)

localpatterns += lang_prefixed_patterns('labsisobar.views',
    url(r'^nowlab/$', 'index', name='labs_view'),
)

localpatterns += patterns('homeisobar.views',
    url(r'^$', 'index', name="home_view"),
)

localpatterns += lang_prefixed_patterns('homeisobar.views',
	url(r'^$', 'index', name="home_view"),
)

localpatterns += lang_prefixed_patterns('careerisobar.views',
	url(r'^career/jobs/job/(?P<job>[a-zA-Z0-9-_]+)/$', 'job_item', name='job_item'),
	url(r'^career/jobs/(?P<region>[a-zA-Z-_,. ]+)/$', 'job_list_json', name='job_list_json'),
	
	#url(r'^career/$', 'job_view', name="job_view"),
	url(r'^career/jobs/$', 'job_list', name="job_list"),
)
urlpatterns = localpatterns + urlpatterns
