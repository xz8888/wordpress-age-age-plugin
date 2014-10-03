# Create your models here.
from apps.common.cache import cache_clear
from apps.common.templatetags import page
from apps.multilingual.translation import TranslationModel
from apps.tinymce import models as tinymce_models
from common.messages import INFO_MESSAGES
from django.core.urlresolvers import reverse
from django.db import models
import settings
import os.path
from django.utils import translation
from south.modelsinspector import add_introspection_rules


add_introspection_rules([], ["^apps\.tinymce\.models\.HTMLField"])


class VideoPromo(models.Model):
    url = models.CharField(max_length=200, blank=True, help_text=(INFO_MESSAGES['url']['text']))
    order =  models.IntegerField(default=999,blank=True,help_text=(INFO_MESSAGES['order']['text']))
        
    class Translation(TranslationModel):
        title = models.CharField(max_length=200,verbose_name="Title",help_text=(INFO_MESSAGES['title_i18n']['text']))
        body = tinymce_models.HTMLField(blank=True)
        link_text = models.CharField(max_length=200, verbose_name="Link Text", blank=True, null=True)
        hero_image = models.FileField(upload_to='img/uploads/video-promo-isobar', help_text=(INFO_MESSAGES['video_promo']['text']))
        video_image = models.FileField(upload_to='img/uploads/video-promo-isobar/', help_text=(INFO_MESSAGES['video_promo']['text']))
        video = models.FileField(upload_to='video/uploads/video-promo-isobar/',blank=True, null=True, help_text=(INFO_MESSAGES['video_promo']['text']))
        
    class Meta:
        verbose_name = 'Video Promo'    
        verbose_name_plural = 'Video Promos'  
        
    def __unicode__(self):
        return os.path.basename(self.video.name)

    def save(self, *args, **kwargs):
            super(VideoPromo, self).save(*args, **kwargs)
            cache_clear(self.get_related_urls(), self.get_cdn_urls())
    
    def get_related_urls(self):
        return [
            settings.MEDIA_URL + str(self.hero_image),
            settings.MEDIA_URL + str(self.video_image),
        ]

    def get_cdn_urls(self):
        return [
            settings.AWS_STATE + '/' + settings.SITE +'/videopromo/'+ str(self.id)+'/'+translation.get_language() +'/hero.mp4',
            settings.AWS_STATE + '/' + settings.SITE +'/videopromo/'+ str(self.id)+'/'+translation.get_language() +'/hero.3gp',
            settings.AWS_STATE + '/' + settings.SITE +'/videopromo/'+ str(self.id)+'/'+translation.get_language() +'/hero.ogg.theora',
            settings.AWS_STATE + '/' + settings.SITE +'/videopromo/'+ str(self.id)+'/'+translation.get_language() +'/hero.webm',
        ]

    def get_streaming_urls(self):
        return [
            settings.AWS_STATE + '/' + settings.SITE +'/videopromo/'+ str(self.id) +'/' +translation.get_language()+ '/hero.mp4'
        ]

    def video_streaming_url(self):
        return 'rtmp://' + settings.CDN_STREAMING_URL + '/cfx/st/mp4:' + settings.AWS_STATE + '/' + settings.SITE +'/videopromo/'+ str(self.id) +'/' +translation.get_language()+ '/hero.mp4'
    
    def video_download_url(self):
        if self.video is None:
            return None
        
        data = {'host':settings.CDN_DOWNLOAD_URL,
            'state':settings.AWS_STATE,
            'site':settings.SITE,
            'id':self.id,
            'lang':translation.get_language()}
        
        return 'http://%(host)s/%(state)s/%(site)s/videopromo/%(id)d/%(lang)s/hero' % data
   
        
