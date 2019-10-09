from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'favs'

urlpatterns = [
	
	#Productos favoritos
	path("p/list/", views.plist, name="plist"),
	path("p/<pid>/add/", views.padd, name="padd"),
	path("p/<pid>/remove/", views.premove, name="premove"),

	#Tiendas favoritas
	path("t/list/", views.tlist, name="tlist"),
	path("t/<tid>/add/", views.tadd, name="tadd"),
	path("t/<tid>/remove/", views.tremove, name="tremove"),	

]