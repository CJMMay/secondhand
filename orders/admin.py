
# Register your models here.
from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [ 'stuid',
                    'address',  'paid','finished',
                    'created', 'updated']
    list_filter = ['paid', 'finished','created', 'updated']
    inlines = [OrderItemInline]
