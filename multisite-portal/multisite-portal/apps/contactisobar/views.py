# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Region, Country, Person, Office
from django.http import HttpResponse, Http404
from django.core import serializers
from django.utils import simplejson as json
from django.conf import settings
import urllib, urllib2

def index(request, location):
    
    regions = None
    active_region = None
    global_contact = None
    map_selector = None
    agencies = None
    
    region_country = {}
    country_office = {}
        
    try:
        regions = Region.objects.filter(name=location)
        active_region = regions[0]
    except:
        pass
    
    try:
        agencies = Office.objects.all()
    except:
        pass
    
    try:
        regions = Region.objects.all().exclude(name='global')
    except:
        pass
    
    for region in regions: 
        for country in region.countries.all():
            region_country.setdefault(region.id, []).append(country)
            for office in country.offices.all():
                country_office.setdefault(country.id, []).append(office)

    
    if location == 'global':
        global_contact = active_region.countries.all()[0].offices.all()[0]
    
    map_selector = "".join(item[0].lower() for item in location.split())   
    
    return render_to_response('contactisobar/templates/contact.html', { 
                                                                     'rc':region_country,
                                                                     'co':country_office,
                                                                     'agencies':agencies,
                                                                     'regions':regions,
                                                                     'region':active_region,
                                                                     'global_contact':global_contact,
                                                                     'map':map_selector,
                                                                     },  context_instance=RequestContext(request))

def contact_data(request, location):
    
    regions = None
    active_region = None
    global_contact = None
    map_selector = None
    agencies = None
    
    region_country = {}
    country_office = {}    

    try:
        regions = Region.objects.filter(name=location)
        active_region = regions[0]
    except:
        pass
    
    try:
        agencies = Office.objects.all()
    except:
        pass
    
    try:
        regions = Region.objects.all().exclude(name='global')
    except:
        pass
    
    for region in regions:
        for country in region.countries.all():
            region_country.setdefault(region.id, []).append(country)
            for office in country.offices.all():
                country_office.setdefault(country.id, []).append(office)

    
    if location == 'global':
        global_contact = active_region.countries.all()[0].offices.all()[0]
    
    map_selector = "".join(item[0].lower() for item in location.split())   
    
    return render_to_response('contactisobar/templates/contact_data.html', { 
                                                                     'rc':region_country,
                                                                     'co':country_office,
                                                                     'agencies':agencies,
                                                                     'regions':regions,
                                                                     'region':active_region,
                                                                     'global_contact':global_contact,
                                                                     'map':map_selector,
                                                                     },  context_instance=RequestContext(request))


def common_contact(request):
    
    regions = None
    
    try:
        regions = Region.objects.all().exclude(name='global')
    except:
        pass
    
    return render_to_response('contactisobar/templates/common_contact.html', {
                                                                     'regions':regions, 
                                                                     },  context_instance=RequestContext(request))
    
def shelf_contact(request):
    
    regions = None
    
    try:
        regions = Region.objects.all().exclude(name='global')
    except:
        pass
    
    return render_to_response('contactisobar/templates/shelf_contact.html', {
                                                                     'regions':regions, 
                                                                     },  context_instance=RequestContext(request))

def shelf_proxy_contact(request):

    url = urllib.quote(settings.LANGUAGE_CODE + '/shelf_contact/')
    data = urllib2.urlopen(settings.CONTACT_BASEURL + '/' + url).read()

    return HttpResponse(data, mimetype="text/html")

def index_proxy_contact(request, location=None):

    if location:
        url = urllib.quote(settings.LANGUAGE_CODE + '/contact_data/' + location + '/')
        contact_data = urllib2.urlopen(settings.CONTACT_BASEURL + '/' + url).read()
    else:
        url = urllib.quote(settings.LANGUAGE_CODE + '/contact_data/' + settings.CONTACT_DEFAULT + '/')
        contact_data = urllib2.urlopen(settings.CONTACT_BASEURL + '/' + url).read()
    
    return render_to_response('contactisobar/templates/contact_proxy.html', { 
                                                                        'contact_data':contact_data,
                                                                        }, context_instance=RequestContext(request)) 

def office_contact(request, name):
    
    offices = None
    
    try:
        offices = Office.objects.filter(name=name)
    except:
        pass
    
    return render_to_response('contactisobar/templates/office_contact.html', {
                                                                     'offices':offices, 
                                                                     },  context_instance=RequestContext(request))
