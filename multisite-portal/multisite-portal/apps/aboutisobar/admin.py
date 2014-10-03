from django.contrib import admin
from apps.aboutisobar.models import About, Profile, Service, Partner
from apps.multilingual.admin import MultilingualModelAdmin, MultilingualInlineAdmin

class ServiceAdmin(MultilingualModelAdmin):
    pass

class AboutAdmin(MultilingualModelAdmin):
    list_display = ('title',)
    
    use_fieldsets = (
       ('Page ID', {'fields' : ('title', 'active', 'meta_description', 'featured_slogan', 'featured_video', 'profiles_text'),}),
       ('Profile', {'fields' : ('profiles',),}),
       ('Partner', {'fields' : ('partners',),}),
       ('Service', {'fields' : ('services',),}),
    )
    
    filter_horizontal = ('profiles', 'partners', 'services')

    
class ProfileAdmin(MultilingualModelAdmin):
    list_display = ('name',)
    use_fieldsets = (
       ('Profile', {'fields' : ('order', 'name', 'image', 'description'),}),
    )

class PartnerAdmin(MultilingualModelAdmin):
    use_fieldsets = (
       ('Partner', {'fields' : ('title', 'description', 'image'),}),
    )
    
admin.site.register(About, AboutAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Partner, PartnerAdmin)
