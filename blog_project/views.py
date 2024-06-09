from django.shortcuts import render
from post.models import post 
from categories.models import category_model

def home(request, category_slug=None):
    data = post.objects.all()
    # categories = category_model.objects.all()
    if category_slug is not None:
        category1 = category_model.objects.get(slug=category_slug)
        data = post.objects.filter(categorys =category1)
    categories1 = category_model.objects.all()
        
   
    return render(request, 'home.html', {'data': data , 'data1': categories1})
 
