from django import template
from django.contrib.sites.models import Site
from apps.social.models import Analytics
import os
import os.path
import settings

register = template.Library()

@register.inclusion_tag('common/templates/primary_nav.html', takes_context=True)
def primary_nav(context, active = '', link = True):
	return {
		'active': active,
		'link': link,
		'request': context['request'],
		'settings': context['settings'],
	}

@register.simple_tag
def current_domain():
	return Site.objects.get_current()

@register.simple_tag
def current_domain_full():
	return 'http://' + str(current_domain())

@register.filter
def divide(item, val):
	return item / val

@register.filter
def nl2comma(val):
	return val.replace("\r\n", ', ')

@register.filter
def dict_key(dict, key):
	return dict[key]

@register.filter
def thumbnail(file, size='100x100x1'):
	if file is None:
		return None
	
	try:
		import Image
	except ImportError, error:
		return file.url

	if not os.path.exists(file.path):
		return file.url

	# defining the size
	x, y, ratio = [int(x) for x in size.split('x')]
	# defining the filename and the miniature filename
	filehead, filetail = os.path.split(file.path)
	basename, format = os.path.splitext(filetail)
	miniature = basename + '_' + size + format
	filename = file.path
	miniature_filename = os.path.join(filehead, miniature)
	filehead, filetail = os.path.split(file.url)
	miniature_url = filehead + '/' + miniature
	if os.path.exists(miniature_filename) and os.path.getmtime(filename) > os.path.getmtime(miniature_filename):
		os.unlink(miniature_filename)
	# if the image wasn't already resized, resize it
	if not os.path.exists(miniature_filename):
		image = Image.open(filename)
		if ratio == 0:
			image = image.resize([x, y], Image.ANTIALIAS)
		else:
			image.thumbnail([x, y], Image.ANTIALIAS)

		image.save(miniature_filename, image.format)

	return miniature_url

#this filter is added by Sean from isobar Canada to solve the animated gif problem for norway.
#this method does not resize the gif file
@register.filter
def thumbnail_no_gif(file, size='100x100x1'):
	if file is None:
		return None
	
	try:
		import Image
	except ImportError, error:
		return file.url

	if not os.path.exists(file.path):
		return file.url

	# defining the size
	x, y, ratio = [int(x) for x in size.split('x')]
	# defining the filename and the miniature filename
	filehead, filetail = os.path.split(file.path)
	basename, format = os.path.splitext(filetail)
    
	if format.lower() == '.gif':
		return file.url

	miniature = basename + '_' + size + format
	filename = file.path
	miniature_filename = os.path.join(filehead, miniature)
	filehead, filetail = os.path.split(file.url)
	miniature_url = filehead + '/' + miniature
	if os.path.exists(miniature_filename) and os.path.getmtime(filename) > os.path.getmtime(miniature_filename):
		os.unlink(miniature_filename)
	# if the image wasn't already resized, resize it
	if not os.path.exists(miniature_filename):
		image = Image.open(filename)
		if ratio == 0:
			image = image.resize([x, y], Image.ANTIALIAS)
		else:
			image.thumbnail([x, y], Image.ANTIALIAS)

		image.save(miniature_filename, image.format)

	return miniature_url



@register.filter
def dimensions(image):
	image_path = settings.MEDIA_ROOT + str(image)
	im = Image.open(image_path)
	return mark_safe(' width="' + str(im.size[0])
	                + '" height="' + str(im.size[1]) + '" ')

@register.simple_tag
def place_holder_img():
	return settings.MEDIA_URL + 'img/placeholders/' + settings.SITE + '/news-holding-image-'

@register.inclusion_tag('common/templates/analytics.html', takes_context=True)
def analytics(context, position):
	item = None
	
	try:
		item = Analytics.objects.get(position__exact = position)
	except:
		print 'no analytics information found'
		
	return {
		'item':item,		
		'settings': context['settings']
	}