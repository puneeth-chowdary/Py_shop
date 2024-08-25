
from django.contrib import admin
from django.urls import path
from . import views 
urlpatterns=[
    path('',views.index,name='index'),
    path('search',views.search,name='search'),
    path('cart',views.cart,name='cart'),
    path('product/<int:id>/',views.product_detail,name='product_detail'),
    path('checkout',views.checkout,name='checkout'),
    path('remove',views.remove,name='remove'),
    path('checky',views.checky,name='checky')


    
]