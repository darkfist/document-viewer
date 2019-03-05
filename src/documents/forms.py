from django import forms

class AddDocument(forms.Form):
	title 		= forms.CharField()
	description = forms.CharField(required=False)
	document 	= forms.FileField()
	document2	= forms.FileField(required=False)
	document3 	= forms.FileField(required=False)
	document4 	= forms.FileField(required=False)
	document5	= forms.FileField(required=False)
	document6	= forms.FileField(required=False)
	document7 	= forms.FileField(required=False)
	document8 	= forms.FileField(required=False)
	document9 	= forms.FileField(required=False)
	document10	= forms.FileField(required=False)