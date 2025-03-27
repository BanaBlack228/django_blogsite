from django.urls import path
from blog.views import index, about, add_post

app_name = 'blog'
urlpatterns = [
    path('', index, name='index'),
    path('post/', add_post, name='add_post'),
    path('about/', about, name='about')
]
