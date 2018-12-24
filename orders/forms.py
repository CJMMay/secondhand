from django import forms
from .models import Order
from sells.models import Product,Category
from login_res.models import User

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order

        fields = ['address','stuid']

class OrderTransForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['finished','paid']
