from apps.common.models import Item
from apps.home.models import Layout
from apps.news.models import Story
from apps.work.models import CaseStudy
from django import forms
from django.contrib import admin


class LayoutAdmin(admin.ModelAdmin):
	
	def formfield_for_foreignkey(self, db_field, request, **kwargs):		
		if db_field.name == "case_study_large_1" \
		or db_field.name == "case_study_large_2" \
		or db_field.name == "case_study_large_3" \
		or db_field.name == "case_study_small_1" \
		or db_field.name == "case_study_small_2" \
		or db_field.name == "case_study_small_3":
			kwargs["queryset"] = CaseStudy.objects.all() \
									.filter(layoutitem_ptr__item_ptr__active=True) \
									.order_by('layoutitem_ptr__item_ptr__title')
			
		if db_field.name == "news_story_1" \
		or db_field.name == "news_story_2":		
			kwargs["queryset"] = Story.objects.all() \
									.filter(layoutitem_ptr__item_ptr__active=True) \
									.order_by('layoutitem_ptr__item_ptr__title')
			
		return super(LayoutAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
	
admin.site.register(Layout, LayoutAdmin)