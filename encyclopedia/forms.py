from django.forms import ModelForm
from django import forms

class Entry_Form(ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}))
    content = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Context'}))
