from django.db import models
from django.urls import reverse

# Create your models here.
class User(models.Model):
    stuid=models.CharField(max_length=15,primary_key=True)
    password=models.CharField(max_length=10)
    username = models.CharField(max_length=250)
    tele = models.CharField(max_length=250)
    class1 = models.CharField(max_length=250)
    major = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    sex =models.CharField(max_length=4)

    def __str__(self):
        return self.stuid


    class Meta:
       ordering = ('-created',)
       verbose_name = 'User'
       verbose_name_plural = 'Users'