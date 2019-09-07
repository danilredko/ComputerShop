from django.shortcuts import render
from .models import Item, Order, OrderItems
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

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
def cart(request, item_id):

    if 'cart' not in request.session:
        request.session['cart'] = list()

    else:
        request.session['cart'] = request.session['cart'] + [item_id]

    return redirect('home')


def show_cart(request):

    if 'cart' not in request.session:
        cart_items = 0
    else:
        cart_items = Item.objects.filter(pk__in=request.session['cart'])

    return render(request, 'show_cart.html', {'cart_items': cart_items})