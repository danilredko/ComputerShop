from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
import requests
import pytz
from django.utils import timezone
# The function returns ip-address of client


def get_client_ip(request):

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


# The function returns how many times a user
# visits the page before session expires

def get_visits(request):

    if 'visits' not in request.session:

        request.session['visits'] = 1

    else:

        request.session['visits'] = request.session.get('visits') + 1

    return request.session['visits']


def get_timezone():

    response = requests.get('http://ip-api.com/json/').json()

    return response['timezone']


def index(request):

    ip = get_client_ip(request)
    visits = get_visits(request)
    timezone = get_timezone()
    return render(request, 'part1.html', {'ip': ip, 'visits': visits, 'timezone': timezone})

