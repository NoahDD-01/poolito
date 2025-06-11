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

class service2(models.Model):
    title = RichTextField(null=True,blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

class service3(models.Model):
    title = RichTextField(null=True,blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

class service4(models.Model):
    title = RichTextField(null=True,blank=True)
    icon = models.ImageField(upload_to='service4',null=True,blank=True)
    image = models.ImageField(upload_to='service4',null=True ,blank=True)
    description = models.TextField()

class ReviewLeft(models.Model):
    name = RichTextField(null=True,blank=True)
    image = models.ImageField(upload_to='ReviewLeft', null=True,blank=True)
    video = models.URLField(null=True,blank=True)

class Reviewtitle(models.Model):
    name = RichTextField(null=True,blank=True)
    title = RichTextField(null=True,blank=True)

class Review(models.Model):
    name = RichTextField(null=True,blank=True)
    reviewnote = models.TextField()
    image = models.ImageField(upload_to='review', null=True ,blank=True)

class team(models.Model):
    name = RichTextField(null=True ,blank=True)
    image = models.ImageField(upload_to='team',null=True,blank=True)
    aboutus = models.TextField()
    position = models.CharField(max_length=100)
    age  = models.IntegerField(max_length=30)
    phone  = models.IntegerField(max_length=40)
    email = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    exp = models.CharField(max_length=50)
