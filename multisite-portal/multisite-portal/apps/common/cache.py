import settings
import urllib2
import urllib

def cache_clear(page_urls = None, cdn_urls = None):
	# If key is blank assume we're running in development so don't try
	# to clear any caches
	if settings.AWS_CLOUDFRONT_KEY == '':
		return False

	urls_with_key = []
	if not page_urls is None:
		for url in page_urls:
			urls_with_key.append({
				'distro_id': settings.AWS_CLOUDFRONT_KEY,
				'url': url
			})

	if not cdn_urls is None:
		for url in cdn_urls:
			urls_with_key.append({
				'distro_id': settings.AWS_CLOUDFRONT_CDN_KEY,
				'url': url
			})

	if urls_with_key.count > 0:
		for url in urls_with_key:
			url['key'] = settings.POST_AUTH
			data = urllib.urlencode(url)
			req = urllib2.Request('http://' + settings.LINKED_SITE + '/admin/cloudfront/schedule-cache-clear/', data)

			# If the connection breaks, at least allow the system
			# to continue functioning
			try:
				urllib2.urlopen(req)
			except:
				pass