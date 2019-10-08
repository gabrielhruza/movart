from django.shortcuts import render
from .cart import Cart
from tienda.models import Producto


def add_to_cart(request, product_id, quantity):
	product = Producto.objects.get(id=product_id)
	cart = Cart(request)
	cart.add(product, product.precio, quantity)
	return render(request, 'cart/cart.html', {'cart': Cart(request)})
	

def remove_from_cart(request, product_id):
	product = Producto.objects.get(id=product_id)
	cart = Cart(request)
	cart.remove(product)
	return render(request, 'cart/cart.html', {'cart': Cart(request)})


def get_cart(request):
	return render(request, 'cart/cart.html', {'cart': Cart(request)})
	