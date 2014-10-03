import setup_django

from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils import simplejson
from isobar.apps.social.models import PosterousAccount, PosterousPost, TwitterAccount, TwitterTweet
import datetime
import sys
import time
import urllib, urllib2
import tweepy

def main():
	"""Main Function"""
	getTweetsJson()
	getPosterousJson()

def getTweetsJson():	
	TwitterTweet.objects.all().delete()
	
	consumer_key = "p6jM0Qbeb96AGrLAQ46kXg"
	consumer_secret="wfY1pigoQo2Nc10Dh8Dg49JV3DvU7J4DGjky6KEtM"
	access_token="16668237-5h5x0fp0Sc7z4q5yYnr9TWfmQgKxF2Q3O6NChl9xE"
	access_token_secret="RkjhXacXmZ8yDG8WfzwVLVE3nvXOCwFeX0SocRRDNw"

	try:
		accounts = TwitterAccount.objects.all()
		
		for account in accounts:
			twitterUrl = 'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name='+account.screen_name
			auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
			auth.set_access_token(access_token, access_token_secret)

			api = tweepy.API(auth)
			tweets = api.user_timeline(account.screen_name)
			for tweet in tweets[:5]:
				uid = uid=tweet.id_str
				
				try:
					TwitterTweet.objects.get(uid = uid)
				except TwitterTweet.DoesNotExist:
					print(tweet.created_at)
					if(len(tweet.text) > 140):
					   tweet.text = tweet.text[0:136] + "..."
					print(tweet.text)
					#ts = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(tweet.created_at,'%a %b %d %H:%M:%S +0000 %Y'))
					TwitterTweet.objects.create(uid=uid, user_id=tweet.user.id, text=tweet.text, screen_name=tweet.user.screen_name, created=tweet.created_at)
		
	except:
		print "Unexpected error:", sys.exc_info()[0]
		raise
	
def getPosterousJson():
	PosterousPost.objects.all().delete()
	
	try:
		accounts = PosterousAccount.objects.all()
		
		for  account in accounts:
			url_info = urllib2.urlopen('http://posterous.com/api/2/users/' + account.site_uid +'/sites/' + account.user+ '/posts/public')
			
			print ('http://posterous.com/api/2/users/' + account.site_uid +'/sites/' + account.user+ '/posts/public')
			
			if url_info:
				json = simplejson.load(url_info)				
				
				if json:
					posts = json
					
					for post in posts[:5]:
						uid = post['id']

						try:
							PosterousPost.objects.get(uid=uid)
						except PosterousPost.DoesNotExist:
							ts = post['display_date'][:19] + ' GMT'
							ts = datetime.datetime.strptime(ts,'%Y/%m/%d %H:%M:%S %Z')
							PosterousPost.objects.create(uid=uid, title=post['title'], url=post['full_url'], created=ts)
				else:
					print ('getPosterousJson - Error! Getting URL')
						
	except PosterousAccount.DoesNotExist:
		raise Http404

if __name__ == "__main__":
	main()       