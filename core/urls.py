from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [

	path("logout/", auth_views.LogoutView.as_view(), name="logout"),
	path("", views.home, name="home"),
	path("login/", views.login, name="login"),
	path("privacy/", views.privacy, name="privacy"),
	path("verificar_perfil/", views.verificar_perfil, name="verificar_perfil"),
	path("actualizar_perfil/", views.actualizar_perfil, name="actualizar_perfil"),
	path("ver_perfil/", views.ver_perfil, name="ver_perfil"),

]