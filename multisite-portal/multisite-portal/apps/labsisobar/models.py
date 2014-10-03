from django.db import models
import os
from apps.tinymce import models as tinymce_models
from common.messages import INFO_MESSAGES
from apps.multilingual.translation import TranslationModel
from django.utils import translation
from apps.multilingual.manager import MultilingualManager
from south.modelsinspector import add_introspection_rules
from apps.video_promo.models import VideoPromo

add_introspection_rules([], ["^apps\.tinymce\.models\.HTMLField"])

# Create your models here.
class Partnership(models.Model):
    url = models.URLField(max_length=200, verbose_name='Link to Project', blank=True)
    image = models.FileField(upload_to='img/uploads/labsisobar/', blank=True, null=True, help_text=(INFO_MESSAGES['labs_image']['text']))
    remove_image = models.BooleanField('Remove Image')
    
    class Translation(TranslationModel):
        title = models.CharField(max_length=200,verbose_name="Title",help_text=(INFO_MESSAGES['title_i18n']['text']))
        description = tinymce_models.HTMLField(blank=True)
    
    class Meta:
        verbose_name = "Labs Content Entry"
        verbose_name_plural = "Labs Content Entries"
    
    def __unicode__(self):
        return self.title
    
    def save(self):
        if self.remove_image and self.image != "":
            if os.path.exists(self.image.path):
                os.remove(self.image.path)
            self.image = ""
            self.remove_image = False
            
        super(Partnership, self).save()

class LabsIndex(models.Model):
    active =  models.BooleanField(default=True)
    featured_video = models.ForeignKey('video_promo.VideoPromo', blank=True, null=True, verbose_name=('Featured Video'))
    partnerships = models.ManyToManyField(Partnership, related_name='partnership')
    
    class Translation(TranslationModel):
        title = models.CharField(max_length=200,verbose_name="Title",help_text=(INFO_MESSAGES['title_i18n']['text']))
        headline = models.CharField(max_length=512, blank=True, null=True, verbose_name=('Headline'), help_text=(INFO_MESSAGES['headline']['text']))   
        meta_description = models.TextField(blank=True, null=True, verbose_name="Metadata Description")
        
    class Meta:
        verbose_name = 'Labs Page'    
        verbose_name_plural = 'Labs Pages'
        
    def __unicode__(self):
        return self.title
