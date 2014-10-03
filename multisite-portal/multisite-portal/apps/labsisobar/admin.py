from django.contrib import admin
from apps.labsisobar.models import Partnership, LabsIndex
from apps.multilingual.admin import MultilingualModelAdmin, MultilingualInlineAdmin

class LabsAdmin(MultilingualModelAdmin):
    list_display = ('title',)
    
    use_fieldsets = (
       ('Page ID', {'fields' : ('title','headline','featured_video'),}),
       ('Partnership', {'fields' : ('partnerships',),}),
    )
    
    filter_horizontal = ('partnerships',)

class PartnershipAdmin(MultilingualModelAdmin):
    list_display = ('title',)
    
    search_fields = ['title']
    
    use_fieldsets = (
       ('Content', {
            'fields' : ('title', 'url', 'image', 'remove_image', 'description',),
       }),
    )
    
admin.site.register(LabsIndex, LabsAdmin)
admin.site.register(Partnership, PartnershipAdmin)
