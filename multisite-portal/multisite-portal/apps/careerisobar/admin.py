from django.contrib import admin
from apps.careerisobar.models import Career
from apps.multilingual.admin import MultilingualModelAdmin

class CareerAdmin(MultilingualModelAdmin):
    pass

admin.site.register(Career, CareerAdmin)