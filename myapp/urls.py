from django.urls import path
from .import views

urlpatterns = [
    path('', views.indexview , name = 'home'), 
    path('about/',views.About_view, name = 'about'),
    path('blog/',views.blog_view, name='blog'),
    path('service/',views.service_view, name = 'service'),
    path('blog_detail/',views.blog_detail,name ='blog_detail')
]