from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from core import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('messages/', include("pinax.messages.urls", namespace="pinax_messages")),
    path('', include('core.urls', namespace="core")),
    path('', include('tienda.urls', namespace="tienda")),
    path('cart/', include('cart.urls', namespace="carrito")),
    path('fav/', include('favs.urls', namespace="favs")),
    path('denuncia/', include('denuncia.urls', namespace="denuncia")),


]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
