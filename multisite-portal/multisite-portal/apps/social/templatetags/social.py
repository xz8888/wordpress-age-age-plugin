from apps.social.models import Application, Share
from django import template
import settings
from django.utils.translation import get_language
from django.conf import settings

register = template.Library()

@register.inclusion_tag('social/templates/share.html', takes_context=True)
def share(context, text, url):
	if len(Share.objects.all()) == 0:
		active = False
	else:
		active = True
	

	share_url = None

	try:
		share_url = settings.SHARE_DOMAIN
	except:
		pass
	
	return {'text':text,
			'url':url,
			'share_domain':share_url,
			'active':active,
			'language':get_language(),}

	
@register.inclusion_tag('social/templates/share_include.html', takes_context=True)
def share_include(context, text, url, template):
	template = 'share_' + template.lower() + '.html'
		
	return {'text':text,
			'url':url,
			'template':template,
			}
