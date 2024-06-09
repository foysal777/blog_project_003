from django import forms
from .models import post,comment


class post_form(forms.ModelForm):
    class Meta :
        model = post
        # fields = '__all__'
        exclude = ['authors']
        
class commentForm(forms.ModelForm):
    class Meta :
        model = comment
        fields = ['name' , 'comment_here' , 'email']
       