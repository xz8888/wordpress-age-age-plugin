from apps.common.cache import cache_clear
from apps.common.templatetags import page
from apps.home.models import LayoutItem
from apps.multilingual.translation import TranslationModel
from apps.tinymce import models as tinymce_models
from common.messages import INFO_MESSAGES
from django.core.urlresolvers import reverse
from django.db import models
from sites.isobar.location.models import Agency
import settings
from django.utils import translation

class CaseStudy(LayoutItem):
	slug = models.SlugField(db_index=True, unique=True, verbose_name=('url Slug'), help_text=(INFO_MESSAGES['url_slug']['text']))
	#created_by = models.ForeignKey(Agency, blank=True, null=True, help_text=(INFO_MESSAGES['created_by']['text']))
	url = models.CharField(max_length=200, blank=True, help_text=(INFO_MESSAGES['url']['text']))
	publish_date = models.DateField(help_text=(INFO_MESSAGES['publish_date']['text']))
	country = models.CharField(max_length=10, blank=True, default=settings.SITE);
	external_db_id = models.IntegerField(default=-1, blank=True, null=True)
	publish_to_external = models.BooleanField(blank=True, help_text=(INFO_MESSAGES['publish_to_external']['text']))
	posting_agency = models.CharField(max_length=200, default=settings.AGENCY_NAME )
	share_url = models.CharField(max_length=200, blank=True)
	
	class Translation(TranslationModel):
		title_i18n = models.CharField(max_length=200,blank=True, null=True,verbose_name="Title",help_text=(INFO_MESSAGES['title_i18n']['text']))
		body = tinymce_models.HTMLField(blank=True)
		
		hero_image = models.FileField(upload_to='img/uploads/case-study/')
		video_image = models.FileField(upload_to='img/uploads/case-study/')
		video = models.FileField(upload_to='video/uploads/case-study/',blank=True, null=True)
		
	class Meta:
		verbose_name = 'Case Study'	
		verbose_name_plural = 'Case Studies'

	def save(self, *args, **kwargs):
		super(CaseStudy, self).save(*args, **kwargs)
		cache_clear(self.get_related_urls(), self.get_cdn_urls())
		
	@models.permalink
	def get_absolute_url(self):
		return ('work_view', (), {'slug': self.slug})
	
	def get_related_urls(self):
		return [
			self.get_absolute_url(),
			settings.MEDIA_URL + str(self.hero_image),
			settings.MEDIA_URL + str(self.video_image),
			reverse('works_view'),
			reverse('work_view_ajax', args=[self.slug]),
		]

	def get_cdn_urls(self):
		return [
			settings.AWS_STATE + '/' + settings.SITE +'/work/'+ str(self.id)+'/'+translation.get_language() +'/hero.mp4',
			settings.AWS_STATE + '/' + settings.SITE +'/work/'+ str(self.id)+'/'+translation.get_language() +'/hero.3gp',
			settings.AWS_STATE + '/' + settings.SITE +'/work/'+ str(self.id)+'/'+translation.get_language() +'/hero.ogg.theora',
			settings.AWS_STATE + '/' + settings.SITE +'/work/'+ str(self.id)+'/'+translation.get_language() +'/hero.webm',
		]

	def get_streaming_urls(self):
		return [
			settings.AWS_STATE + '/' + settings.SITE +'/work/'+ str(self.id) +'/' +translation.get_language()+ '/hero.mp4'
		]

	def video_streaming_url(self):
		return 'rtmp://' + settings.CDN_STREAMING_URL + '/cfx/st/mp4:' + settings.AWS_STATE + '/' + settings.SITE +'/work/'+ str(self.id) +'/' +translation.get_language()+ '/hero.mp4'
	
	def video_download_url(self):
		if self.video is None:
			return None
		
		data = {'host':settings.CDN_DOWNLOAD_URL,
			'state':settings.AWS_STATE,
			'site':settings.SITE,
			'id':self.id,
			'lang':translation.get_language()}
		
		return 'http://%(host)s/%(state)s/%(site)s/work/%(id)d/%(lang)s/hero' % data
		#return 'http://' + settings.CDN_DOWNLOAD_URL + ('/' + settings.AWS_STATE + '/' + settings.SITE +'/work/'+ str(self.id) +'/hero') 
	
	def title_label(self):
		if self.title_i18n:
			return self.title_i18n
		else:
			return self.title
	
	def __unicode__(self):
		return self.slug

class Award(models.Model):
	id = models.AutoField(primary_key=True)
	image = models.FileField(upload_to='img/uploads/awards/', blank=True, null=True, default="")
	date = models.DateField()
	case_study = models.ForeignKey(CaseStudy,related_name='award_case_study')
	description = models.CharField(max_length=200, blank=True, null=True, default="")
	
	class Translation(TranslationModel):
		title = models.CharField(max_length=200)
		description = models.CharField(max_length=200)
		
	def __unicode__(self):
		return self.title