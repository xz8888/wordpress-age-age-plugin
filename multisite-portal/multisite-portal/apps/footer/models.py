from django.db import models
from apps.common.models import Item
from apps.multilingual.translation import TranslationModel
from apps.tinymce import models as tinymce_models
from common.messages import INFO_MESSAGES

class Footer(Item):
	def __unicode__(self):
		return self.title

class Social(Item):
	link = models.CharField(max_length=200);
	image = models.FileField(upload_to='img/uploads/social/')
	footer = models.ForeignKey(Footer, related_name='social_footer')

	class Meta:
		ordering = ['item_ptr__order']
		verbose_name = 'Social link'
		verbose_name_plural = 'Social links'

	def __unicode__(self):
		return self.title
	
class Phone(models.Model):
	number = models.CharField(max_length=100)
	order = models.IntegerField(default=999, help_text=(INFO_MESSAGES['order']['text']))
	footer = models.ForeignKey(Footer, related_name='phone_footer')

	class Meta:
		ordering = ['order']
		verbose_name = 'Phone number'
		verbose_name_plural = 'Phone numbers'

#	def __unicode__(self):
#		return self.number

class Email(models.Model):
	address = models.CharField(max_length=200);
	order = models.IntegerField(default=999, help_text=(INFO_MESSAGES['order']['text']))
	footer = models.ForeignKey(Footer, related_name='email_footer')
	
	class Meta:
		ordering = ['order']
		verbose_name = 'Email address'
		verbose_name_plural = 'Email addresses'

	def __unicode__(self):
		return self.address

class Promo(models.Model):
	image = models.FileField(upload_to='img/uploads/social/')
	footer = models.ForeignKey(Footer, related_name='promo_footer')

	class Translation(TranslationModel):
		content = tinymce_models.HTMLField(blank=True)

#	def __unicode__(self):
#		return self.content