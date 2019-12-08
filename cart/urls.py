from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import account.views
import product.views
import cart.views

urlpatterns = [
     path('<int:product_id>/', cart.views.add_to_cart, name='add_to_cart'),
     path('<int:product_id>/', cart.views.add_to_cart2, name='add_to_cart2'),
     path('cart_home/', cart.views.cart_home, name='cart_home'),
     path('reach_product_home', cart.views.reach_product_home, name='reach_product_home'),
     path('<int:order_id>/proceed', cart.views.proceed, name='proceed'),


]
