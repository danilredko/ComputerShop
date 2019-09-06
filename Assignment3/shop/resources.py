from .models import Item, OrderItems, Order
from import_export import resources


class ItemResources(resources.ModelResource):

    class Meta:
        model = Item
