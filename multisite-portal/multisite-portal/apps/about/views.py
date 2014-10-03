from django.shortcuts import render_to_response
from django.template import RequestContext
from models import About

def index(request):
	about = None

	try:
		about = About.objects.all()
	except About.DoesNotExist:
		pass

	if about.count() > 0:
		about = about[0]
	
	return render_to_response('about/templates/about.html', {
			'about': about,
		}, context_instance=RequestContext(request)
	)