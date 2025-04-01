from tkinter.font import names

from django.urls import path
from blog.views import index, about, add_post,read_post

app_name = 'blog'
urlpatterns = [
    path('post/', add_post, name='add_post'),
    path('post/<int:pk>/',read_post,name='read_post'),
    path('about/', about, name='about'),
    path('', index, name='index'),
]
