from django.contrib.auth import get_user_model
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views

User = get_user_model()

urlpatterns = [
    path('all/', views.blog_home, name='blog_home'),
    path('<int:blog_id>/', views.blog_detail, name = 'blog_detail'),
    path('<int:blog_id>/comment_blog/', views.comment_blog, name='comment_blog'),
    path('<int:product_id>/reach_product/', views.reach_product, name='reach_product')
]
