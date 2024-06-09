
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view() , name= 'register'),
    path('log_in/', views.log_inView.as_view() , name= 'log_in'),
    path('log_out/', views.log_out.as_view() , name= 'log_out'),
    path('profile/', views.profile , name= 'profile'),
    path('edit_profile/', views.edit_profile , name= 'edit_profile'),
    path('pass_change/', views.pass_change , name= 'pass_change'),
 
]
