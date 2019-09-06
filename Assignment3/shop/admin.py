from django.contrib import admin

# Register your models here.
from .models import Item, Order, OrderItems
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderItems)
