from django import template
from apps.footer.models import Footer, Social, Phone, Email, Promo

register = template.Library()
 
@register.inclusion_tag('footer/templates/footer.html', takes_context=True)
def footer(context):
	footer = None
	social = None
	phone = None
	promo = None
	email = None
	
	try:
		footer = Footer.objects.all()[:1][0]
		social = Social.objects.filter(footer=footer)
		phone = Phone.objects.filter(footer=footer)
		email = Email.objects.filter(footer=footer)
		promo = Promo.objects.get(footer=footer)
	except:		
		pass

	return {
		'footer': footer,
		'social': social,
		'phone': phone,
		'email': email,
		'promo': promo,
		'request': context['request'],
		'settings': context['settings'],
	}