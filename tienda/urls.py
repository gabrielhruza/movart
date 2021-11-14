from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'tienda'

urlpatterns = [
	
	path("tienda/add/", views.tiendadd, name="tiendadd"),
	path("tienda/list/", views.tiendalist, name="tiendalist"),
	path("tienda/ver/<tid>/", views.tiendaver, name="tiendaver"),
	path("tienda/<tid>/prods/", views.prodlist, name="prodlist"),
	path("prod/<pid>/ver/", views.prodver, name="prodver"),
	path("prod/add/<url>/<img>/", views.prodadd, name="prodadd"),
	path("prod/<pid>/edit/", views.prodedit, name="prodedit"),
	path("prod/list/", views.prodlistall, name="prodlistall"),
	path("prod/<pid>/cons/", views.prodcons, name="prodcons"),

]