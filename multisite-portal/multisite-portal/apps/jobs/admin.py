from apps.common.admin import ItemSlugAdmin
from apps.jobs.models import Job
from django.contrib import admin
from django.core.urlresolvers import reverse


class JobAdmin(ItemSlugAdmin):
		
	#ordering = ('slug',)
	use_fieldsets = (
		('Content', {
			'fields':('active','title','title_i18n','order','contact','slug','specification','url','body'),
		}),
	)
	def save_model(self, request, obj, form, change):
#			page_updates = []
#			page_updates.append(str(reverse('job_view', kwargs={'slug':obj.slug})))
#			page_updates.append(str(reverse('jobs_view')))
#			print page_updates			
		obj.save()
			

admin.site.register(Job, JobAdmin)
