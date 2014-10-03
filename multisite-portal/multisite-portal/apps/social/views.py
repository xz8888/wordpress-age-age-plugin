from apps.social.models import Share
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

def share(request):
	url = request.GET.get('url')
	text = request.GET.get('text')
	items = Share.objects.all().order_by('order')
		
	return render_to_response('share.ajax', {'url':url,
											 'text':text, 
											 'items': items},
											  context_instance=RequestContext(request))