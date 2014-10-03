from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.cache import never_cache
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from boto.cloudfront import CloudFrontConnection
from boto.cloudfront.origin import CustomOrigin
from forms import DistributionForm
from models import CacheClearQueue
import settings

def distribution(request):
	c = CloudFrontConnection(settings.AWS_ACCESS_KEY, settings.AWS_SECRET_KEY)
	query = c.get_all_distributions()
	
	distros = []
	for result in query:
		distro = result.get_distribution()
		distros.append({
			'id': distro.id,
			'active': distro.config.enabled,
			'comment': distro.config.comment,
			'domain': distro.domain_name,
			'origin': distro.config.origin.dns_name,
		})

	return render_to_response('distribution.html', {
			'distributions': distros,
		}, context_instance=RequestContext(request)
	)
distribution = staff_member_required(never_cache(distribution))

def distribution_add(request):
	if request.method == 'POST':
		form = DistributionForm(request.POST)
		if form.is_valid():
			c = CloudFrontConnection(settings.AWS_ACCESS_KEY, settings.AWS_SECRET_KEY)
			origin = CustomOrigin(form.cleaned_data['origin_domain'], origin_protocol_policy='http-only')
			c.create_distribution(origin=origin, enabled=True, comment=form.cleaned_data['comment'])

			return HttpResponseRedirect(reverse('cloudfront_distribution_view'))
	else:
		form = DistributionForm()


	return render_to_response('distribution_add.html', {
			'form': form,
		}, context_instance=RequestContext(request)
	)
distribution_add = staff_member_required(never_cache(distribution_add))

@csrf_exempt
def schedule_cache_clear(request):
	if request.POST.get('key', '') != settings.POST_AUTH:
		return HttpResponse('denied')

	try:
		clear_obj = CacheClearQueue.objects.get(
					url=request.POST.get('url', ''),
					distribution_id=request.POST.get('distro_id', '')
		)
	except CacheClearQueue.DoesNotExist:
		clear_obj = CacheClearQueue()
		clear_obj.url = request.POST.get('url', '')
		clear_obj.distribution_id = request.POST.get('distro_id', '')
		clear_obj.save()

	return HttpResponse('ok')