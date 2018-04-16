from django import forms
from s3direct.widgets import S3DirectWidget

class DocumentForm(forms.Form):
    file = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )
class S3DirectUploadForm(forms.Form):
    images = forms.URLField(widget=S3DirectWidget(dest='example_destination'))
