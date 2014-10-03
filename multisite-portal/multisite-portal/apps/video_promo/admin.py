from apps.common.admin import ItemSlugAdmin
from apps.multilingual.admin import admin
from apps.video_promo.models import VideoPromo
from django.contrib import admin
from django.core.urlresolvers import reverse
from apps.common import utils
from apps.common.encode import Encode
import settings
import os.path
from django.contrib import messages
from multilingual.utils import GLL
from apps.multilingual.admin import MultilingualModelAdmin,MultilingualInlineAdmin



class VideoPromoAdmin(MultilingualModelAdmin):
    local_file = ''
    aws_file_key = ''
    
    list_display = ('video',)
    
    search_fields = ['title']

    use_fieldsets = (
       ('Content', {
            'fields' : ('title', 'body', 'url', 'link_text','order'),
       }),
       ('Video', {
            'fields' : ('hero_image','video_image', 'video',),
       }),
    )
    
    
    def save_model(self, request, obj, form, change):

        obj.save()


        if 'video' in request.FILES:
            encode = Encode()
            #upload_path = settings.SITE +'/work/'+ str(obj.id) +'/hero'
            data = {'site':settings.SITE, 'id':obj.id, 'lang':GLL.language_code}
            upload_path = '%(site)s/videopromo/%(id)d/%(lang)s/hero' % data
            
            encode.upload_aws_s3(str(obj.video), upload_path)


admin.site.register(VideoPromo, VideoPromoAdmin)
