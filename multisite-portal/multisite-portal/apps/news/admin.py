from apps.common import utils
from apps.common.admin import ItemSlugAdmin
from apps.news.models import Story, Category, RelatedLink, Friend
from apps.people.models import Person
from django.contrib import admin, messages
from django.core.urlresolvers import reverse
from django.db import models
import settings
from django.contrib import messages
from apps.multilingual.admin import MultilingualInlineAdmin,MultilingualModelAdmin

if settings.ISOBAR_SITE_BOOL is False:
	class CategoryAdmin(MultilingualModelAdmin):
		#ordering = ('title',)
		prepopulated_fields = {'slug': ('title', )}
		
		use_fieldsets = (
			('Content', {
				'fields':('title','title_i18n','slug'),
				}),
		)
		
	admin.site.register(Category, CategoryAdmin)


class RelatedLinkAdmin(MultilingualInlineAdmin):
	model =  RelatedLink
	extra = 0
	
class StoryAdmin(MultilingualModelAdmin):
	#ordering = ('slug',)
	prepopulated_fields = {'slug': ('title', )}
	#list_display_links = ('title', 'publish_date')
	inlines = [RelatedLinkAdmin]

	readonly_fields = ('country', 'posting_agency',)
	
	# site specific functionality
	if settings.ISOBAR_SITE_BOOL:
		list_display = ('title', 'sticky', 'active', 'publish_date')
		#fields_to_exclude = ('subclass','external_db_id','order','publish_to_external', 'category',)
		#fields_to_readonly = ('country', 'posting_agency',)
		use_fieldsets = (
				('Content', {
					'fields':('active','title','title_i18n','slug','author',
							'sticky','image','publish_date','publish_to_external',
							'body','country','posting_agency'),
					}),
		)
	else:
		#list_display = ('title', 'category', 'sticky', 'active', 'publish_date')
		#fields_to_exclude = ('subclass','external_db_id','order','created_by')
		#fields_to_readonly = ('country', 'posting_agency',)
	#exclude = (fields_to_exclude)
	#readonly_fields = (fields_to_readonly)
	
		use_fieldsets = (
				('Content', {
					'fields':('active','title','title_i18n','slug','author','category',
							'sticky','image','show_homepage_thumbnail','homepage_image','publish_date','publish_to_external',
							'body','country','posting_agency'),
					}),
		)


	def save_model(self, request, obj, form, change):

		if obj.country == None or obj.country == '':
			obj.country = settings.SITE

		obj.save()

		if settings.ISOBAR_SITE_BOOL == False:
			if form.cleaned_data['publish_to_external'] == True:
				utils.publish_to_external(self, obj, request)

									
	def formfield_for_foreignkey(self, db_field, request, **kwargs):		
		if db_field.name == "category": \
			kwargs["queryset"] = Category.objects.all() \
									.order_by('slug')
		if db_field.name == "author": \
			kwargs["queryset"] = Person.objects.all() \
									.order_by('slug')

		return super(StoryAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Story, StoryAdmin)

class FriendAdmin(admin.ModelAdmin):
	pass
admin.site.register(Friend, FriendAdmin)


