# -*- coding: utf-8 -*-
from django.conf import settings
from django.urls import path
from sells import views
from django.conf.urls.static import static
#from . import views  这个也可以使用,跟上面那个一样的
app_name = 'sells'
urlpatterns = [
    path('publish/', views.publish, name='publish'),
    path('do_publish/', views.do_publish, name='do_publish'),
    path('product_list/', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
