from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from .models import OrderItem
from .forms import OrderCreateForm, OrderTransForm
from sells.models import Product
from django.http import HttpResponseRedirect
# Create your views here.
def order_create(request,product_id):
    stuid=request.session['stuid']
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
       form=OrderCreateForm(request.POST)
       if form.is_valid():
          order=form.save()
          pro = Product.objects.get(id=product_id)
          pro.available = False
          pro.save()
          OrderItem.objects.create(order=order, product=product, price=product.price)
          form = OrderTransForm()
          return render(request, 'orders/order/created.html',  {'order': order,'form':form})
    else:
        form = OrderCreateForm()

    return render(request, 'orders/order/create.html', {'product': product, 'form': form,'stuid':stuid})

# def receive(request,product_id):
# #     product=get_object_or_404(Product,product_id=product_id)
# #     orderItem=get_object_or_404(OrderItem,product=product)
# #     if request.method == "POST":
# #         form = OrderTransForm(request.POST)
# #         if form.is_valid():
# #             orderItem.order.finished=form.cleaned_data['finished']
# #             orderItem.order.paid=form.cleaned_data['paid']
# #             orderItem.order.stuid=orderItem.order.stuid
# #             orderItem.order.address=orderItem.order.address
# #             orderItem.save()
# #             return render(request, 'orders/order/order_sucessful.html')
# #     else:
# #         form = OrderTransForm()
#       return render(request, 'orders/order/created.html', {'order': order,'form': form})