from apps.common.admin import ItemSlugAdmin
from apps.multilingual.admin import admin
from apps.work.models import Award, CaseStudy
from apps.work.forms import CaseStudyForm
from django.contrib import admin
from django.core.urlresolvers import reverse
from apps.common import utils
from apps.common.encode import Encode
import settings
from django.contrib import messages
from multilingual.utils import GLL
from apps.multilingual.admin import MultilingualModelAdmin,MultilingualInlineAdmin


class AwardInline(admin.TabularInline):
	model =  Award
	extra = 0

class CaseStudyAdmin(MultilingualModelAdmin):
	local_file = ''
	aws_file_key = ''

	prepopulated_fields = {'slug': ('title', )}

	#list_display = ('title','title_i18n', 'slug', 'active', 'publish_date')
	#ordering = ('slug',)
	inlines = [AwardInline]

	# site specific functionality
	if settings.ISOBAR_SITE_BOOL:
		exclude = ('subclass','external_db_id','order','publish_to_external',)
		readonly_fields = ('posting_agency',)
	else:
		#exclude = ('subclass','external_db_id','order','created_by')
		readonly_fields = ('country', 'posting_agency',)
		use_fieldsets = (
				('Content', {
					'fields':('active','title','title_i18n','slug','publish_date','publish_to_external',
							'url','share_url','body','country','posting_agency','hero_image'),
					}),
				('Video options', {'fields':('video','video_image')}),
		)



	#exclude = (fields_to_exclude)
	#readonly_fields = (fields_to_readonly)

	def save_model(self, request, obj, form, change):
		video_selected = False

		page_updates = []

		page_updates.append(str(reverse('work_view', kwargs={'slug':obj.slug})))
		page_updates.append(str(reverse('works_view')))

		if obj.country == None or obj.country == '':
			obj.country = settings.SITE

		obj.save()

		if settings.ISOBAR_SITE_BOOL == False:
			if 'video' in request.FILES:
				video_selected = True

			# If publishing external, no existing external record and no video
			# then inform the user the case study hasn't been published externally.
			if form.cleaned_data['publish_to_external'] == True:
				if obj.external_db_id == -1 and video_selected == False:
					msg = u"Case Study NOT published to external! You need " + \
					"to re-upload a video if publishing to an external site. " + \
					"Please edit and try again."
					messages.add_message(request, messages.INFO, msg)
				else:
					utils.publish_to_external(self, obj, request)




		if 'video' in request.FILES:
			encode = Encode()
			#upload_path = settings.SITE +'/work/'+ str(obj.id) +'/hero'
			data = {'site':settings.SITE, 'id':obj.id, 'lang':GLL.language_code}
			upload_path = '%(site)s/work/%(id)d/%(lang)s/hero' % data

			encode.upload_aws_s3(str(obj.video), upload_path)

admin.site.register(CaseStudy, CaseStudyAdmin)
