# Create your models here.
from apps.common.cache import cache_clear
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


class Home(models.Model):
    featured_case_studies = models.ManyToManyField('workisobar.CaseStudy', blank=True, null=True)
    featured_news_1 = models.ForeignKey('news.Story', verbose_name='Featured News Story 1', related_name='featured_story_1')
    active =  models.BooleanField(default=True)
    
    class Translation(TranslationModel):
        title = models.CharField(max_length=200)
        headline = models.CharField(max_length=512)
        meta_description = models.TextField()
        
    def __unicode__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Homepage'
        verbose_name_plural = 'Homepages'
