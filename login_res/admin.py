from django.contrib import admin

# Register your models here.
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('stuid', 'username', 'password', 'tele',
                    'class1','major','sex','eml','age','jianjie')
admin.site.register(User,UserAdmin)