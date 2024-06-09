
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    # path('post/', views.post_form , name= 'add_post'),
    path('post/', views.add_post_classView.as_view() , name= 'add_post'),
    path('edit/<int:id>', views.edit_post_view.as_view() , name= 'edit_post'),
    path('delete/<int:id>', views.delete_view.as_view() , name= 'delete_post'),
    path('post_details/<int:id>', views.post_details.as_view() , name= 'post_details'),
 
]
