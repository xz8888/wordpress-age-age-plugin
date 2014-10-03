from apps.tinymce import models as tinymce_models
from common.messages import INFO_MESSAGES
from django.core.paginator import Paginator
from django.db import models
import settings

class Application(models.Model):

	ANALYTICS = 'Analytics'
	FACEBOOK_SHARE = 'Facebook share'
	POSTEROUS = 'Posterous'
	PROMO_BOX = 'Promo box'
	TWITTER = 'Twitter'
	TWITTER_SHARE = 'Twitter share'
	
	INSTALL = (
		(ANALYTICS, ANALYTICS),
		(FACEBOOK_SHARE, FACEBOOK_SHARE),
		(PROMO_BOX, PROMO_BOX),
		(POSTEROUS, POSTEROUS),
		(TWITTER, TWITTER),
		(TWITTER_SHARE, TWITTER_SHARE),
	)
	
	install = models.CharField(max_length=20, choices=INSTALL, unique=True)
	order =  models.IntegerField(default=999, help_text=(INFO_MESSAGES['order']['text']))
	
	def __unicode__(self):
		return str(self.install)

class Share(models.Model):
	FACEBOOK = 'Facebook'
	TWITTER = 'Twitter'
	
	INSTALL = (
		(FACEBOOK, FACEBOOK),
		(TWITTER, TWITTER),
	)
	 
	install = models.CharField(max_length=20, choices=INSTALL, unique=True)
	order =  models.IntegerField(default=999, help_text=(INFO_MESSAGES['order']['text']))
	
	def __unicode__(self):
		return str(self.install)
	
	class Meta:
		verbose_name_plural = 'Share'
		
class PosterousAccount(models.Model):
	site_uid = models.CharField(max_length=15, blank=True)
	user = models.CharField(max_length=100, blank=True)
	
	def __unicode__(self):
		return str(self.user)

class PosterousPost(models.Model):
	uid = models.CharField(max_length=100, blank=True)
	title = models.CharField(max_length=100, blank=True)
	created = models.DateTimeField()
	url =  models.CharField(max_length=100, blank=True)
	
	def __unicode__(self):
		return str(self.title)
	
class TwitterAccount(models.Model):
	screen_name = models.CharField(max_length=200)	    

	def __unicode__(self):
		return self.screen_name
	
class TwitterTweet(models.Model):
	text = models.CharField(max_length=140)
	created = models.DateTimeField()
	user_id = models.CharField(max_length=25)
	uid = models.CharField(max_length=200, unique=True)
	screen_name = models.CharField(max_length=200)
	
	def __unicode__(self):
		return str(self.id)

class Analytics(models.Model):
	POSITION_TOP = 'Top'
	POSITION_BOTTOM = 'Bottom'
	POSITION_MIDDLE = 'Middle'
	
	POSITIONS = (
		(POSITION_TOP, POSITION_TOP),
		(POSITION_MIDDLE, POSITION_MIDDLE),
		(POSITION_BOTTOM, POSITION_BOTTOM),
	)
	type = models.CharField(max_length=25) 
	position = models.CharField(max_length=20, choices=POSITIONS, unique=True)
	embed = models.TextField()
	
	class Meta:
		verbose_name = 'Analytics'		
		verbose_name_plural = 'Analytics'		
	
	def __unicode__(self):
		return str(self.type)
	
class PromoBox(models.Model):
	title = models.CharField(max_length=100)
	body = tinymce_models.HTMLField()
	url_title = models.CharField(max_length=100)
	url = models.CharField(max_length=200)
	
	def __unicode__(self):
		return str(self.title)
	
	