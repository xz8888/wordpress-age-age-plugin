from apps.social.models import PosterousAccount, TwitterAccount, Application, PromoBox, Analytics, Share
from django.contrib import admin
from django.core.urlresolvers import reverse

try:
	Application.objects.all().get(install=Application.POSTEROUS)	
	admin.site.register(PosterousAccount)	
except:
	pass

try:
	Application.objects.all().get(install=Application.TWITTER)
	admin.site.register(TwitterAccount)
except:
	pass

try:
	Application.objects.all().get(install=Application.ANALYTICS)
	admin.site.register(Analytics)
except:
	pass

try:
	Application.objects.all().get(install=Application.PROMO_BOX)
	admin.site.register(PromoBox)	
except:
	pass
	
admin.site.register(Application)
admin.site.register(Share)