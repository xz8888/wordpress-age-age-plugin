from django.contrib import admin
from apps.multilingual.admin import MultilingualModelAdmin, MultilingualModelAdminForm
from apps.common.encode import Encode
from models import About
import settings
from django.utils import translation
from multilingual.utils import GLL

class AboutAdmin(MultilingualModelAdmin):
	use_fieldsets = (
					('Video options', {'fields':('video','video_image')}),
					('Content', {
						'fields':('tagline','left_header','left_body','right_header','right_body'),
				}),
			)
	
	def save_model(self, request, obj, form, change):
		obj.save()

		if 'video' in request.FILES:
			
			encode = Encode()
			upload_path = '%s/about/%s/hero' %(settings.SITE,GLL.language_code)
			encode.upload_aws_s3(str(obj.video), upload_path)

admin.site.register(About, AboutAdmin)