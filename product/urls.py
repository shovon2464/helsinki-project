from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import account.views
import product.views
import cart.views

urlpatterns = [
     path('all/', product.views.product_home, name = 'product_home'),
     path('<int:product_id>/', product.views.detail, name='detail'),
     path('<int:product_id>/comment_product/', product.views.comment_product, name='comment_product'),
     path('cart/', include('cart.urls')),
     path('search/', product.views.search, name='search'),
]
