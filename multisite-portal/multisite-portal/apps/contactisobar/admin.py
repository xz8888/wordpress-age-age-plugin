from django.contrib import admin
from apps.contactisobar.models import Region, Country, Person, Office
from apps.multilingual.admin import MultilingualModelAdmin, MultilingualInlineAdmin

class OfficeInline(MultilingualInlineAdmin):
    model = Office
    extra = 0 

class RegionAdmin(MultilingualModelAdmin):
    list_display = ('name',)
    
    filter_horizontal = ('countries', 'people')
    
class CountryAdmin(MultilingualModelAdmin):
    filter_horizontal = ('offices',)
    pass

class PersonAdmin(MultilingualModelAdmin):
    pass

class OfficeAdmin(MultilingualModelAdmin):
    use_fieldsets = (
       ('Office Info', {'fields' : ('name', 'city',),}),
       ('Office Location', {'fields' : ('address_line1', 'address_line2',),}),
       ('Office GPS', {'fields' : ('latitude', 'longitude',),}),
       ('Office Contact', {'fields' : ('email', 'url', 'telephone',),}),
       ('Contact Page', {'fields' : ('show',),}),
    )

admin.site.register(Region, RegionAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Office, OfficeAdmin)
