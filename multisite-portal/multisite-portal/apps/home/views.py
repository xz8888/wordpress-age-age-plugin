from apps.home.models import Layout
from apps.people.models import Person
from apps.social.models import Application, TwitterTweet
from apps.contact.models import Location
from apps.footer.models import Phone, Email
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
	person_1 = None
	person_2 = None
	person_3 = None
	layout = None
	casestudy_1 = None
	casestudy_2 = None
	casestudy_3 = None
	casestudy_4 = None
	casestudy_5 = None
	casestudy_6 = None
	news_1 = None
	news_2 = None

	try:	
		people = Person.objects.all().filter(layoutitem_ptr__item_ptr__active=True).order_by('?')[:3]
		if people and people.count >= 3:
			person_1 = people[0]
			person_2 = people[1]
			person_3 = people[2]
	except:
		pass

	try:
		tweet = TwitterTweet.objects.all()
		if tweet.count() > 0:
			tweet = TwitterTweet.objects.all().order_by('-created')[:1][0]
	except:
		pass
	
	try:
		layout = Layout.objects.all()[0]
		
		casestudy_1 = layout.case_study_small_1
		casestudy_2 = layout.case_study_small_2
		casestudy_3 = layout.case_study_small_3
		
		casestudy_4 = layout.case_study_large_1
		casestudy_5 = layout.case_study_large_2	
		casestudy_6 = layout.case_study_large_3
		
		news_1 = layout.news_story_1
		news_2 = layout.news_story_2
	except:
		pass
	
	try:
		Application.objects.all().get(install=Application.TWITTER)
		twitter_installed = True
	except:
		twitter_installed = False

	try:
		locations = Location.objects.all().order_by('order','title')
	except:
		locations = None

	emails = Email.objects.all().order_by('order', 'address')
	phones = Phone.objects.all().order_by('order', 'number')
	
	return render_to_response('home/templates/home.html', {
			'person_1': person_1,
			'person_2': person_2,
			'person_3': person_3,
			'casestudy_1': casestudy_1,
			'casestudy_2': casestudy_2,
			'casestudy_3': casestudy_3,
			'casestudy_4': casestudy_4,
			'casestudy_5': casestudy_5,
			'casestudy_6': casestudy_6,
			'news_1': news_1,
			'news_2': news_2,
			'tweet': tweet,
			'twitter_installed': twitter_installed,
			'locations': locations,
			'emails': emails,
			'phones': phones,
		}, context_instance=RequestContext(request)
	)