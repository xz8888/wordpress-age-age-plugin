from apps.common.admin import ItemSlugAdmin
from apps.contact.models import Person, Location, Link, Map
from django.contrib import admin
from django.core.urlresolvers import reverse

class MapAdmin(admin.ModelAdmin):
	pass
admin.site.register(Map, MapAdmin)

class PersonAdmin(admin.ModelAdmin):
	pass
admin.site.register(Person, PersonAdmin)

class LocationAdmin(admin.ModelAdmin):
	pass
admin.site.register(Location, LocationAdmin)

class LinkAdmin(admin.ModelAdmin):
	pass
admin.site.register(Link, LinkAdmin)

