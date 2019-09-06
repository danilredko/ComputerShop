from django.shortcuts import render
from .models import Item, Order, OrderItems
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def welcome_page(request):

    return render(request, 'welcome_page.html')


@login_required(login_url='welcome_page')
def home(request):

    rams = Item.objects.filter(ItemType='RAM')

    cpus = Item.objects.filter(ItemType='CPU')

    hard_drives = Item.objects.filter(ItemType='HD')

    mother_boards = Item.objects.filter(ItemType='MB')

    monitors = Item.objects.filter(ItemType='Monitor')

    return render(request, 'home.html', {'items': [cpus, mother_boards, hard_drives, rams, monitors]})


@login_required(login_url='welcome_page')
def cart(request):

    return render(request, 'cart.html')