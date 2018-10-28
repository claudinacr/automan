from . import models 
from django import forms

class OwnerForm(forms.ModelForm):
    class Meta:
        model = models.Owner
        fields = '__all__'
        