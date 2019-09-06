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

    hard_drives = Item.objects.filter(ItemType='HardDrive')

    mother_boards = Item.objects.filter(ItemType='MotherBoard')

    monitors = Item.objects.filter(ItemType='Monitor')

    return render(request, 'home.html', {'rams': rams, 'cpus': cpus, 'hard_drives': hard_drives, 'mother_boards': mother_boards, 'monitors': monitors})

