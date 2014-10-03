from multilingual.utils import GLL
from isobar.apps.work.models import *
from isobar.apps.work.forms import *
from isobar.apps.news.models import *
from isobar.apps.news.forms import *
from django.utils import simplejson as json
import settings

from multilingual.utils import GLL # GlobalLanguageLock
from django.core import serializers

#http://pypi.python.org/pypi/poster/0.4
from lib.poster.encode import multipart_encode
from lib.poster.streaminghttp import register_openers
import urllib2
import urllib

import sys

def publish_to_external(self, obj, request):
	"""
	Send the given object (CaseStudy/Story) to another site
	The potential alternate language versions are sent as a json object (in the POST)
	"""
	# Register the streaming http handlers with urllib2
	# http://atlee.ca/software/poster/index.html
	register_openers()

	language_content = {}
	for language in settings.LANGUAGES:
		GLL.lock(language[0])
#		print(language)
#		print obj.body
		language_content[language[0]] = {
			'body': obj.body
		}
		GLL.release()

	s = json.dumps(language_content)

	if isinstance(obj, CaseStudy):
#		print 'publish_to_external CaseStudy - started'
		object = { \
			'subclass': obj.subclass, \
			'active': obj.active, \
			'title': obj.title, \
			'order': obj.order, \
			'slug': obj.slug, \
			'hero_image': open(str(settings.MEDIA_ROOT + str(obj.hero_image.name)), 'rb'), \
			'video_image': open(str(settings.MEDIA_ROOT + str(obj.video_image.name)), 'rb'), \
			'url': obj.url, \
			'publish_date': obj.publish_date, \
			'country': obj.country, \
			'body': obj.body, \
			'key': settings.POST_AUTH, \
			'language_content': s, \
			'external_db_id': obj.external_db_id, \
			'posting_agency': settings.AGENCY_NAME, \
			'share_url': obj.share_url }

		# Only send the video if we have one (in FILES or existing)
		if 'video' in request.FILES:
			object['video'] = open(str(settings.MEDIA_ROOT + str(obj.video.name)), 'rb')

		datagen, headers = multipart_encode(object)
		this_request = urllib2.Request('http://' + settings.LINKED_SITE + '/receive-casestudy/', datagen, headers)
#		print 'publish_to_external CaseStudy - finished'
	elif isinstance(obj, Story):
#		print 'publish_to_external Story - started'
		object = { \
			'subclass': obj.subclass, \
			'active': obj.active, \
			'title': obj.title, \
			'order': obj.order, \
			'slug': obj.slug, \
#			'author': obj.author_id, \
#			'category': obj.category_id, \
			'sticky': obj.sticky, \
#			'image': open(str(settings.MEDIA_ROOT + str(obj.image.name)), 'rb'), \
			'publish_date': obj.publish_date, \
			'country': obj.country, \
			'body': obj.body, \
			'key': settings.POST_AUTH, \
			'language_content': s, \
			'external_db_id': obj.external_db_id, \
			'posting_agency': settings.AGENCY_NAME }

		# Only send the image if we have one (in FILES or existing)
		if obj.image:
			object['image'] = open(str(settings.MEDIA_ROOT + str(obj.image.name)), 'rb')

		datagen, headers = multipart_encode(object)
		this_request = urllib2.Request('http://' + settings.LINKED_SITE + '/receive-newsstory/', datagen, headers)
#		print 'publish_to_external Story - finished'
	try:
		response = urllib2.urlopen(this_request)
	except urllib2.URLError, e:
		if hasattr(e, 'reason'):
			print 'We failed to reach a server.'
			print 'Reason: ', e.reason
		elif hasattr(e, 'code'):
			print 'The server couldn\'t fulfill the request.'
			print 'Error code: ', e.code
	else:
		# 200
		# De-Serialize what comes back
		# Get the record of object just saved
		# Update record, set external_db_id = id recevied back in json
		this_response = json.loads(response.read())

		if isinstance(obj, CaseStudy):
			update_obj = CaseStudy.objects.get(slug=obj.slug)
		elif isinstance(obj, Story):
			update_obj = Story.objects.get(slug=obj.slug)
		update_obj.external_db_id = this_response['id']
		update_obj.save()






		# *************************************************
		# post the related links for this story
		# *************************************************

		if isinstance(obj, Story):
			# run this here as we need to know what the id ()on the receiving db was of the story just published
			# get the related links for this news story
			# iterate and store them in a serialized json object (see s above)
			# send the to another receiving view
			existing_related_links = RelatedLink.objects.all().filter(story = int(obj.id))
			r = serializers.serialize('json', existing_related_links)
			print 'related links='
			print r

			object_related_links = { \
				'story': this_response['id'], \
				'key': settings.POST_AUTH, \
				'related_links': r
			}

			datagen, headers = multipart_encode(object_related_links)
			this_request = urllib2.Request('http://' + settings.LINKED_SITE + '/receive-relatedlinks/', datagen, headers)


			try:
				response = urllib2.urlopen(this_request)
			except urllib2.URLError, e:
				if hasattr(e, 'reason'):
					print 'We failed to reach a server.'
					print 'Reason: ', e.reason
				elif hasattr(e, 'code'):
					print 'The server couldn\'t fulfill the request.'
					print 'Error code: ', e.code
			else:
				# 200
				# De-Serialize what comes back
				# Get the record of object just saved
				# Update record, set external_db_id = id recevied back in json
				this_response = json.loads(response.read())







#		print 'publish_to_external - finished'


def create_update_model(obj, form, action, request):
	"""
	Receive an object (CaseStudy/Story), Create or Update.
	Return ID of object	created or updated.
	"""
	if isinstance(obj, CaseStudy):
#		print 'CaseStudy create_update_model - started'
		obj.subclass = form.cleaned_data['subclass']
		if action == 'create':
			obj.active = False
		obj.title = form.cleaned_data['title']
		obj.order = form.cleaned_data['order']
		obj.slug = form.cleaned_data['slug']
		obj.hero_image = form.cleaned_data['hero_image']
		obj.video_image = form.cleaned_data['video_image']
		obj.video = form.cleaned_data['video']
		obj.url = form.cleaned_data['url']
		obj.publish_date = form.cleaned_data['publish_date']
		obj.country = form.cleaned_data['country']
		obj.posting_agency = form.cleaned_data['posting_agency']
		obj.share_url = form.cleaned_data['share_url']
	elif isinstance(obj, Story):
#		print 'Story create_update_model - started'
		obj.subclass = form.cleaned_data['subclass']
		if action == 'create':
			obj.active = False
		obj.title = form.cleaned_data['title']
		obj.order = form.cleaned_data['order']
		obj.slug = form.cleaned_data['slug']
		obj.author = form.cleaned_data['author']
		obj.category = form.cleaned_data['category']
		obj.sticky = form.cleaned_data['sticky']
		obj.image = form.cleaned_data['image']
		obj.publish_date = form.cleaned_data['publish_date']
		obj.country = form.cleaned_data['country']
		obj.posting_agency = form.cleaned_data['posting_agency']

	for key, value in json.loads(request.POST['language_content']).items():
		GLL.lock(key)
		if value['body'] != None and value['body'] != '':
			obj.body = value['body']
			try:
				obj.save()
			except:
				print str(sys.exc_info()[0])
				print str(sys.exc_info()[1])
			
		GLL.release()

#	print 'create_update_model - finished'
#	print obj.id
	return obj.id


def build_response(formErrors, message, result, id, object):
	"""
	Build a json object response and return it to the caller
	"""
	response = {}
	response['form errors'] = formErrors
	response['message'] = message
	response['result'] = result
	response['id'] = id
	response['object'] = object
	return response

