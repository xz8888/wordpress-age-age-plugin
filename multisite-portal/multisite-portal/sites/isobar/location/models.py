from django.db import models
from apps.tinymce import models as tinymce_models
from common.messages import INFO_MESSAGES
from apps.common.cache import cache_clear
from django.core.urlresolvers import reverse

class Country(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(db_index=True, unique=True, verbose_name=('url Slug'), help_text=(INFO_MESSAGES['url_slug']['text']))
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
	latitude = models.CharField(max_length=15, blank=True)
	longitude = models.CharField(max_length=15, blank=True)
	
	class Meta:
		verbose_name_plural = 'Countries'

	def save(self, *args, **kwargs):
		super(Country, self).save(*args, **kwargs)
		cache_clear(self.get_related_urls())

	@models.permalink
	def get_absolute_url(self):
		return ('country_view', (), {
				'country': self.slug,})

	def get_related_urls(self):
		return [
			self.get_absolute_url(),
		]

	def __unicode__(self):
		return self.title

class Agency(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(db_index=True, unique=True, verbose_name=('url Slug'), help_text=(INFO_MESSAGES['url_slug']['text']))
	city = models.CharField(max_length=200)
	country = models.ForeignKey(Country)
	latitude = models.CharField(max_length=15)
	longitude = models.CharField(max_length=15)
	website = models.CharField(max_length=100, blank=True)
	image = models.FileField(upload_to='img/location/agency/', blank=True)
	body = tinymce_models.HTMLField(blank=True)
	address = models.TextField(blank=True)
	
	class Meta:
		verbose_name_plural = 'Agencies'

	def save(self, *args, **kwargs):
		super(Agency, self).save(*args, **kwargs)
		cache_clear(self.get_related_urls())

	@models.permalink
	def get_absolute_url(self):
		return ('agency_view', (), {
				'country': self.country.slug,
				'agency': self.slug,})

	def get_related_urls(self):
		return [
			self.get_absolute_url(),
			reverse('agency_view_ajax', args=[self.country.slug, self.slug]),
		]

	def __unicode__(self):
		return self.title

class Contact(models.Model):
	agency = models.ForeignKey(Agency, related_name='contact_agency')
	name = models.CharField(max_length=200, blank=True)
	position = models.CharField(max_length=50, blank=True)
	email = models.EmailField(max_length=200, blank=True)
	number = models.CharField(max_length=20, blank=True)

	def save(self, *args, **kwargs):
		super(Contact, self).save(*args, **kwargs)
		cache_clear(self.get_related_urls())

	def get_related_urls(self):
		return [
			reverse('contact_view'),
		]

	def __unicode__(self):
		return self.name