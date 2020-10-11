from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    Title =  models.CharField(max_length=50)
    Overview =  models.CharField(max_length=100)
    content = models.TextField()
    Date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Title    
    
    @property
    def get_comnents(self):
        return self.Comments.all().order_by('-timestamp')    

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    post = models.ForeignKey(Post,related_name="Comments",on_delete=models.CASCADE,blank=True,null=True)
    Message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.post)

