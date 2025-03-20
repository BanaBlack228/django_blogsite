from django.urls import path
from blog.views import index, about

app_name = 'blog'
urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about')
]
