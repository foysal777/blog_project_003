from django.shortcuts import render,redirect
from . import forms
from . import models
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy
# Create your views here.
# @login_required
# def post_form(request):
#     if request.method=='POST':
#         post_form = forms.post_form(request.POST)
#         if post_form.is_valid():
#             post_form.instance.authors = request.user
#             post_form.save()
#         return redirect('add_post')
    
#     else:
#      post_form = forms.post_form()  
#      return render(request, 'post.html' , {'data' : post_form})
 
 
#  add post replace by class viewd 
@method_decorator(login_required, name='dispatch')
class add_post_classView(CreateView):
    model = models.post
    form_class = forms.post_form
    template_name = 'post.html'
    success_url = reverse_lazy('add_post')
    def form_valid(self, form):       
        form.instance.authors = self.request.user
        return super().form_valid(form)

 




# edit post cardview 
@method_decorator(login_required, name='dispatch')

class edit_post_view(UpdateView):
    model = models.post
    form_class = forms.post_form
    template_name = 'post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')
    



# @login_required
# def delete(request, id):
#     post= models.post.objects.get(pk=id)
#     post.delete()
#     return redirect('homepage')
@method_decorator(login_required, name='dispatch')

class delete_view(DeleteView):
    model = models.post
    from_class = forms.post_form
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg ='id'
    
    
    
class post_details(DetailView):
    model = models.post
    pk_url_kwarg = 'id'
    template_name = 'text_details.html'
    
    
    def post(self, request, *args, **kwargs):
        comment_Form = forms.commentForm(data=self.request.POST)
        post = self.get_object()
        if comment_Form.is_valid():
            new_comment = comment_Form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    
    
    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()       
        comment_Form = forms.commentForm()           
        context['comments'] = comments
        context['comment_Form'] = comment_Form
        return context       
    
      