from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import account.views
import product.views
import blog.views
import cart.views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('account/', include('account.urls')),
    path('product/', include('product.urls')),
    path('blog/', include('blog.urls')),
    path('cart/', include('cart.urls')),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
