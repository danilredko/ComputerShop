from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.welcome_page, name='welcome_page'),
    path('home', views.home, name='home'),
    path('cart', views.cart, name='cart')

]
