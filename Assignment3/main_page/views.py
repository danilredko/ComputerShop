from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def main_page(request):

    return render(request, 'tma3.html')

