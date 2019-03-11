from django import forms
from django.core.validators import FileExtensionValidator

class AddDocument(forms.Form):
	title 		= forms.CharField()
	description = forms.CharField(required=False)
	document 	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['pdf', 'odt', 'fodt']
												)])
	document2	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['pdf', 'odt', 'fodt']
												)], required=False)
	document3 	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['pdf', 'odt', 'fodt']
												)], required=False)
	document4 	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['pdf', 'odt', 'fodt']
												)], required=False)
	document5	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['pdf', 'odt', 'fodt']
												)], required=False)
	document6	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['pdf', 'odt', 'fodt']
												)], required=False)
	document7 	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['pdf', 'odt', 'fodt']
												)], required=False)
	document8 	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['pdf', 'odt', 'fodt']
												)], required=False)
	document9 	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['pdf', 'odt', 'fodt']
												)], required=False)
	document10	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['pdf', 'odt', 'fodt']
												)], required=False)