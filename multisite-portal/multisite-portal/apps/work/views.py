from apps.work.models import CaseStudy
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, Http404

import sys
from isobar.apps.work.models import *
from isobar.apps.work.forms import *
from django.utils import simplejson as json
import settings
from django.views.decorators.csrf import csrf_exempt

from apps.common import utils

def index(request):
	try:    
		casestudies =  CaseStudy.objects.all() \
			.filter(layoutitem_ptr__item_ptr__active=True) \
			.order_by('-publish_date')
	except CaseStudy.DoesNotExist:
		raise Http404

	return render_to_response('work/templates/case_studies.html', { 
				'casestudies': casestudies,
			}, context_instance=RequestContext(request)
	)

def casestudy(request, slug, ajax=False):
	try:
		casestudy = CaseStudy.objects.all() \
			.filter(layoutitem_ptr__item_ptr__active=True) \
			.select_related() \
			.get(slug=slug)
	except CaseStudy.DoesNotExist:
		raise Http404

	parent_template = 'base.html'
	if ajax:
		parent_template = 'blank.html'

	return render_to_response('work/templates/case_study.html', { 
				'casestudy': casestudy,
				'ajax': ajax,
				'parent_template': parent_template,
			}, context_instance=RequestContext(request)
	)

@csrf_exempt
def recieve_casestudy(request):
	form = CaseStudyForm()
	if request.method == 'POST': # If the form has been submitted...
		this_response = {}

		if request.POST['key'] == settings.POST_AUTH:
			try:
				# Look on the external db for this record
				# We have to store the created_by in a variable as dJango seems to lose it once we get inside form.is_valid()?
#				print 'existing_casestudy_record - started'
				existing_record = CaseStudy.objects.get(layoutitem_ptr__item_ptr__id = int(request.POST['external_db_id']))
				created_by = existing_record.created_by
				already_exists = True
				# Update form POST with any files that have also been posted
				# http://www.stereoplex.com/blog/django-newforms-file-upload
				form = CaseStudyForm(request.POST, request.FILES, instance=existing_record)
			except CaseStudy.DoesNotExist:
				already_exists = False
				form = CaseStudyForm(request.POST, request.FILES)
				
#			print 'already_exists='
#			print already_exists

			if form.is_valid(): # All validation rules pass
#				print 'form.is_valid - started'
				if not already_exists:
#					print 'form.is_valid - creation'
					responseId = utils.create_update_model(CaseStudy(), form, 'create', request)
#					print 'responseId from creation='
#					print responseId
					this_response = utils.build_response(form.errors, '', 'success', responseId, 'CaseStudy')
				else:
#					print 'form.is_valid - update'
					existing_record.created_by = created_by
					responseId = utils.create_update_model(existing_record, form, 'update', request)
#					print 'responseId from update='
#					print responseId
					this_response = utils.build_response(form.errors, '', 'success', responseId, 'CaseStudy')

			else:
				print 'no form not valid'
				print form.errors
				print str(sys.exc_info()[0])
				print str(sys.exc_info()[1])
				this_response = utils.build_response(form.errors, str(sys.exc_info()[0]), 'failure', '', 'CaseStudy')
		else:
			this_response = utils.build_response(form.errors, 'auth key mis-match', 'failure', '', 'CaseStudy')

#		print 'this_response='
#		print this_response
		return HttpResponse(json.dumps(this_response), mimetype="application/json")
	else:
		# receive_suggestion - Error! you must post to this form
		print ('recieve_casestudy - Error! you must post to this form\n' + str(sys.exc_info()[0]))

