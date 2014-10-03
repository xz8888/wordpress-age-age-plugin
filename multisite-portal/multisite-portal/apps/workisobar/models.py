# Create your models here.
from apps.common.cache import cache_clear
from apps.video_promo.models import VideoPromo 
from apps.common.templatetags import page
from apps.common.models import Item
from apps.multilingual.translation import TranslationModel
from apps.tinymce import models as tinymce_models
from common.messages import INFO_MESSAGES
from django.core.urlresolvers import reverse
from django.db import models
from sites.isobar.location.models import Agency
import settings
from django.utils import translation
from south.modelsinspector import add_introspection_rules


add_introspection_rules([], ["^apps\.tinymce\.models\.HTMLField"])


class Award(models.Model):
    casestudy = models.ForeignKey('CaseStudy', related_name='awards', blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    
    class Translation(TranslationModel):
        title = models.CharField(max_length=200, blank=True)
        description = models.TextField()
        
    def __unicode__(self):
        return self.title
    
class ClientQuote(models.Model):
    casestudy = models.ForeignKey('CaseStudy', related_name='client_quotes', blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    
    class Translation(TranslationModel):
        title = models.CharField(max_length=200, blank=True)
        description = models.TextField(blank=True, null=True)
        
    def __unicode__(self):
        return self.title    

class PressRelease(models.Model):
    casestudy = models.ForeignKey('CaseStudy', related_name='press_releases', blank=True, null=True)
    date = models.DateField()
    url = models.CharField(max_length=200, blank=True, null=True)
    
    class Translation(TranslationModel):
        title = models.CharField(max_length=200)
        description = models.TextField(blank=True, null=True)
        
    def __unicode__(self):
        return self.title  

class ClientsIndex(models.Model):
    active =  models.BooleanField(default=True)
    featured_video = models.ForeignKey('video_promo.VideoPromo', blank=True, null=True, verbose_name=('Featured Video'))
    
    class Translation(TranslationModel):
        title = models.CharField(max_length=200,verbose_name="Title",help_text=(INFO_MESSAGES['title_i18n']['text']))
        headline = models.CharField(max_length=512, blank=True, null=True, verbose_name=('Headline'), help_text=(INFO_MESSAGES['headline']['text']))   
        meta_description = models.TextField(blank=True, null=True, verbose_name="Metadata Description")
        
    class Meta:
        verbose_name = 'Clients Landing Page'    
        verbose_name_plural = 'Client Landing Pages'
        
        
    def __unicode__(self):
        return self.title


class Clients(models.Model):
    active =  models.BooleanField(default=True)
    featured =  models.BooleanField(default=True)
    url = models.CharField(max_length=200, blank=True, help_text=(INFO_MESSAGES['url']['text']))
    logo = models.FileField(upload_to='img/uploads/client-isobar/', blank=True, default='Enter a logo', help_text=(INFO_MESSAGES['client_logo']['text']))
    client = models.CharField(max_length=200,verbose_name="Client Name")
    order = models.IntegerField(default=999, help_text=(INFO_MESSAGES['order']['text']))
    
    class Translation(TranslationModel):
        description = models.TextField(blank=True, null=True, verbose_name="Description")
        
    class Meta:
        verbose_name = 'Client'    
        verbose_name_plural = 'Clients'
        
    def __unicode__(self):
        return self.client

class SlideShowItem(models.Model):
    image_id = models.CharField(max_length=200,verbose_name="Image ID",help_text=(INFO_MESSAGES['title_i18n']['text']))
    image = models.FileField(upload_to='img/uploads/case-study-isobar/homepage', blank=True, null=True, help_text=(INFO_MESSAGES['video_promo']['text']))
    order =  models.IntegerField(default=999,blank=True,help_text=(INFO_MESSAGES['order']['text']))
    casestudy = models.ForeignKey('CaseStudy', related_name='client_slide', blank=True, null=True)

    class Translation(TranslationModel):
        title = models.CharField(max_length=200, blank=True, null=True, help_text=(INFO_MESSAGES['not_displayed']['text']))
        description = models.TextField(blank=True, null=True, help_text=(INFO_MESSAGES['not_displayed']['text']))
    
    class Meta:
        verbose_name = 'Slide Show Item'    
        verbose_name_plural = 'Slide Show Item'  
        ordering = ['order'] 
        
    def __unicode__(self):
        return self.image_id  

class CaseStudy(models.Model):
    slug = models.SlugField(db_index=True, unique=True, verbose_name=('url Slug'), help_text=(INFO_MESSAGES['url_slug']['text']))
    title_id = models.CharField(max_length=200,verbose_name="Title ID",help_text=(INFO_MESSAGES['title_i18n']['text']))
    publish_date = models.DateField(help_text=(INFO_MESSAGES['publish_date']['text']))
    active =  models.BooleanField(default=True)
    url = models.CharField(max_length=200, blank=True, help_text=(INFO_MESSAGES['url']['text']))
    order =  models.IntegerField(default=999,blank=True,help_text=(INFO_MESSAGES['order']['text']))
    client = models.ForeignKey(Clients, blank=True, null=True)
    logo_sprite = models.FileField(upload_to='img/uploads/case-study-isobar/logo/', blank=True, null=True, help_text=(INFO_MESSAGES['thumbnail_grid']['text']))
    homepage_image = models.FileField(upload_to='img/uploads/case-study-isobar/homepage', blank=True, null=True, help_text=(INFO_MESSAGES['homepage_image']['text']))
        
    class Translation(TranslationModel):
        title = models.CharField(max_length=200,verbose_name="Title",help_text=(INFO_MESSAGES['title_i18n']['text']))
        body = tinymce_models.HTMLField(blank=True)
        hero_image = models.FileField(upload_to='img/uploads/case-study-isobar/hero/', help_text=(INFO_MESSAGES['hero_image']['text']))
        video_image = models.FileField(upload_to='img/uploads/case-study-isobar/video/', help_text=(INFO_MESSAGES['video_promo']['text']))
        video = models.FileField(upload_to='video/uploads/case-study-isobar/video/',blank=True, null=True, help_text=(INFO_MESSAGES['video_promo']['text']))
        
    class Meta:
        verbose_name = 'Case Study'    
        verbose_name_plural = 'Case Studies'  
        ordering = ['order'] 
        
    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
            super(CaseStudy, self).save(*args, **kwargs)
            cache_clear(self.get_related_urls(), self.get_cdn_urls())
    
    @models.permalink
    def get_absolute_url(self):
        return ('specific_work_view', (), {
                'slug': self.slug})
    
    def get_related_urls(self):
        return [
            settings.MEDIA_URL + str(self.hero_image),
            settings.MEDIA_URL + str(self.video_image),
            reverse('works_view'),
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
   
        
class CaseStudyIndex(models.Model):
    active =  models.BooleanField(default=True)
    featured_video = models.ForeignKey('video_promo.VideoPromo', blank=True, null=True, verbose_name=('Featured Video'))
    
    
    class Translation(TranslationModel):
        title = models.CharField(max_length=200,verbose_name="Title",help_text=(INFO_MESSAGES['title_i18n']['text']))
        headline = models.CharField(max_length=512, blank=True, null=True, verbose_name=('Headline'), help_text=(INFO_MESSAGES['headline']['text']))   
        meta_description = models.TextField(blank=True, null=True, verbose_name="Metadata Description")
        
    class Meta:
        verbose_name = 'Case study landing page'    
        verbose_name_plural = 'Case study landing pages'
        
        
    def __unicode__(self):
        return self.title


