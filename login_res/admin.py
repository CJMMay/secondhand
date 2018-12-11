from django.contrib import admin

# Register your models here.
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('stuid', 'username', 'password', 'tele',
                    'class1','major','sex')
admin.site.register(User,UserAdmin)