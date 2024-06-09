from django.db import models
from categories.models import category_model
from django.contrib.auth.models import User

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    categorys = models.ManyToManyField(category_model)
    authors = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/media/upload', blank= True, null= True)
    
    def __str__(self):
        return self.title


class comment(models.Model):
    post = models.ForeignKey(post,  on_delete=models.CASCADE , related_name= 'comments')
    name = models.CharField(max_length=40)
    email = models.EmailField()
    comment_here = models.TextField()
    show_time = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
            return f'Comments by : { self.name }' 
        
        