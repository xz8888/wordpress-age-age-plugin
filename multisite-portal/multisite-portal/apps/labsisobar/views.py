from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Partnership, LabsIndex

from models import LabsIndex

def index(request):
    page = None
    partnerships = None
    video = None
    headline = None
    
    try:
        page = LabsIndex.objects.filter(active=True)
        
        if page.count():
            page = page[0:1].get()
            
            if page:
                video = page.featured_video
                headline = page.headline
                title = page.title
                
                try:      
                    partnerships = page.partnerships.all()
                except:
                    pass
    except LabsIndex.DoesNotExist:
        pass
    
    return render_to_response('labsisobar/templates/labs.html', {
                                                                 'partnerships':partnerships,
                                                                 'casestudy':video,
                                                                 'headline':headline,
                                                                 'title':title,
                                                                 },  context_instance=RequestContext(request))
