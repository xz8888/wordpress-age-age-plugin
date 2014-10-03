from apps.common.models import Item
from django.db import models
import apps.multilingual
from apps.tinymce import models as tinymce_models
from common.messages import INFO_MESSAGES
from apps.common.cache import cache_clear
from django.core.urlresolvers import reverse
from south.modelsinspector import add_introspection_rules


add_introspection_rules([], ["^apps\.tinymce\.models\.HTMLField"])

class Job(Item):
	contact = models.CharField(max_length=200)
	slug = models.SlugField(db_index=True, unique=True, verbose_name=('url Slug'), help_text=(INFO_MESSAGES['url_slug']['text']))
	specification = models.FileField(upload_to='pdf/uploads/', blank=True)
	url = models.CharField(max_length=200, blank=True,verbose_name="External Job url", help_text=(INFO_MESSAGES['url']['text']))
	
	class Translation(apps.multilingual.translation.Translation):
		title_i18n = models.CharField(max_length=200,blank=True, null=True,verbose_name="Title",help_text=(INFO_MESSAGES['title_i18n']['text']))
		body = tinymce_models.HTMLField(blank=True)
	
	@models.permalink
	def get_absolute_url(self):
		return ('job_view', (), {'slug': self.slug})
	
	def __unicode__(self):
		return self.title
		
	def title_label(self):
		if self.title_i18n:
			return self.title_i18n
		else:
			return self.title


	def save(self, *args, **kwargs):
		super(Job, self).save(*args, **kwargs)
		cache_clear(self.get_related_urls())

	def get_related_urls(self):
		return [
			self.get_absolute_url(),
			reverse('jobs_view'),
		]