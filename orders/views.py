from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from .models import OrderItem
from .forms import OrderCreateForm
from sells.models import Product,Category
# Create your views here.
def order_create(request,product_id):
    stuid=request.session['stuid']
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
       form=OrderCreateForm(request.POST)
       if form.is_valid():
          order=form.save()
          OrderItem.objects.create(order=order, product=product, price=product.price)
          product.available=False
          return render(request, 'orders/order/created.html',  {'order': order})
    else:
        form = OrderCreateForm()

    return render(request, 'orders/order/create.html', {'product': product, 'form': form,'stuid':stuid})