from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.contact.models import Person, Link, Location, Map
from apps.footer.models import Phone, Email
from apps.footer.models import Footer, Social, Promo

def index(request):
	people = None
	links = None
	locations = None
	emails = None 
	phones = None
	footer = None
	promo = None
	
	try:
		map = Map.objects.all()[:1][0]
	except:
		map = None

	try:
		footer = Footer.objects.all()[:1][0]
		social = Social.objects.filter(footer=footer)

		try:
			promo = Promo.objects.get(footer=footer)
		except:
			promo = None
	except:
		social = None
		
	people = Person.objects.all().order_by('order','title')
	links = Link.objects.all().order_by('order','title')
	locations = Location.objects.all().order_by('order','title')
	emails = Email.objects.all().order_by('order', 'address')
	phones = Phone.objects.all().order_by('order', 'number')

	return render_to_response('contact/templates/contact.html', {
						'people': people,
						'links': links,
						'locations': locations,
						'emails': emails,
						'phones': phones,
						'map': map,
						'social': social,
						'promo': promo,
		}, context_instance=RequestContext(request)
	)