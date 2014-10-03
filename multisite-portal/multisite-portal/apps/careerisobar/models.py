from django.db import models
from common.messages import INFO_MESSAGES
from apps.tinymce import models as tinymce_models
from apps.multilingual.translation import TranslationModel
from django.utils import translation

# Create your models here.
class Career(models.Model):

    active = models.BooleanField(default=False)
    
    class Translation(TranslationModel):
        title = models.CharField(max_length=200, verbose_name="Title", help_text=(INFO_MESSAGES['title_id']['text']))
        meta_description = models.TextField()
        headline = models.CharField(max_length=250, verbose_name="Headline")
        content = tinymce_models.HTMLField(blank=True)
        
    class Meta:
        verbose_name = "Career Isobar Page"
        verbose_name_plural = "Career Isobar Pages"

    def __unicode__(self):
        return self.title