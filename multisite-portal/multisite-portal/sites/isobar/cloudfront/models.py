from django.db import models

class Distribution(models.Model):
    class Meta:
        managed = False

class CacheClearQueueManager(models.Manager):
	def get_by_distribution(self):
		distributions = self.all().values('distribution_id').distinct()
		clear_distros = []
		for distro in distributions:
			if distro['distribution_id'] != None:
				paths = self.all().filter(distribution_id=distro['distribution_id'])
	
				clear_distros.append({
					'id': distro['distribution_id'],
					'paths': paths,
				})

		return clear_distros

class CacheClearQueue(models.Model):
	distribution_id = models.CharField(max_length=20)
	url = models.CharField(max_length=250)
	date = models.DateTimeField(auto_now_add=True)
	objects = CacheClearQueueManager()

	def __unicode__(self):
		return self.distribution_id + ': ' + self.url