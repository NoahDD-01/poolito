from django.urls import path
from .import views

urlpatterns = [
    path('', views.indexview , name = 'home'), 
    path('about/',views.About_view, name = 'about'),
    path('blog/',views.blog_view, name='blog')
]