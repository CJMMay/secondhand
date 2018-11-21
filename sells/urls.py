# -*- coding: utf-8 -*-

from django.urls import path
from sells import views
#from . import views  这个也可以使用,跟上面那个一样的
urlpatterns = [
    path('', views.login,name = 'login'),
    path(r'login/changepwd/',views.changepwd,name='changepwd'),
    path(r'login/register/',views.register,name='register'),
]
