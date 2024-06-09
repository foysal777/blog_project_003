from django.shortcuts import render,redirect
from . import forms

# Create your views here.
def category(request):
    if request.method=='POST':
        categorys_form = forms.categoryFrom(request.POST)
        if categorys_form.is_valid():
            categorys_form.save()
            return  redirect ('add_categories')
    
    
    else :
        categorys_form = forms.categoryFrom()
    return render(request,'category.html' ,{'data': categorys_form })
    