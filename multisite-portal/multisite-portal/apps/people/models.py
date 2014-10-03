
from django.db import models
from apps.common.models import Item
from apps.home.models import LayoutItem
from apps.tinymce import models as tinymce_models
from common.messages import INFO_MESSAGES
from apps.common.cache import cache_clear
from django.core.urlresolvers import reverse
import apps.multilingual
from apps.multilingual.translation import TranslationModel

class Department(Item):
	colour = models.CharField(max_length=7, default='#ff0000')
	slug = models.SlugField(db_index=True, unique=True, verbose_name=('url Slug'), help_text=(INFO_MESSAGES['url_slug']['text']))

	class Translation(TranslationModel):
		title_i18n = models.CharField(max_length=200,blank=True, null=True,verbose_name="Title",help_text=(INFO_MESSAGES['title_i18n']['text']))
		
	def get_total_people(self):
		#return len(Person.objects.all().filter(department=self))
		return Person.objects.all().filter(department=self, layoutitem_ptr__item_ptr__active= True).count()

	def save(self, *args, **kwargs):
		super(Department, self).save(*args, **kwargs)
		cache_clear(self.get_related_urls())

	@models.permalink
	def get_absolute_url(self):
		return ('people_department_view', (), {'slug': self.slug})

	def title_label(self):
		if self.title_i18n:
			return self.title_i18n
		else:
			return self.title

	def get_related_urls(self):
		return [
			self.get_absolute_url(),
			reverse('people_department_page_view', args=[self.slug, 1]),
			reverse('department_ajax_view', args=[self.slug, 1, 1]),
		]

class Person(LayoutItem):	
	slug = models.SlugField(db_index=True, unique=True, verbose_name=('url Slug'), help_text=(INFO_MESSAGES['url_slug']['text']))
	image = models.FileField(upload_to='img/uploads/people/')
	department = models.ForeignKey(Department)
	
	class Translation(apps.multilingual.translation.Translation):
		title_i18n = models.CharField(max_length=200,blank=True, null=True,verbose_name="Title",help_text=(INFO_MESSAGES['title_i18n']['text']))
		body = tinymce_models.HTMLField(blank=True)
		role = models.CharField(max_length=100, blank=True)
		
	class Meta:
		verbose_name_plural = 'People'

	def save(self, *args, **kwargs):
		super(Person, self).save(*args, **kwargs)
		cache_clear(self.get_related_urls())

	@models.permalink
	def get_absolute_url(self):
		return ('person_view', (), {'person': self.slug})

	def get_related_urls(self):
		# Iterate every department and add to the views to be cleared
		# (in case the person was moved to another dept for instance)
		views_to_clear = [
			self.get_absolute_url(),
			reverse('person_ajax_view', args=[self.slug]),
			reverse('people_page_view', args=[1]),
			reverse('people_page_ajax_view', args=[1, 1]),	
		]

		items = Department.objects.all()
		for item in items:
			views_to_clear.append(reverse('people_department_person_view', args=[item.department.slug, item.slug]),)
			views_to_clear.append(reverse('people_department_person_ajax_view', args=[item.department.slug, item.slug]),)
	
		return [
			views_to_clear
		]


	def next_in_department(self):
		items = Person.objects.all().filter( layoutitem_ptr__item_ptr__active= True ) \
									.filter( department=self.department ) \
									.order_by( 'slug' ) \
		
		item = items.filter( slug__gt=self.slug )[:1]		

		if len( item ) is 1:
			return item[0]
		else:
			return items[:1][0]		

	def previous_in_department(self):		
		items = Person.objects.all().filter( layoutitem_ptr__item_ptr__active= True ) \
									.filter( department=self.department ) \
									.order_by( 'slug' ) \
									.reverse()
								 	
		item = items.filter( slug__lt=self.slug )[:1]							 	
				
		if len( item ) is 1:
			return item[0]
		else:
			return items[:1][0]
		
	def next(self):
		items = Person.objects.all().filter( layoutitem_ptr__item_ptr__active= True ) \
									.order_by( 'slug' )
									 	
		item = items.filter( slug__gt=self.slug )[:1]		
		
		if len( item ) is 1:
			return item[0]
		else:
			return items[:1][0]	
				
	def previous(self):
		items = Person.objects.all().filter( layoutitem_ptr__item_ptr__active= True ) \
									.order_by( 'slug' ) \
									.reverse()
									
		item = items.filter( slug__lt=self.slug )[:1]							 	
				
		if len( item ) is 1:
			return item[0]
		else:
			return items[:1][0]		
	
	def title_label(self):
		if self.title_i18n:
			return self.title_i18n
		else:
			return self.title
		
	def __unicode__(self):
		return self.title