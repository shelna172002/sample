from django import forms
from .models import imagegallery
class ImageForm(forms.ModelForm):
    class Meta:
        model=imagegallery
        fields=('caption','image')