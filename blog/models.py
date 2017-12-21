from django.db import models
from django.utils import timezone
import datetime

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    Title = models.CharField(max_length=200)
    Subtitle = models.CharField(max_length=300, null=True, blank=True)
    Title_image = models.FileField(upload_to='documents/%Y/%m/%d', default=None, blank=True)
    Introduction_text =  models.TextField(null=True, blank=True)
    First_paragraph_title= models.CharField(max_length=200, null=True, blank=True)
    First_paragraph_date = models.DateField(default=datetime.date.today,blank=True)
    First_paragraph_text =  models.TextField(null=True, blank=True)
    First_paragraph_image = models.FileField(upload_to='documents/%Y/%m/%d', default=None, blank=True, null=True)
    Second_paragraph_title= models.CharField(max_length=200, null=True, blank=True)
    Second_paragraph_date = models.DateField(default=datetime.date.today,blank=True)
    Second_paragraph_text =  models.TextField(null=True, blank=True)
    Second_paragraph_image = models.FileField(upload_to='documents/%Y/%m/%d', default=None, blank=True, null=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)




    def publish(self):
        self.published_date = timezone.now()
        self.save()

    #def __str__(self):
        #return self.title

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
