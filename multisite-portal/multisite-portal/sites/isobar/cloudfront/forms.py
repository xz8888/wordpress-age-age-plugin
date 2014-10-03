from django import forms

class DistributionForm(forms.Form):
    origin_domain = forms.CharField(max_length=100)
    comment = forms.CharField(max_length=100)