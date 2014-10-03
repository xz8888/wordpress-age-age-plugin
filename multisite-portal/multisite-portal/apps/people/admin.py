from apps.common.admin import ItemSlugAdmin
from apps.people.models import Department, Person
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.db import models
from apps.people.models import Person, Department
from urlparse import urlparse

class DepartmentAdmin(ItemSlugAdmin):
	#ordering = ('title',)
	#ordering = ('slug',)
	
	#prepopulated_fields = {'slug': ('title', )}
	
	use_fieldsets = (
			('Content', {
				'fields':('active','title','title_i18n','slug','order','colour'),
				}),
	)
	
	def save_model(self, request, obj, form, change):
		page_updates = []
		obj.save()

class PersonAdmin(ItemSlugAdmin):	
	list_display = ('sorted_title','title_i18n', 'department','role')
	ordering = ('slug',)
	use_fieldsets = (
				('Content', {
					'fields':('active','title','title_i18n','order','slug','image','department','body','role'),
					}),
		)

	def sorted_title(self, request):
		return request
	
	sorted_title.admin_order_field = 'common_item.title'

	def save_model(self, request, obj, form, change):
		page_updates = []				
		obj.save()
		
	def formfield_for_foreignkey(self, db_field, request, **kwargs):		
		if db_field.name == "department": \
			kwargs["queryset"] = Department.objects.all() \
									.order_by('item_ptr__title')

		return super(PersonAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Department, DepartmentAdmin)    
admin.site.register(Person, PersonAdmin)    
