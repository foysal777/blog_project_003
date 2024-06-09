from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm


# class author_form(forms.ModelForm):
#     class Meta :
#         model = author
#         fields = '__all__'


class RegistrationForm(UserCreationForm):
   
    
    class Meta :
        model = User
        fields = ['username' , 'first_name' , 'last_name' , 'email']
        

class user_change_data(UserChangeForm):
    password = None
    class Meta:
        model=User
        fields = ['username' , 'first_name' , 'last_name' , 'email']
