from apps.common.admin import ItemSlugAdmin
from apps.multilingual.admin import admin
from apps.workisobar.models import CaseStudy, CaseStudyIndex, Award, Clients, ClientsIndex, PressRelease, ClientQuote, SlideShowItem
from django.contrib import admin
from django.core.urlresolvers import reverse
from apps.common import utils
from apps.common.encode import Encode
import settings
from django.contrib import messages
from multilingual.utils import GLL
from apps.multilingual.admin import MultilingualModelAdmin,MultilingualInlineAdmin
   
class PressReleaseInline(MultilingualInlineAdmin): 
    model = PressRelease 
    extra = 0

class ClientQuoteInline(MultilingualInlineAdmin):
    model = ClientQuote
    extra = 0

class SlideShowItemInline(MultilingualInlineAdmin):
    model = SlideShowItem
    extra = 0

class AwardInline(MultilingualInlineAdmin):
    model = Award
    extra = 0

class CaseStudyIndexAdmin(MultilingualModelAdmin):
    list_display = ('title',)
    
    search_fields = ['title']
    
    use_fieldsets = (
        ('Featured', {
            'fields': ('featured_video',),
        }),
        ('Content', {
            'fields': ('active', 'title', 'headline'),
        }),
        ('Metadata', {
           'fields': ('meta_description',)
        }),          
    )


class CaseStudyAdmin(MultilingualModelAdmin):
    local_file = ''
    aws_file_key = ''
    
    prepopulated_fields = {'slug': ('title_id',)}
    
    list_display = ('title_id','publish_date')
    
    search_fields = ['title_id']
    
    inlines = [
               AwardInline,
               PressReleaseInline, 
               ClientQuoteInline,
               SlideShowItemInline
               ]

    use_fieldsets = (
       ('Content', {
            'fields' : ('active', 'order','title', 'title_id', 'slug', 'publish_date', 'client', 'body', 'url',),
       }),
       ('Video', {
            'fields' : ('hero_image','video_image', 'video',),
       }),
       ('Homepage', {
            'fields' : ('logo_sprite','homepage_image',),
       }),
    )
    
    def save_model(self, request, obj, form, change):

        page_updates = []
    
        page_updates.append(str(reverse('works_view')))
        

        obj.save()


        if 'video' in request.FILES:
            encode = Encode()
            #upload_path = settings.SITE +'/work/'+ str(obj.id) +'/hero'
            data = {'site':settings.SITE, 'id':obj.id, 'lang':GLL.language_code}
            upload_path = '%(site)s/work/%(id)d/%(lang)s/hero' % data
            
            encode.upload_aws_s3(str(obj.video), upload_path)


class ClientsAdmin(MultilingualModelAdmin):
    list_display = ('client',)
    
    search_fields = ['client']
    
    use_fieldsets = (
       ('Content', {
            'fields' : ('client', 'active', 'featured', 'order', 'logo', 'description','url',),
       }),
    )
    
    
class ClientsIndexAdmin(MultilingualModelAdmin):
    list_display = ('title',)
    
    search_fields = ['title']
    
    use_fieldsets = (
        ('Featured', {
            'fields': ('featured_video',),
        }),
        ('Content', {
            'fields': ('active', 'title', 'headline',),
        }),
        ('Metadata', {
           'fields': ('meta_description',)
        }),          
    )
    
    
  

   
admin.site.register(CaseStudy, CaseStudyAdmin)
admin.site.register(CaseStudyIndex, CaseStudyIndexAdmin)
admin.site.register(Clients, ClientsAdmin)
admin.site.register(ClientsIndex, ClientsIndexAdmin)
