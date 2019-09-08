from django.shortcuts import render
from .models import Item, Order, OrderItems
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template.defaulttags import register
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
        request.session['cart'] = request.session['cart'] + [item_id]
        request.session['total'] = float(Item.objects.get(pk=item_id).price)

    else:
        request.session['cart'] += [item_id]
        request.session['total'] += float(Item.objects.get(pk=item_id).price)

    request.session['total'] = round(request.session['total'], 2)
    return redirect('home')


@login_required(login_url='welcome_page')
def show_cart(request):

    if 'cart' not in request.session:
        cart_items = 0
    else:
        cart_items = {}
        for id in request.session['cart']:
            cart_item = Item.objects.get(pk=id)
            if cart_item in cart_items:
                cart_items[cart_item] += 1
            else:
                cart_items[cart_item] = 1

    return render(request, 'show_cart.html', {'cart_items': cart_items})


@login_required(login_url='welcome_page')
def delete_cart_item(request, item_id):

    price_to_delete = float(Item.objects.get(pk=item_id).price)
    list_delete = request.session['cart']
    list_delete.remove(item_id)
    request.session['cart'] = list_delete
    request.session['total'] -= price_to_delete
    request.session['total'] = round(request.session['total'], 2)
    return redirect('show_cart')


@login_required(login_url='welcome_page')
def submit_order(request):

    order_to_save = Order.objects.create(customer=request.user, total=request.session['total'])
    order_to_save.save()

    for item_id in request.session['cart']:

        item = Item.objects.get(pk=item_id)

        OrderItems.objects.create(order_owner=order_to_save, item_contains=item).save()

    request.session['cart'] = list()
    request.session['total'] = 0
    return render(request, 'submit_success.html')


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@login_required(login_url='welcome_page')
def order_history(request):

    orders = Order.objects.filter(customer=request.user)

    order_hist = {}

    totals = {}

    for order in orders:

        totals[order.pk] = order.total
        order_hist[order.pk] = {}

        for item in OrderItems.objects.filter(order_owner=order):

            if item.item_contains in order_hist[order.pk]:
                order_hist[order.pk][item.item_contains] +=1
            else:
                order_hist[order.pk][item.item_contains] = 1

            #order_hist[order.pk].append(Item.objects.get(pk=item.pk))

    return render(request, 'order_history.html', {'orders': order_hist, 'totals': totals})

