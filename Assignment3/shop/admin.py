from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
# Register your models here.
from .models import Item, Order, OrderItems
#admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderItems)

@admin.register(Item)
class ItemAdmin(ImportExportActionModelAdmin):
    pass