from django import forms
from .models import FreeTaster

class FreeTasterForm(forms.ModelForm):
    class Meta:
        model = FreeTaster
        exclude = ['applied_on']