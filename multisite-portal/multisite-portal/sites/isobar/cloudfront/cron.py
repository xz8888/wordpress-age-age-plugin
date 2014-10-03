import setup_django

from boto.cloudfront import CloudFrontConnection
from sites.isobar.cloudfront.models import CacheClearQueue
from datetime import date, timedelta
import settings

def main():
	_clear_old_requests()
	_clear_cache()

def _clear_cache():
	c = CloudFrontConnection(settings.AWS_ACCESS_KEY, settings.AWS_SECRET_KEY)

	distros = CacheClearQueue.objects.get_by_distribution()[0:1000]
	for distro in distros:
		clear_paths = []
		# Always clear the homepage/root of the distro
		clear_paths.append('/')
		for path in distro['paths']:
			clear_paths.append(path.url)

		try:
			c.create_invalidation_request(distro['id'], clear_paths)
			# If no exception was thrown, we can remove the paths
			# that we just asked to be cleared
			for path in distro['paths']:
				path.delete()
		except Exception as e:
			print 'Failed: ', e

def _clear_old_requests():
	# Delete any requests older than two days as there's probably something
	# wrong with them
	one_day_ago = date.today()-timedelta(days=1)
	CacheClearQueue.objects.filter(date__lte=one_day_ago.isoformat()).delete()

if __name__ == "__main__":
	main()