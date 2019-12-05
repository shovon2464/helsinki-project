from django.contrib.auth import get_user_model
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
User = get_user_model()


urlpatterns = [
     path('signup/', views.signup, name = 'signup'),
     path('login/', views.login, name = 'login'),
     path('logout/', views.logout, name = 'logout'),
     path('<int:user_id>/', views.profile, name = 'profile'),
     path('<int:user_id>/edit/', views.edit, name = 'edit'),
     path('<int:user_id>/edit_save/', views.edit_save, name = 'edit_save'),

]
