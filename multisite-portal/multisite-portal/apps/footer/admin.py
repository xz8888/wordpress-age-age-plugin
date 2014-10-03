from apps.common.admin import ItemAdmin
from django.contrib import admin
from apps.footer.models import Email, Social, Footer, Phone, Promo

from apps.multilingual.admin import MultilingualInlineAdmin


class EmailInline(admin.StackedInline):
	model =  Email
	extra = 0
	
class PhoneInline(admin.StackedInline):
	model =  Phone
	extra = 0
	
class SocialInline(admin.StackedInline):
	model =  Social
	extra = 0
	fk_name = "footer"
	exclude = ('subclass','active')

class PromoInline(MultilingualInlineAdmin):
	model =  Promo
	extra = 0
	max_num = 1

class FooterAdmin(ItemAdmin):
	inlines = [EmailInline, PhoneInline, SocialInline, PromoInline]
	exclude = ('order','subclass','active')

admin.site.register(Footer, FooterAdmin)
