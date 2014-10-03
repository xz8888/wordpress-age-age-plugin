from apps.home.models import LayoutItem
from apps.people.models import Person
from apps.tinymce import models as tinymce_models
from common.messages import INFO_MESSAGES
from django.db import models
import settings
from sites.isobar.location.models import Agency
from apps.common.cache import cache_clear
from django.core.urlresolvers import reverse
import apps.multilingual
from apps.multilingual.translation import TranslationModel

class Category(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(db_index=True, unique=True, verbose_name=('url Slug'), help_text=(INFO_MESSAGES['url_slug']['text']))

	class Translation(TranslationModel):
		title_i18n = models.CharField(max_length=200,blank=True, null=True,verbose_name="Title",help_text=(INFO_MESSAGES['title_i18n']['text']))
	
	class Meta:
		verbose_name = 'Category'		
		verbose_name_plural = 'Categories'	
	
	def category_total(self):
		return len(Story.objects.all() \
								.filter( layoutitem_ptr__item_ptr__active=True ) \
								.filter(category=self))

	def overall_total(self):
		return len(Story.objects.all() \
								.filter( layoutitem_ptr__item_ptr__active=True ))
	
	def save(self, *args, **kwargs):
		super(Category, self).save(*args, **kwargs)
		cache_clear(self.get_related_urls())

	@models.permalink
	def get_absolute_url(self):
		return ('news_category_view', (), {
				'slug': self.slug}) 

	def get_related_urls(self):
		return [
			self.get_absolute_url(),
		]

	def title_label(self):
		if self.title_i18n:
			return self.title_i18n
		else:
			return self.title
		
	def __unicode__(self):
		return self.title

class Story(LayoutItem):
	slug = models.SlugField(db_index=True, unique=True, verbose_name=('url Slug'), help_text=(INFO_MESSAGES['url_slug']['text']))
	created_by = models.ForeignKey(Agency, blank=True, null=True, help_text=(INFO_MESSAGES['created_by']['text']))
	author = models.ForeignKey(Person, blank=True, null=True)
	category = models.ForeignKey(Category, blank=True, null=True)
	sticky = models.BooleanField(default=False, help_text=(INFO_MESSAGES['sticky']['text']))
	publish_date = models.DateTimeField(help_text=(INFO_MESSAGES['publish_date']['text']))
	country = models.CharField(max_length=10, blank=True, default=settings.SITE);
	external_db_id = models.IntegerField(default=-1, blank=True, null=True)
	publish_to_external = models.BooleanField(blank=True, help_text=(INFO_MESSAGES['publish_to_external']['text']))
	posting_agency = models.CharField(max_length=200, default=settings.AGENCY_NAME )
	show_homepage_thumbnail =  models.BooleanField(default=True, verbose_name="Show thumbnail when featured on homepage?")

	class Translation(apps.multilingual.translation.Translation):
		title_i18n = models.CharField(max_length=200,blank=True, null=True,verbose_name="Title",help_text=(INFO_MESSAGES['title_i18n']['text']))
		image = models.FileField(upload_to='img/uploads/news/', blank=True)
		homepage_image = models.FileField(upload_to='img/uploads/news/homepage', blank=True, null=True)
		body = tinymce_models.HTMLField(blank=True)
	
	class Meta:
		verbose_name = 'Story'		
		verbose_name_plural = 'Stories'	

	def save(self, *args, **kwargs):
		super(Story, self).save(*args, **kwargs)
		cache_clear(self.get_related_urls())

	@models.permalink
	def get_absolute_url(self):
		return ('news_story_view', (), {
				'year': self.publish_date.year,
				'month': self.publish_date.month,
				'day': self.publish_date.day,
				'slug': self.slug})

	def get_related_urls(self):
		return [
			self.get_absolute_url(),
			reverse('news_story_view', args=[self.publish_date.year, self.publish_date.month, self.publish_date.day, self.slug]),
			reverse('news_archive_day_view', args=[self.publish_date.year, self.publish_date.month, self.publish_date.day]),
			reverse('news_archive_month_view', args=[self.publish_date.year, self.publish_date.month]),
			reverse('news_archive_year_view', args=[self.publish_date.year]),
			reverse('news_archive_view'),
			#reverse('news_category_page_view', args=[self.category.slug, 1]),
			#reverse('news_category_view', args=[self.category.slug]),
			reverse('news_page_view', args=[1]),
			reverse('news_page_ajax_view', args=[1]),
			reverse('news_archive_view'),
			reverse('news_view'),
			reverse('news_rss'),
		]

	def title_label(self):
		if self.title_i18n:
			return self.title_i18n
		else:
			return self.title
		
	def __unicode__(self):
		return self.title
	
class RelatedLink(models.Model):
	story = models.ForeignKey(Story, related_name='related_link_story')
	url = models.CharField(max_length=200)

	class Translation(apps.multilingual.translation.Translation):
		description = models.CharField(max_length=200)
		
	def save(self, *args, **kwargs):
		super(RelatedLink, self).save(*args, **kwargs)
		cache_clear(self.get_related_urls())

	def get_related_urls(self):
		return [
			reverse('news_story_view', args=[self.story.publish_date.year, self.story.publish_date.month, self.story.publish_date.day, self.story.slug]),
			reverse('news_archive_day_view', args=[self.story.publish_date.year, self.story.publish_date.month, self.story.publish_date.day]),
			reverse('news_archive_month_view', args=[self.story.publish_date.year, self.story.publish_date.month]),
			reverse('news_archive_year_view', args=[self.story.publish_date.year]),
			reverse('news_archive_view'),
			#reverse('news_category_page_view', args=[self.story.category.slug, 1]),
			#reverse('news_category_view', args=[self.story.category.slug]),
			reverse('news_page_view', args=[1]),
			reverse('news_page_ajax_view', args=[1]),
			reverse('news_archive_view'),
			reverse('news_view'),
			reverse('news_rss'),
		]

	def __unicode__(self):
		return self.url
	
class Friend(models.Model):	
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	url = models.CharField(max_length=200) 

	def save(self, *args, **kwargs):
		super(Friend, self).save(*args, **kwargs)
		cache_clear(self.get_related_urls())

	def get_related_urls(self):
		views_to_clear = [
			reverse('news_view'),
		]
		
		items = Story.objects.all() \
			.filter(layoutitem_ptr__item_ptr__active = True)

		#for item in items:
		#	views_to_clear.append(reverse('news_category_page_view', args=[item.category.slug, 1]),)
		#	views_to_clear.append(reverse('news_category_view', args=[item.category.slug]),)

		return [
			views_to_clear
		]

	def __unicode__(self):
		return self.title