from django.db import models
from django.db.models.related import RelatedObject
from common.messages import INFO_MESSAGES

class Item(models.Model):
	id = models.AutoField(primary_key=True)
	subclass = models.CharField(blank=True, max_length=100)
	active =  models.BooleanField(default=True)
	title = models.CharField(max_length=200,verbose_name="Title-id", help_text=(INFO_MESSAGES['title_id']['text']))
	order =  models.IntegerField(default=999, help_text=(INFO_MESSAGES['order']['text']))
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

 
	def save(self, *args, **kwargs):
		if not self.id:
		    parent = self._meta.parents.keys()[0]
		    subclasses = parent._meta.get_all_related_objects()
		    for klass in subclasses:
			if isinstance(klass, RelatedObject) and klass.field.primary_key and klass.opts == self._meta:
			    self.subclass = klass.get_accessor_name()
			    break

		return super(Item, self).save(*args, **kwargs)
    
	def get_object(self):
		try:
			if self.subclass and self._meta.get_field_by_name(self.subclass)[0].opts != self._meta:
				return getattr(self, self.subclass)

		except FieldDoesNotExist:
			pass

		return self

	def __unicode__(self):
		return self.title