from django.contrib import admin
from models import Distribution

class DistributionAdmin(admin.ModelAdmin):
	name='Distribution'

admin.site.register(Distribution, DistributionAdmin)