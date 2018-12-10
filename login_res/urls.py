from django.conf import settings
from django.urls import path
from login_res import views

from django.conf.urls.static import static

# from . import views  这个也可以使用,跟上面那个一样的
app_name = 'login_res'
urlpatterns = [

    path('res/', views.res, name='res'),
    path('do_res/', views.do_res, name='do_res'),
    path('login/', views.login, name='login'),

]
