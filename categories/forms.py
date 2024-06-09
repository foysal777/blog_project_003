from django import forms
from .models import category_model


class categoryFrom(forms.ModelForm):
    class Meta:
        model = category_model
        fields = '__all__'
        
        
        
