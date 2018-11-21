from django.db import models
# Create your models here.
class User(models.Model):
    STATUS_CHOICES = (
        ('female', '女'),
        ('male', '男'),
    )
    stuid=models.CharField(max_length=15,primary_key=True)
    password=models.CharField(max_length=10)
    username = models.CharField(max_length=250)
    tele = models.CharField(max_length=250)
    class1 = models.CharField(max_length=250)
    major = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    sex = models.CharField(max_length=10,
                                choices=STATUS_CHOICES,
                                default='男')

    def __str__(self):
        return self.stuid

    class Meta:
       ordering = ('-created',) 
