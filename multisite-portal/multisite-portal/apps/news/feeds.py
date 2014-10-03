from django.contrib.syndication.views import Feed
from django.contrib.sites.models import Site


class NewsFeed(Feed):	
	title = str(Site.objects.get_current().name)
	link = '/'
	description = 'The latest stories from ' + title 
	
	def items(self):
		# Import needs to be inside due to dependency issue
		from apps.news.models import Story
	    
		return Story.objects.all() \
			.filter(layoutitem_ptr__item_ptr__active=True) \
			.order_by('-publish_date')[:10]

	def item_title(self, item):
		return item.title

	def item_description(self, item):
		return item.body
	
	def item_pubdate(self, item):
		return item.publish_date