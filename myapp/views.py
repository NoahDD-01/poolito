from django.shortcuts import render
from .models import *

# Create your views here.
def indexview(request):
    hero_area = HearArea.objects.all().order_by('-id')[:1]
    service1 = Service1.objects.all().order_by('-id')[:4]
    gallery = Gallery.objects.all().order_by('-id')[:8]
    Service2 = service2.objects.all().order_by('-id')
    Service3 = service3.objects.all().order_by('-id')
    Service4 = service4.objects.all().order_by('id')
    contex = {
        'hero_area':hero_area ,
        'service1' : service1,
        'gallery' : gallery,
        'Service2' : Service2,
        'Service3' : Service3,
        'Service4' : Service4,
    }
    return render(request,'index.html',contex)
def About_view(request):
    return render(request,'about.html')

def blog_view(request):
    blog = Blog.objects.all()
    contex = {
        'blog':blog
    }
    return render(request,'blog.html',contex)

def service_view(request):
    return render(request,'service.html')
