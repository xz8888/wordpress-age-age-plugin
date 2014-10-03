from django.conf.urls.defaults import *
from django.contrib import admin
from isobar.urls import urlpatterns
from isobar.apps.transurlvania.defaults import *
from django.views.generic.simple import direct_to_template
from isobar.apps.work.models import CaseStudy as OldCaseStudy
from isobar.apps.contact.models import Person as ContactPerson
from isobar.apps.contact.models import Map as ContactMap
from isobar.apps.contact.models import Location as ContactLocation
from isobar.apps.contact.models import Link as ContactLink
from isobar.apps.about.models import *
from isobar.apps.home.models import *
from isobar.apps.people.models import Person as PeoplePerson
from isobar.apps.people.models import Department
from django.contrib.flatpages.models import *
from isobar.apps.footer.models import *
from isobar.apps.news.models import *
from isobar.apps.social.models import *


# remove older models in favor of new ones so the old ones don't show up on the admin panel:
# example: work vs workisobar, about vs aboutisobar
admin.site.unregister(About)
admin.site.unregister(OldCaseStudy)
admin.site.unregister(ContactPerson)
admin.site.unregister(ContactLocation)
admin.site.unregister(ContactLink)
admin.site.unregister(ContactMap)
admin.site.unregister(Department)
admin.site.unregister(PeoplePerson)
admin.site.unregister(Layout)

admin.site.unregister(FlatPage)

admin.site.unregister(Footer)
admin.site.unregister(Story)
admin.site.unregister(Friend)
admin.site.unregister(Category)
admin.site.unregister(Application)
admin.site.unregister(Share)


localpatterns = lang_prefixed_patterns('contactisobar.views',                        
    url(r'^contact/(?P<location>[a-zA-Z-_,. ]+)/$', 'index', name='contact_view'),
	url(r'^contact_data/(?P<location>[a-zA-Z-_,. ]+)/$', 'contact_data', name='contact_data_view'),  
    url(r'^common_contact/$', 'common_contact', name='common_contact_view'),
    url(r'^shelf_contact/$', 'shelf_contact', name='shelf_contact_view'),
	url(r'^office_contact/(?P<name>[a-zA-Z-_,. ]+)/$', 'office_contact', name='office_contact_view'),
)

urlpatterns = localpatterns + urlpatterns