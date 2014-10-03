from apps.homeisobar.models import Home
from apps.home.models import Layout
from apps.news.models import Story
from apps.social.models import Application, TwitterTweet
from apps.contact.models import Location
from apps.footer.models import Phone, Email
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
from apps.common import feedparser
import re

def index(request):
	homepage = None
	tweet = None
	twitter_installed = None
	blog_1 = None
	blog_2 = None
	page_id = 'home'
	f_title = None
	f_link = None
	f_image_html = None
	latest_news = None

	try:
		homepage = Home.objects.filter(active = True)[0]
		latest_news = Story.objects.all().order_by('-publish_date')[0]
	except:
		pass
	
	try:
		tweet = TwitterTweet.objects.all()
		if tweet.count() > 0:
			tweet = TwitterTweet.objects.all().order_by('-created')[:1][0]
	except:
		pass
	
	try:
		Application.objects.all().get(install=Application.TWITTER)
		twitter_installed = True
	except:
		twitter_installed = False

	try:
		f = feedparser.parse(settings.FACEBOOK_RSS)
		for entry in f.entries:
			if entry.title:
				f_title = entry.title
				f_link = entry.link
				regex = re.compile("<img.*?alt=\"([^\"]*)\".*?src=\"([^\"]*)\".*?>")
				r = regex.search(entry.content[0].value)
				f_image_html = r.group(0)
				break
	except:
		pass

	try:
		d = feedparser.parse(settings.BLOG_RSS)
		blog_1 = {
				'title' : d.entries[0].title,
				'url':d.entries[0].link,
				'description':d.entries[0].description,
		}
		blog_2 = {
				'title' : d.entries[1].title,
				'url':d.entries[1].link,
				'description':d.entries[1].description,
				'image': d.entries[1]
		}
	except:
		pass

	return render_to_response('homeisobar/templates/home.html', { 
																 'facebook_title':f_title,
																 'facebook_link':f_link,
																 'facebook_img_html':f_image_html,
																 'homepage': homepage,
																 'latest_news': latest_news,
																 'tweet':tweet,
																 'blog_1':blog_1,
																 'blog_2':blog_2,
																 'twitter_installed': twitter_installed,
																 'page_id':page_id,
			}, context_instance=RequestContext(request)
	)
