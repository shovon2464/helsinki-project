from django.urls import path
from . import views

urlpatterns = [
     path('all/', views.product_home, name = 'product_home'),
     path('<int:product_id>/', views.detail, name='detail'),
     path('<int:product_id>/comment_product/', views.comment_product, name='comment_product'),

]
