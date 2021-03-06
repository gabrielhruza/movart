from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .cart import Cart
from tienda.models import Producto


@login_required
def add_to_cart(request, product_id, quantity):
	try:
		product = Producto.objects.get(id=product_id)
		cart = Cart(request)
		cart.add(product, product.precio, quantity)
		messages.success(request, 'Se ha agregado con éxito!')
	except Exception as e:
		messages.error(request, 'Hubo un error :(')
	return render(request, 'cart/cart.html', {'cart': Cart(request)})
	

@login_required
def remove_from_cart(request, product_id):
	try:
		product = Producto.objects.get(id=product_id)
		cart = Cart(request)
		cart.remove(product)
		messages.warning(request, 'Se ha eliminado con éxito!')
	except Exception as e:
		messages.error(request, 'Hubo un error :(')
	return render(request, 'cart/cart.html', {'cart': Cart(request)})


@login_required
def get_cart(request):
	return render(request, 'cart/cart.html', {'cart': Cart(request)})
	