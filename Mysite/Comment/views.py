from django.shortcuts import render,redirect,reverse
from .forms import PostForm,CommentForm
from .models import Post
# Create your views here.
def CreatePost(request):
    form =  PostForm()
    if request.method =="POST":
        form = PostForm(request.POST or None)
        if form.is_valid:
            form.save()
            return redirect('/')
    context = {"form":form}
    return render(request,"create.html",context)        

def Post_list(request):
    posts =  Post.objects.all()
    return render(request,'index.html',{'posts':posts})

def Post_details(request,id):
    Posts = Post.objects.get(id=id)
    form = CommentForm()
    if request.method =="POST":
        form = CommentForm(request.POST or None)
        if form.is_valid:
            form.instance.user = request.user
            form.instance.post = Posts
            form.save()
            return redirect(reverse('detail',kwargs={'id':Posts.id}))
    return render(request,"details.html",{"Posts":Posts,"form":form})    