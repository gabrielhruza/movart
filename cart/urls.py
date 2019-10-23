from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
	
	path("", views.get_cart, name="ver_carrito"),
	path("add/<product_id>/<quantity>/", views.add_to_cart, name="additem"),
	path("delete/<product_id>/", views.remove_from_cart, name="deleteitem"),

]
