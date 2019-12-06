from django.contrib.auth import get_user_model
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views

User = get_user_model()


urlpatterns = [
     path('signup/', views.signup, name = 'signup'),
     path('login/', views.login, name = 'login'),
     path('logout/', views.logout, name = 'logout'),

     path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
     name='password_change_done'),

     path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),
     name='password_change'),

     path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
     name='password_reset_done'),

     path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
     path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),

     path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
     name='password_reset_complete'),

     path('<int:user_id>/', views.profile, name = 'profile'),
     path('<int:user_id>/edit/', views.edit, name = 'edit'),
     path('<int:user_id>/edit_save/', views.edit_save, name = 'edit_save'),

]
