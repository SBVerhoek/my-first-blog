from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200, default='Blog title')
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    docfile = models.FileField(upload_to='documents/%Y/%m/%d', default='MEDIA_ROOT/bali-secret-beach.jpg')
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    #def __str__(self):
        #return self.title

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
