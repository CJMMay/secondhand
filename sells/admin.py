from django.contrib import admin

# Register your models here.
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('stuid', 'username', 'password', 'tele',
                    'class1','major','sex')
admin.site.register(User,UserAdmin)
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    #哪些字段可以显示
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated','stuid','gold','tel']
    #过滤字段
    list_filter = ['available', 'created', 'updated']
    #可编辑字段
    list_editable = ['price','available','gold','tel']
    #数据一致
    prepopulated_fields = {'slug': ('name',)}