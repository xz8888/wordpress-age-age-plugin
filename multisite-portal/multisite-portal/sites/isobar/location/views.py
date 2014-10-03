from apps.contact.models import Person, Location
from django.shortcuts import render_to_response
from django.template import RequestContext
from sites.isobar.location.models import Country, Agency
from django.http import Http404

def index(request):	
	countries = Country.objects.all().order_by('title')
	agencies = Agency.objects.all().order_by('title')
	
	people = Person.objects.all().order_by('order')
	locations = Location.objects.all().order_by('title')

	print _getCountryAgencyTotals(countries, agencies)
	
	return render_to_response('location/templates/agencies.html', {
				'agencies': agencies,
				'countries': countries,
				'people': people,
				'locations': locations,
				'country_agency_counts': _getCountryAgencyTotals(countries, agencies)
		}, context_instance=RequestContext(request)
	)

def country(request, country):
	try: 
		agencies = Agency.objects.all().filter(country__slug=country).order_by('title')
	except Agency.DoesNotExist:
		raise Http404
	
	return render_to_response('location/templates/country.html', {
				'agencies': agencies
		}, context_instance=RequestContext(request)
	)

def agency(request, country, agency, ajax=False):
	try: 
		agency = Agency.objects.all().get(slug=agency)
	except Agency.DoesNotExist:
		raise Http404

	parent_template = 'base.html'
	if ajax:
		parent_template = 'blank.html'

	return render_to_response('location/templates/agency.html', {
			'agency': agency,
			'ajax': ajax,
			'parent_template': parent_template,
		}, context_instance=RequestContext(request)
	)

def _getCountryAgencyTotals(countries, agencies):
	totals = dict()

	for country in countries:
		i = 0
		for agency in agencies:
			if agency.country == country:
				i = i+1

		totals[country.slug] = i

	return totals