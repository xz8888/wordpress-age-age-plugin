from django import forms
from models import Story, RelatedLink


class StoryForm(forms.ModelForm):
	class Meta:
		model = Story

	def clean(self):
		"""
		This will force the data to be cleaned.
		"""
		cleaned_data = self.cleaned_data
		return cleaned_data

class RelatedLinkForm(forms.ModelForm):
	class Meta:
		model = RelatedLink

	def clean(self):
		"""
		This will force the data to be cleaned.
		"""
		cleaned_data = self.cleaned_data
		return cleaned_data