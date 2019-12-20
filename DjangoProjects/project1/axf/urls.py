from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('', views.market, name="market"),
    path('', views.cart, name="cart"),
    path('', views.mine, name="mine"),
]
