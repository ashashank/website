from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=200,default='')
    lname = models.CharField(max_length=200,default='')
    city = models.CharField(max_length=200,default='')
    job = models.CharField(max_length=200,default='')
    organ = models.CharField(max_length=200,default='')
    q1 = models.TextField(default='')
    q2 = models.TextField(default='')
    q3 = models.CharField(max_length=200,default='')
    q4 = models.CharField(max_length=200,default='')
    q5 = models.CharField(max_length=200,default='')
    q6 = models.TextField(default='')
    q7 = models.TextField(default='')
    q8 = models.TextField(default='')
    q9 = models.TextField(default='')
    q10 = models.TextField(default='')
    q11 = models.TextField(default='')
    q12 = models.CharField(max_length=500,default='')
    date = models.DateTimeField(default=timezone.now)


    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.name
