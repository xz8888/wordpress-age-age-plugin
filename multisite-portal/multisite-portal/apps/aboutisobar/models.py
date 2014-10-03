from django.db import models
from apps.tinymce import models as tinymce_models
from common.messages import INFO_MESSAGES
from apps.multilingual.translation import TranslationModel
from django.utils import translation
from apps.multilingual.manager import MultilingualManager
from south.modelsinspector import add_introspection_rules
from apps.video_promo.models import VideoPromo
from django.utils.html import strip_tags

add_introspection_rules([], ["^apps\.tinymce\.models\.HTMLField"])

# Create your models here.

class Profile(models.Model):
   	name = models.CharField(max_length=100)
   	image = models.FileField(upload_to='img/uploads/aboutisobar/', help_text=(INFO_MESSAGES['profile_image']['text']))
   	order = models.IntegerField(default=999, help_text=(INFO_MESSAGES['order']['text']))
   	
	class Translation(TranslationModel):   	
   		description = tinymce_models.HTMLField(blank=True, max_length=1070)
   		
   	def __unicode__(self):
   	    return self.name
    
   	class Meta:
   	    ordering = ['order']
   	    verbose_name = "Profile"
   	    verbose_name_plural = "Profiles"
   	    

class Partner(models.Model):
	title = models.CharField(max_length=500, verbose_name="Partner Title")
	description = models.CharField(max_length=270, default='Default')
	image = models.FileField(upload_to='img/uploads/aboutisobar/', help_text=(INFO_MESSAGES['partner_image']['text']))

   	class Meta:
   	    ordering = ['title']
   	    verbose_name = "Partner"
   	    verbose_name_plural = "Partners"

	def __unicode__(self):
		return self.title


class Service(models.Model):
    order = models.IntegerField(default=999, help_text=(INFO_MESSAGES['order']['text']))
    
    class Translation(TranslationModel):
		title = models.CharField(max_length=200,verbose_name="Title-id", help_text=(INFO_MESSAGES['title_id']['text']))
		short_description = tinymce_models.HTMLField(blank=True)
		long_description = tinymce_models.HTMLField(blank=True)
			
    def __unicode__(self):
        return unicode(self.title)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Service"
        verbose_name_plural = "Services"


class About(models.Model):

	title = models.CharField(max_length=200, verbose_name="Title-id", help_text=(INFO_MESSAGES['title_id']['text']))
	featured_slogan = models.CharField(max_length=500, verbose_name="Featured Slogan")
	active = models.BooleanField(default=False)
	profiles_text = tinymce_models.HTMLField(blank=True)
	profiles = models.ManyToManyField(Profile, related_name='profile_about')
	partners = models.ManyToManyField(Partner, related_name='partner_about')
	services = models.ManyToManyField(Service, related_name='service_about')
	featured_video = models.ForeignKey(VideoPromo, blank=True, null=True, verbose_name=('Featured Video'))

	class Translation(TranslationModel):
		meta_description = models.TextField()
	
	class Meta:
		ordering = ['title']
		verbose_name = "About Isobar Page"
		verbose_name_plural = "About Isobar Pages"

   	def __unicode__(self):
   	    return self.title
