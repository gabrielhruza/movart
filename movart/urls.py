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
    path('', include('core.urls', namespace="core")),

]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
