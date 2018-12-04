from django.shortcuts import render, render_to_response, get_object_or_404

from .models import User, Category, Product
from django import forms
from django.http import HttpResponseRedirect
# Create your views here.

class UserForm(forms.Form):
    stuid = forms.CharField(label = '账号 :',max_length = 15)
    password = forms.CharField(label = '密码 :',widget = forms.PasswordInput())

def login(request):
    if request.method=='POST':
        uf=UserForm(request.POST)
        if uf.is_valid():
            #获取表单用户密码
            stuid = uf.cleaned_data['stuid']
            password = uf.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            user = User.objects.filter(stuid__exact = stuid,password__exact = password)
            if user:
                return render_to_response('sells/product/home.html', {'stuid': stuid})
            else:
                return HttpResponseRedirect('/login/')
    else:
        uf = UserForm()  
    return render_to_response('login.html',{'uf':uf})


# 根据品类显示商品
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(categories, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'sells/product/home.html',
                  {'category': category, 'categories': categories, 'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, availbable=True)
    return render(request, 'detailinfo.html', {'product': product})
