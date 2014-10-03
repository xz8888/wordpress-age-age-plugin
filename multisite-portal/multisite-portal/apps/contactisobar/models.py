from django.db import models
from apps.tinymce import models as tinymce_models
from common.messages import INFO_MESSAGES
from apps.multilingual.translation import TranslationModel
from django.utils import translation
from apps.multilingual.manager import MultilingualManager
from south.modelsinspector import add_introspection_rules


add_introspection_rules([], ["^apps\.tinymce\.models\.HTMLField"])

# Create your models here.
class Office(models.Model):
    
    name = models.CharField(max_length=100, verbose_name='Office Name')
    city = models.CharField(max_length=100, verbose_name='City Location')
    address_line1 = models.CharField(max_length=250, verbose_name='Address Line 1', blank=True)
    address_line2 = models.CharField(max_length=250, verbose_name='Address Line 2', blank=True)
    latitude = models.CharField(max_length=15, blank=True)
    longitude = models.CharField(max_length=15, blank=True)
    telephone = models.CharField(max_length=40, verbose_name='Telephone', blank=True)
    url = models.CharField(max_length=100, verbose_name='URL', blank=True)
    email = models.CharField(max_length=250, verbose_name='E-mail', blank=True)
    show = models.BooleanField(default = True, verbose_name='Show on Contact Page')
    
    def get_absolute_url(self):
        if self.url and self.url.startswith('http'):
            return self.url
        
        return 'http://%s' % self.url
    
    class Meta:
        ordering = ['city']
        verbose_name = "Office"
        verbose_name_plural = "Offices"

    def __unicode__(self):
        return u'%s @ %s %s' % (self.name, self.latitude, self.longitude)
    

class Country(models.Model):
    
    name = models.CharField(max_length=100)
    offices = models.ManyToManyField(Office, related_name='offices')
    order =  models.IntegerField(default=999)
    
    
    class Meta:
        ordering = ['order','name']
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    def __unicode__(self):
        return self.name
    
class Person(models.Model):
    
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True)
    description = models.CharField(max_length=100, blank=True)
    telephone = models.CharField(max_length=20, blank=True)
    order =  models.IntegerField(default=999, help_text=(INFO_MESSAGES['order_people']['text']))
    
    class Meta:
        ordering = ['order']
        verbose_name = "Person"
        verbose_name_plural = "People"

    def __unicode__(self):
        return self.title

class Region(models.Model):
    
    name = models.CharField(max_length=100, verbose_name='Region Name')
    people = models.ManyToManyField(Person, max_length=200, verbose_name='people')  
    countries = models.ManyToManyField(Country, related_name='countries')
    order =  models.IntegerField(default=999)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Region"
        verbose_name_plural = "Regions"

    def __unicode__(self):
        return self.name
