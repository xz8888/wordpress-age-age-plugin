from django import forms
from models import CaseStudy


class CaseStudyForm(forms.ModelForm):
	
#	def __init__(self, *args, **kwargs):
#		self.request = kwargs.pop('request', None)
#		super(CaseStudyForm, self).__init__(*args, **kwargs)


	class Meta:
		model = CaseStudy


	def clean(self):
		"""
		Check we have been given a video
		"""
#
#		print self.request
#
		cleaned_data = self.cleaned_data
#		video_selected = False
#		publish_to_external = cleaned_data.get("publish_to_external")
#		external_db_id = cleaned_data.get("external_db_id")
#		if 'video' in self.request.FILES:
#			video_selected = True
#
#		print 'doing clean'
#		print publish_to_external
#		print external_db_id
#
#		if (publish_to_external and external_db_id == -1 and video_selected):
#			msg = u"You need to provide a video if publishing to an external " + \
#				"site. Please select one and try again."
#			self._errors["video"] = self.error_class([msg])
#			del cleaned_data["video"]

		return cleaned_data