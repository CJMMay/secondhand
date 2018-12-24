from django.shortcuts import render, get_object_or_404, render_to_response
from login_res.models import User
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.conf import settings
#from django.http import HttpResponseRedirect
# Create your views here.

# 根据品类显示商品
def product_list(request, category_slug=None):
    stuid = request.session['stuid']
    category=None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    new_products=Product.objects.filter(available=True).order_by('-created')
    new_products=new_products[:4]
    if category_slug:
        category = get_object_or_404(categories, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'sells/product/home.html',
                  {'category': category, 'categories': categories, 'products': products,'stuid':stuid,'new_products':new_products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'detailinfo.html', {'product': product,'cart_product_form': cart_product_form})

#发布闲置
#显示发布页面
def publish(request):
    try:
        del request.session['error']
    except:
        return render(request,'publish.html')
    return render(request,'publish.html')

#发布操作
def do_publish(request):
     stuid = request.session['stuid']
     users=User.objects.all()
     for i in users:
         if i.stuid==stuid:
             id=i
     name=request.POST.get('name')
     tel=request.POST.get('tel')
     description=request.POST.get('description')
     price=request.POST.get('price')
     gold=request.POST.get('gold')
     category=request.POST.get('category')
     cat=Category.objects.get(pk=category)
     f1 = request.FILES.get('img')
     image= "products/2018/12/publishphotos" + f1.name
     fname = settings.MEDIA_ROOT + "products/2018/12/publishphotos"+ f1.name
     with open(fname,'wb') as pic:
         for c in f1.chunks():
             pic.write(c)
     Product.objects.create(name=name,description=description,price=price,gold=gold,category=cat,tel=tel,stuid=id,image=image,slug=name)
     return render_to_response('sells/product/home.html', {'stuid': stuid})

# def index(request):
#     return render(request, 'sells/product/home.html')

def showmypublish(request):
    stuid=request.session['stuid']
    #users=User.objects.filter(stuid=stuid)
    #username=users.username
    #tele=users.tele
    products = Product.objects.filter(stuid=stuid)
    return render(request, 'showmypublish.html',
                  {'products': products})