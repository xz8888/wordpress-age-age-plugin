from common.messages import INFO_MESSAGES
from django.db import models
from apps.common.cache import cache_clear
from django.core.urlresolvers import reverse

# Create your models here.

class Person(models.Model):
	title = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	description = models.CharField(max_length=100)
	telephone = models.CharField(max_length=20, blank=True)
	order =  models.IntegerField(default=999, help_text=(INFO_MESSAGES['order']['text']))

	class Meta:
		verbose_name_plural = 'People'
	
	def __unicode__(self):
		return self.title

	def save(self, *args, **kwargs):
		super(Person, self).save(*args, **kwargs)
		cache_clear(self.get_related_urls())

	def get_related_urls(self):
		return [
			reverse('contact_view'),
		]

class Location(models.Model):
	title = models.CharField(max_length=100)
	address = models.TextField(blank=True)
	latitude = models.CharField(max_length=15, blank=True)
	longitude = models.CharField(max_length=15, blank=True)
	order =  models.IntegerField(default=999, help_text=(INFO_MESSAGES['order']['text']))
	map_image = models.FileField(upload_to='img/uploads/contact/', blank=True) 
	
	def __unicode__(self):
		return self.title
	
	def save(self, *args, **kwargs):
		super(Location, self).save(*args, **kwargs)
		cache_clear(self.get_related_urls())	

	def get_related_urls(self):
		return [
			reverse('contact_view'),
		]

class Link(models.Model):
	title = models.CharField(max_length=200);
	url = models.CharField(max_length=200);
	image = models.FileField(upload_to='img/uploads/contact/')
	order =  models.IntegerField(default=999, help_text=(INFO_MESSAGES['order']['text']))
	
	def __unicode__(self):
		return self.title

	def save(self, *args, **kwargs):
		super(Link, self).save(*args, **kwargs)
		cache_clear(self.get_related_urls())

	def get_related_urls(self):
		return [
			reverse('contact_view'),
		]

class Map(models.Model):
	centre_point_latitude = models.CharField(max_length=15, blank=True)
	centre_point_longitude = models.CharField(max_length=15, blank=True)
	ZOOM_LEVELS = (
		('1', '1'),
		('2', '2'),
		('2', '3'),
		('3', '3'),
		('4', '4'),
		('5', '5'),
		('6', '6'),
		('7', '7'),
		('8', '8'),
		('9', '9'),
		('10', '10'),
		('11', '11'),
		('12', '12'),
		('13', '13'),
		('14', '14'),
	 	('15', '15'),
	)
	zoom_level = models.CharField(max_length=2, choices=ZOOM_LEVELS, default='5')

	def save(self, *args, **kwargs):
		super(Map, self).save(*args, **kwargs)
		cache_clear(self.get_related_urls())

	def get_related_urls(self):
		return [
			reverse('contact_view'),
		]