from careerisobar.jobvite.JobViteReciever import *
from careerisobar.jobvite.JobViteParser import *
from careerisobar.models import Career
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, Http404
from django.utils import simplejson as json
import HTMLParser

# Create your views here. 

def job_view(request):
    
    careerindex = None
    
    try:
        careerindex = Career.objects.filter(active = True)[0]
    except:
        pass
    
    return render_to_response('careerisobar/templates/careers_index.html', 
                              {
                               'careerindex' : careerindex,
                               },
                              context_instance=RequestContext(request))

def job_list(request):
    
    careerindex = None
    
    try:
        careerindex = Career.objects.filter(active = True)[0]
    except:
        pass

    return render_to_response('careerisobar/templates/careers_list.html', 
                              {
                               'careerindex' : careerindex,
                               },
                              context_instance=RequestContext(request))

def job_item(request, job):
    jvr = JobViteReciever('http://www.jobvite.com/CompanyJobs/Xml.aspx?c=qwX9Vfwh')
    jvp = JobViteParser()

    jobs = jvp.parseXML(jvr.getData())
    
    data = jvp.getJobDescription(jobs, job)
    
    return HttpResponse(data, mimetype="text/html")

def job_list_json(request, region):
    jvr = JobViteReciever('http://www.jobvite.com/CompanyJobs/Xml.aspx?c=qwX9Vfwh')
    jvp = JobViteParser()

    jobs = jvp.parseXML(jvr.getData())
    
    unescaped_region = HTMLParser.HTMLParser().unescape(region)
    data = jvp.getTitleByRegion(jobs, unescaped_region)
    
    return HttpResponse(json.dumps(data), mimetype="application/json")
