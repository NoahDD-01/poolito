from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class HearArea(models.Model):
    icon_img = models.ImageField(upload_to='hero_area', blank=True, null=True)
    icon_title = models.CharField(max_length=20,blank=True,null=True)
    bg_img =  models.ImageField(upload_to='hero_area', blank=True, null=True)
    title = models.CharField(max_length=20,blank=True,null=True)
    note = models.CharField(max_length=100, blank=True,null=True)
    video = models.URLField(null=True,blank=True)

class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Service1(models.Model):
    title = RichTextField(null=True ,blank=True)
    description = models.TextField(null=True,blank=True)
    icon = models.ImageField(upload_to='Service1', blank=True , null=True)
    backgoung_image = models.ImageField(upload_to='Service1' ,blank=True,null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery', blank=True ,null=True)
    image_name = models.CharField(max_length=20)