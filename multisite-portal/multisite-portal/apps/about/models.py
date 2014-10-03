from django.db import models
from apps.tinymce import models as tinymce_models
import settings
from apps.common.cache import cache_clear
from django.core.urlresolvers import reverse
from apps.multilingual.translation import TranslationModel
from django.utils import translation

class About(models.Model):

	class Meta:
		verbose_name = 'About page'
		verbose_name_plural = 'About page'

	def save(self, *args, **kwargs):
		super(About, self).save(*args, **kwargs)
		cache_clear(self.get_related_urls())
		
	class Translation(TranslationModel):
		tagline = tinymce_models.HTMLField(blank=True)
		left_header = models.CharField(max_length=100)
		left_body = tinymce_models.HTMLField(blank=True)
		right_header = models.CharField(max_length=100) 
		right_body = tinymce_models.HTMLField(blank=True)
		video_image = models.FileField(upload_to='img/uploads/about/')
		video = models.FileField(upload_to='video/uploads/about/',blank=True, null=True)
		
	def __unicode__(self):
		return 'About'

	def video_streaming_url(self):
		return 'rtmp://' + settings.CDN_STREAMING_URL + '/cfx/st/mp4:' + settings.AWS_STATE + '/' + settings.SITE +'/about/'+translation.get_language()+'/hero.mp4'

	def video_download_url(self):
		if self.video is None:
			return None
				
		data = {'host':settings.CDN_DOWNLOAD_URL,'state':settings.AWS_STATE,'site':settings.SITE,'lang':translation.get_language()}
		
		return 'http://%(host)s/%(state)s/%(site)s/about/%(lang)s/hero' % data
		
		#return 'http://' + settings.CDN_DOWNLOAD_URL + ('/' + settings.AWS_STATE + '/' + settings.SITE +'/about/'+translation.get_language()+'/hero')

	def get_related_urls(self):
		return [
			self.video_download_url,
			reverse('about_view'),
		]