from django.shortcuts import render, get_object_or_404

from .models import Category, Product
from django import forms
from django.http import HttpResponseRedirect
from cart.forms import CartAddProductForm

# Create your views here.

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
    cart_product_form = CartAddProductForm()
    #return render(request, 'sells/product/detail.html', {'product': product, 'cart_product_form': cart_product_form})
    return render(request, 'detailinfo.html', {'product': product})
