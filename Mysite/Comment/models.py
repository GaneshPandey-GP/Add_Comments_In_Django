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
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')


    class Meta:
        ordering = ('timestamp',)

    def __str__(self):
        return 'Comment by {}'.format(self.user)


