# django form
#https://docs.djangoproject.com/en/3.2/topics/forms/

from django import forms
from django.forms import ModelForm, TextInput
from .models import Weather


class MeteoForm(ModelForm):
    class Meta:
        model = Weather
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={'class': 'input', 'placeholder': 'City Name'}),
            }