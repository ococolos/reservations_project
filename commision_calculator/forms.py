from django import forms

from .models import City


class UploadFileForm(forms.Form):
    file = forms.FileField()

class CityForm(forms.Form):
    city_name = forms.CharField(max_length=25)
