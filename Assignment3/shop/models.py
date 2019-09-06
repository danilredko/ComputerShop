from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Item(models.Model):

    type_choices = [
        ('RAM', 'RAM'),
        ('CPU', 'CPU'),
        ('HD', 'Hard Drive'),
        ('MB', 'MotherBoard'),
        ('Monitor', 'Monitor')
    ]

    ItemType = models.CharField(max_length=10, choices=type_choices)
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=400)
    price = models.DecimalField(max_digits=6, decimal_places=2)


class Order(models.Model):

    customer = models.ForeignKey(User, related_name='order', on_delete=models.DO_NOTHING)


class OrderItems(models.Model):

    order_owner = models.ForeignKey(Order, related_name='order_item', on_delete=models.DO_NOTHING)
    item_contains = models.ForeignKey(Item, related_name='item_cont', on_delete=models.DO_NOTHING)
