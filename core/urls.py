from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [

	path("", views.home, name="home"),
	path("login/", views.login, name="login"),
	path("privacy/", views.privacy, name="privacy"),
	path("logout/", auth_views.LogoutView.as_view(), name="logout"),

]