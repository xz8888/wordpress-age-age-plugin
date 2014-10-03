from django.contrib import admin
from django.core.urlresolvers import reverse
from django.db import models
from sites.isobar.location.models import Country, Agency, Contact

class CountryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title', )}
	ordering = ('slug',)
	
admin.site.register(Country, CountryAdmin)


class ContactInline(admin.StackedInline):
	model =  Contact
	extra = 0

class AgencyAdmin(admin.ModelAdmin):
	inlines = [ContactInline]
	prepopulated_fields = {'slug': ('title', )}
	ordering = ('title',)
	list_display = ('title','city')
	
admin.site.register(Agency, AgencyAdmin)