from django.urls import path
from .views import Post_list,CreatePost,Post_details

urlpatterns = [
    path('',Post_list,name='home'),
    path('create/',CreatePost),
    path('details/<id>',Post_details, name="detail")
]

