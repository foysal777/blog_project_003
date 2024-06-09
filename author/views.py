from typing import Any
from django.shortcuts import render,redirect
from . import forms
from django.urls import reverse_lazy
from django.contrib.auth.forms import  AuthenticationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth import authenticate , login ,logout,update_session_auth_hash
from django.contrib import messages
from post.models import post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import FormView
    



from django.contrib.auth import login
from .forms import RegistrationForm  

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, "Registration completed successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, "Invalid registration details")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'register'
        return context

    
#  log in of cardview 
class log_inView(LoginView):
    template_name = 'register.html'
    # success_url = reverse_lazy('profile')
    def get_success_url(self):
         return reverse_lazy('profile')
    
    def form_valid(self, form):
        messages.success(self.request, "Logged in Complete successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request, "Invalid User and Password")
        return super().form_invalid(form)
    
    
    def get_context_data(self, **kwargs) :
        context =  super().get_context_data(**kwargs)
        context['type'] ='log_in'
        return context
    
# def log_out(request):
#     logout(request)
#     messages.success(request, 'Log out Successfully Completed')
#     return redirect ('log_in')

class log_out(LogoutView):

    def get_success_url(self):
        return reverse_lazy('log_in')

    def dispatch(self, request, *args, **kwargs):
        messages.success(self.request, 'Logged out successfully')
        return super().dispatch(request, *args, **kwargs)
   
    
  

@login_required
def profile(request):
    
    form = post.objects.filter(authors = request.user)     
    return render(request, 'profile.html' ,{'data': form} )
    



def edit_profile(request):
    
        if request.method=='POST':
            profile_form = forms.user_change_data(request.POST , instance = request.user )
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, 'Profile update Successfully Completed')

            return redirect('profile')
        
        else:
         profile_form = forms.user_change_data( instance = request.user)  
        return render(request, 'edit_profile.html' , {'data' : profile_form } )










def pass_change(request):
    
        if request.method=='POST':
            pass_form = PasswordChangeForm(request.user, data=request.POST )
            if pass_form.is_valid():
                pass_form.save()
                messages.success(request, 'Password update Successfully Completed')
                update_session_auth_hash(request, pass_form.user)
                messages.success(request, 'Your password alredy Changed')
                return redirect('profile')
        
        else:
         pass_form = PasswordChangeForm(request.user)  
        return render(request, 'pass_change.html' , {'data' : pass_form } )