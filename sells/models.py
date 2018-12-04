from django.db import models
from django.urls import reverse

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
       verbose_name = 'User'
       verbose_name_plural = 'Users'
       
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('sells:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    stuid=models.ForeignKey(User, related_name='User', on_delete=models.CASCADE)
    gold = models.CharField(max_length=100,db_index=True)
    tel= models.CharField(max_length=11,db_index=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('sells:product_detail', args=[self.id, self.slug])
