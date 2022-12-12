from django import forms
from django.forms import ModelForm
from .models import Proyecto

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['photo','title','description','tags','urlgithub']
        widgets = {
            'photo': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.TextInput(attrs={'class': 'form-control'}),
            'urlgithub': forms.TextInput(attrs={'class': 'form-control'}),
            }