from django.forms import ModelForm
from .models import Post,Comment


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('Message',)