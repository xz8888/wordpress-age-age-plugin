from django.http import HttpResponse
from django.shortcuts import render_to_response,get_object_or_404
from django.template import RequestContext
from apps.jobs.models import Job

def index(request):
	
	try: 
		jobs = Job.objects.all().order_by('item_ptr__order').filter(item_ptr__active=True)
	except Job.DoesNotExist:
		raise Http404
	
	return render_to_response('jobs/templates/jobs.html', {'jobs':jobs}, context_instance=RequestContext(request))


def job(request, slug):
	
	try:
		job = Job.objects.all().filter(item_ptr__active=True).get(slug=slug)
	except Job.DoesNotExist:
		raise Http404
	
	return render_to_response('jobs/templates/job.html', {'job':job}, context_instance=RequestContext(request))