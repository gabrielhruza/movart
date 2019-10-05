from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'tienda'

urlpatterns = [
	
	path("tienda/add/", views.tiendadd, name="tiendadd"),
	path("tienda/list/", views.tiendalist, name="tiendalist"),
	path("prod/<id>/ver/", views.prodver, name="prodver"),
	path("prod/add/<url>/", views.prodadd, name="prodadd"),
	path("prod/<id>/edit/", views.prodedit, name="prodedit"),
	path("prod/<id>/list/", views.prodlist, name="prodlist"),
	path("prod/list/", views.prodlistall, name="prodlistall"),

]