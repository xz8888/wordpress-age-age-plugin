from apps.common import utils
from apps.news.models import Story, Category
from isobar.apps.news.forms import StoryForm, RelatedLinkForm
from apps.social.models import Application
from django import template
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson as json
from django.views.decorators.csrf import csrf_exempt
import settings
import sys

template.add_to_builtins('apps.news.templatetags.news')

def index(request):
	return news_page(request, 1)

def news_page(request, page, ajax=False):
	try:
		stories_list = Story.objects.all() \
			.filter(layoutitem_ptr__item_ptr__active = True) \
			.order_by( '-sticky', '-publish_date')						
 	except Story.DoesNotExist: 
		raise Http404
	
	return pagination(request, stories_list, page, ajax=ajax)

def pagination(request, list, page, total=6, comment=False, ajax=False, category=''):
	paginator = Paginator(list, total)

	try:
		page = int(request.GET.get('page', page))
	except ValueError:
		page = page

	try:
		stories = paginator.page(page)
	except (EmptyPage, InvalidPage):
		return Http404
			
	try:
		Application.objects.all().get(install=Application.TWITTER)
		twitter_installed = True
	except:
		twitter_installed = False
		
	try:
		Application.objects.all().get(install=Application.POSTEROUS)
		posterous_installed = True
	except:
		posterous_installed = False
		
	try:
		Application.objects.all().get(install=Application.PROMO_BOX)
		promo_box_installed = True
	except:
		promo_box_installed = False

	template = 'news.html'
	if ajax:
		template = 'news_ajax.html'
	
	return render_to_response(template, {
				'stories': stories,
				'category': category,
				'comment': comment,
				'page': page,
				'ajax': ajax,
				'twitter_installed': twitter_installed,
				'posterous_installed': posterous_installed, 
				'promo_box_installed': promo_box_installed,
		}, context_instance=RequestContext(request)
	)

def category(request, slug):
	return category_page(request, slug, 1)

def category_page(request, slug, page, ajax=False):
	try:
		category = Category.objects.all().get(slug=slug)
	except Category.DoesNotExist:
		raise Http404

	stories_list = Story.objects.filter( layoutitem_ptr__item_ptr__active=True ) \
					.filter( category__slug=slug ) \
					.order_by( '-publish_date' )
					
	return pagination(request, stories_list, page, 6, True, ajax, slug)

def story(request, year, month, day, slug):
	try: 
		story = Story.objects.filter(layoutitem_ptr__item_ptr__active=True) \
				.get(slug=slug)
	except Story.DoesNotExist:
		raise Http404

	return render_to_response('story.html', { 'story':story },
											 	context_instance=RequestContext(request))
	
def archive_year(request, year):	
	try: 
		stories = Story.objects.filter( layoutitem_ptr__item_ptr__active=True ) \
								.filter( layoutitem_ptr__item_ptr__created__year=year )
	except Story.DoesNotExist:
		raise Http404	
	
	return render_to_response('archive.html', { 'stories':stories },
												 context_instance=RequestContext(request))

def archive_month(request, year, month):
	try: 
		stories = Story.objects.filter( layoutitem_ptr__item_ptr__active=True ) \
								.filter (layoutitem_ptr__item_ptr__created__year=year ) \
								.filter( layoutitem_ptr__item_ptr__created__month=month )
	except Story.DoesNotExist:
		raise Http404	
	
	return render_to_response('archive.html', { 'stories':stories },
											  	context_instance=RequestContext(request))

def archive_day(request, year, month, day):
	try: 
		stories = Story.objects.filter( layoutitem_ptr__item_ptr__active=True ) \
								.filter( layoutitem_ptr__item_ptr__created__year=year ) \
								.filter( layoutitem_ptr__item_ptr__created__month=month ) \
								.filter( layoutitem_ptr__item_ptr__created__day=day )
	except Story.DoesNotExist:
		raise Http404	
	return render_to_response('archive.html', { 'stories':stories },
												context_instance=RequestContext(request))

def archive(request):
	try: 
		stories = Story.objects.filter( layoutitem_ptr__item_ptr__active=True ) \
								.order_by( '-publish_date' )
	except Story.DoesNotExist:
		raise Http404
	
	sorted_stories = dict()
	
	for story in stories:
		if story.publish_date.year not in sorted_stories:
			sorted_stories[story.publish_date.year] = dict()
				
		if story.publish_date.month not in sorted_stories[story.publish_date.year]:
			sorted_stories[story.publish_date.year][story.publish_date.month] = []
				
		sorted_stories[story.publish_date.year][story.publish_date.month].append(story)
	
	#sorted(sorted_stories.iteritems(), key=lambda (v,k): (v,k)
	#keys = sorted_stories.keys()
	#	keys.sort()
	#	sorted_stories = map(sorted_stories.get, keys)
	#	print sorted_stories
	
	#	print sorted_stories
	#	sorted_stories = sorted(sorted_stories.items(), key=lambda x: (x[0]))
	#	print sorted_stories
	
	return render_to_response('archive.html',  {'sorted_stories':sorted_stories }, 
												context_instance=RequestContext(request))

@csrf_exempt
def recieve_newsstory(request):
	form = StoryForm()
	if request.method == 'POST': # If the form has been submitted...
		this_response = {}

		if request.POST['key'] == settings.POST_AUTH:
			try:
				# Look on the external db for this record
				# We have to store the created_by in a variable as dJango seems to lose it once we get inside form.is_valid()?
#				print 'existing_story_record - started'
				existing_record = Story.objects.get(layoutitem_ptr__item_ptr__id = int(request.POST['external_db_id']))
				created_by = existing_record.created_by
				already_exists = True
				# Update form POST with any files that have also been posted
				# http://www.stereoplex.com/blog/django-newforms-file-upload
				form = StoryForm(request.POST, request.FILES, instance=existing_record)
			except Story.DoesNotExist:
				already_exists = False
				form = StoryForm(request.POST, request.FILES)

#			print 'already_exists='
#			print already_exists

			if form.is_valid(): # All validation rules pass
#				print 'form.is_valid - started'
				if not already_exists:
#					print 'form.is_valid - creation'
					responseId = utils.create_update_model(Story(), form, 'create', request)
#					print 'responseId from creation='
#					print responseId
					this_response = utils.build_response(form.errors, '', 'success', responseId, 'Story')
				else:
#					print 'form.is_valid - update'
					existing_record.created_by = created_by
					responseId = utils.create_update_model(existing_record, form, 'update', request)
#					print 'responseId from update='
#					print responseId
					this_response = utils.build_response(form.errors, '', 'success', responseId, 'Story')

			else:
				print 'no form not valid'
				print form.errors
				print str(sys.exc_info()[0])
				print str(sys.exc_info()[1])
				this_response = utils.build_response(form.errors, str(sys.exc_info()[0]), 'failure', '', 'Story')
		else:
			this_response = utils.build_response(form.errors, 'auth key mis-match', 'failure', '', 'Story')

#		print 'this_response='
#		print this_response
		return HttpResponse(json.dumps(this_response), mimetype="application/json")
	else:
		# receive_newsstory - Error! you must post to this form
		print ('recieve_newsstory - Error! you must post to this form\n' + str(sys.exc_info()[0]))


@csrf_exempt
def recieve_relatedlinks(request):
	"""
	Receive a json object in a POST
	Iterate through each one checking if it already exists for this story id
	Create or Update it
	"""

	print 'recieve_relatedlinks'


	form = RelatedLinkForm()
	if request.method == 'POST': # If the form has been submitted...
		this_response = {}
		
		if request.POST['key'] == settings.POST_AUTH:

			print request.POST

			for key, value in json.loads(request.POST['related_links']).items():
#				print key, value

				if value['description'] != None and value['desciption'] != '' and value['url'] != None and value['url'] != '':
					print 'yup'
#
#					try:
#						existing_record = RelatedLink.objects.get(story = int(value['story']))
#						obj = existing_record
#						form = RelatedLinkForm(request.POST, instance=existing_record)
#						print 'existing_record - update'
#					except RelatedLink.DoesNotExist:
#						form = RelatedLinkForm(request.POST)
#						obj = RelatedLink()
#						print 'existing_record - creation'
#
#					if form.is_valid():
#						print 'form.is_valid - started'
#						obj.story = value['story']
#						obj.desciption = value['description']
#						obj.url = value['url']
#						obj.save()
#						this_response = utils.build_response(form.errors, '', 'success', '', 'RelatedLink')
#					else:
#						print 'no form not valid'
#						print form.errors
#						print str(sys.exc_info()[0])
#						print str(sys.exc_info()[1])
#						this_response = utils.build_response(form.errors, str(sys.exc_info()[0]), 'failure', '', 'RelatedLink')

		else:
			this_response = utils.build_response(form.errors, 'auth key mis-match', 'failure', '', 'RelatedLink')

		print 'this_response='
		print this_response
		return HttpResponse(json.dumps(this_response), mimetype="application/json")
	else:
		# recieve_relatedlinks - Error! you must post to this form
		print ('recieve_relatedlinks - Error! you must post to this form\n' + str(sys.exc_info()[0]))
