from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.welcome_page, name='welcome_page'),
    path('home', views.home, name='home'),
    path('cart/<int:item_id>/', views.cart, name='cart'),
    path('delete_item/<int:item_id>/', views.delete_cart_item, name='delete_cart_item'),
    path('show_cart', views.show_cart, name='show_cart')

]
