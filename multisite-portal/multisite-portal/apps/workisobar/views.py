from apps.workisobar.models import CaseStudy, CaseStudyIndex, ClientsIndex, Clients
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, Http404
from django.core import serializers
from django.utils import simplejson as json
from django import template
from datetime import datetime

template.add_to_builtins('apps.news.templatetags.news')

def index(request, slug = None):
    casestudyindex = None
    casestudies = None  
    pageid = 'work'  
    
    try:
        casestudyindex = CaseStudyIndex.objects.filter(active = True)[0]
    except:
        pass
    
    try:
        casestudies = CaseStudy.objects.filter(active = True).filter(publish_date__lte=datetime.now())
    except:
        pass
    
    return render_to_response('workisobar/templates/case_study_index.html', { 
                                                                             'casestudies': casestudies,
                                                                             'casestudyindex': casestudyindex,
                                                                             'page' : 'casestudies',
                                                                             'pageid':pageid,
            }, context_instance=RequestContext(request)
    )
def index_ajax(request):
    casestudyindex = None
    casestudies = None  
    pageid = 'work'  
    
    try:
        casestudyindex = CaseStudyIndex.objects.filter(active = True)[0]
    except:
        pass
    
    try:
        casestudies = CaseStudy.objects.filter(active = True).filter(publish_date__lte=datetime.now())
    except:
        pass
    
    return render_to_response('workisobar/templates/case_study_list.html', { 
                                                                             'casestudies': casestudies,
                                                                             'casestudyindex': casestudyindex,
                                                                             'page' : 'casestudies',
                                                                             'pageid':pageid,
            }, context_instance=RequestContext(request)
    )

def clients(request):
    casestudyindex = None
    clientindex = None
    clientslist = None
    featuredclientlist = None
    pageid = 'clients'
    
    try:
        casestudyindex = CaseStudyIndex.objects.filter(active = True)[0]
    except:
        pass
        
    try:
        clientindex = ClientsIndex.objects.filter(active = True)[0]
    except:
        pass
    
    try:
        clientslist = Clients.objects.filter(active = True).exclude(featured=True).order_by('client')
        featuredclientlist = Clients.objects.filter(active=True).filter(featured=True).order_by('order')
    except:
        pass
    
    return render_to_response('workisobar/templates/case_study_index.html', { 
                                                                             'clientindex': clientindex,
                                                                             'clientslist': clientslist,
                                                                             'featuredclients': featuredclientlist,
                                                                             'casestudyindex': casestudyindex,
                                                                             'page': 'clients',
                                                                             'pageid': pageid,
            }, context_instance=RequestContext(request)
    )
def clients_ajax(request):
    casestudyindex = None
    clientindex = None
    clientslist = None
    featuredclientlist = None
    pageid = 'clients'
    
    try:
        casestudyindex = CaseStudyIndex.objects.filter(active = True)[0]
    except:
        pass
        
    try:
        clientindex = ClientsIndex.objects.filter(active = True)[0]
    except:
        pass
    
    try:
        clientslist = Clients.objects.filter(active = True).exclude(featured=True).order_by('client')
        featuredclientlist = Clients.objects.filter(active=True).filter(featured=True).order_by('order')
    except:
        pass
    
    return render_to_response('workisobar/templates/clients.html', { 
                                                                             'clientindex': clientindex,
                                                                             'clientslist': clientslist,
                                                                             'featuredclients': featuredclientlist,
                                                                             'casestudyindex': casestudyindex,
                                                                             'pageid': pageid,
            }, context_instance=RequestContext(request)
    )
def clients_json(request):

    clientindex = None
    clientslist = None
    
    
    try:
        clientindex = ClientsIndex.objects.filter(active = True)[0:1]
    except:
        pass
    
    try:
        clientslist = Clients.objects.filter(active = True).order_by('client')
    except:
        pass
    
    
    
    
    clientslistjson = serializers.serialize("json", clientslist, ensure_ascii=False)
    clientindexjson = serializers.serialize("json", clientindex, ensure_ascii=False)
    
    data = {
            'clients':clientslistjson,
            'clientindex': clientindexjson, 
            }
    
    
    
    return HttpResponse(json.dumps(data, ensure_ascii=False), mimetype="application/json")
    
    
    
    
    
