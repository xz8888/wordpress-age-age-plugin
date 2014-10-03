# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import About, Profile, Partner, Service

def profiles(request):
    page = None
    profiles_text = None
    profiles = None
    video = None
    services = None
    slogan = None
    partners = None
    
    try:
        page = About.objects.filter(active=True)
        
        if page.count():
            page = page[0:1].get()
            slogan = page.featured_slogan
            
            try:      
                profiles = page.profiles.all()
            except:
                pass
            try:
                services = page.services.all()
            except:
                pass
            try:
                partners = page.partners.all()
            except:
                pass
            try:
                profiles_text = page.profiles_text
            except:
                pass
            
            try:
                video = page.featured_video
            except:
                pass
    except About.DoesNotExist:
        pass
    
    return render_to_response('aboutisobar/templates/aboutisobar.html', {
                                                                     'profile_text':profiles_text, 
                                                                     'services':services,
                                                                     'partners':partners,
                                                                     'profiles':profiles, 
                                                                     'page':'profiles',
                                                                     'slogan':slogan,
                                                                     'casestudy':video,
                                                                     },  context_instance=RequestContext(request))
def profiles_ajax(request):
    page = None
    profiles_text = None
    items = None
    profiles = None
    video = None
    services = None
    slogan = None
    
    try:
        page = About.objects.filter(active=True)
        
        if page.count():
            page = page[0:1].get()
            slogan = page.featured_slogan
            
            try:      
                profiles = page.profiles.all()
            except:
                pass
            try:
                services = page.services.all()
            except:
                pass
            try:
                partners = page.partners.all()
            except:
                pass
            try:
                profiles_text = page.profiles_text
            except:
                pass
            
            try:
                video = page.featured_video
            except:
                pass
    except About.DoesNotExist:
        pass
    
    return render_to_response('aboutisobar/templates/profiles.html', {
                                                                     'profile_text':profiles_text, 
                                                                     'items':items,
                                                                     'services':services,
                                                                     'partners':partners,
                                                                     'profiles':profiles, 
                                                                     'page':'profiles',
                                                                     'slogan':slogan,
                                                                     'casestudy':video,
                                                                     },  context_instance=RequestContext(request))
def services(request):
    page = None
    services = None
    video = None
    
    try:
        page = About.objects.filter(active=True)
        
        if page.count():
            page = page[0:1].get()
            slogan = page.featured_slogan
            
            try:
                services = page.services.all()
            except:
                pass
            
            try:
                video = page.featured_video
            except:
                pass
    except About.DoesNotExist:
        pass
    

    return render_to_response('aboutisobar/templates/aboutisobar.html', {
                                                                     'services':services, 
                                                                     'page':'services',
                                                                     'slogan':slogan,
                                                                     'casestudy':video,
                                                                     },  context_instance=RequestContext(request))
def services_ajax(request):
    page = None
    services = None
    video = None
    
    try:
        page = About.objects.filter(active=True)
        
        if page.count():
            page = page[0:1].get()
            slogan = page.featured_slogan
            
            try:
                services = page.services.all()
            except:
                pass
            
            try:
                video = page.featured_video
            except:
                pass
    except About.DoesNotExist:
        pass
    

    return render_to_response('aboutisobar/templates/services.html', {
                                                                     'services':services, 
                                                                     'page':'services',
                                                                     'slogan':slogan,
                                                                     'casestudy':video,
                                                                     },  context_instance=RequestContext(request))
                                                                     
                                                                         
def partners(request):
    page = None
    partners = None
    video = None
    
    try:
        page = About.objects.filter(active=True)
    
        if page.count():
            page = page[0:1].get()
            slogan = page.featured_slogan

            try:
                partners = page.partners.all()
            except:
                pass
            
            try:
                video = page.featured_video
            except:
                pass
    except About.DoesNotExist:
        pass
        
    return render_to_response('aboutisobar/templates/aboutisobar.html', {
                                                                     'partners':partners, 
                                                                     'page':'partners',
                                                                     'slogan':slogan,
                                                                     'casestudy':video,
                                                                     },  context_instance=RequestContext(request))
                                                                     
def partners_ajax(request):
    page = None
    partners = None
    video = None
    
    try:
        page = About.objects.filter(active=True)
    
        if page.count():
            page = page[0:1].get()
            slogan = page.featured_slogan

            try:
                partners = page.partners.all()
            except:
                pass
            
            try:
                video = page.featured_video
            except:
                pass
    except About.DoesNotExist:
        pass
        
    return render_to_response('aboutisobar/templates/partners.html', {
                                                                     'partners':partners, 
                                                                     'page':'partners',
                                                                     'slogan':slogan,
                                                                     'casestudy':video,
                                                                     },  context_instance=RequestContext(request))
