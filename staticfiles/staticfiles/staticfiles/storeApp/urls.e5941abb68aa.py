from django.urls import path
from . import views

urlpatterns = [
    path('mystore/', views.allproducts, name='mystore'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name='update_item'), 
]
