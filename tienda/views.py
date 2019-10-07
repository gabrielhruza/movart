from django.shortcuts import render, redirect
from django.contrib import messages
from pinax.messages.models import Message
from .models 	import Tienda, Producto
from .forms 	import TiendaForm, ProductoForm, ProdconsForm
from .filters 	import ProductoFilter


def tiendadd(request):
	try:
		tienda = Tienda.objects.get(usuario=request.user)
	except Exception as e:
		tienda = None
	if tienda is None:
		tienda = Tienda()
		tienda.usuario = request.user
		tienda.save()
	return redirect('/')


def tiendalist(request):
	tienda_list = Tienda.objects.all()
	return render(request, 'tienda/tiendalist.html', {'tienda_list': tienda_list})


def prodver(request, id):
	producto = Producto.objects.get(id=id)
	return render(request, 'tienda/prodver.html', {'producto': producto})


def prodadd(request, url):
	if request.method == 'POST':
		form = ProductoForm(request.POST)
		if form.is_valid():
			try:
				prod = form.save(commit=False)
				prod.tienda = Tienda.objects.get(usuario=request.user)
				prod.shortcode = url
				prod.save()
				form.save_m2m()#save the many-to-many data for the form.
				messages.success(request, 'Se ha realizado con éxito!')
				return redirect('/')
			except Exception as e:
				messages.error(request, e)
				print(e)
	else:
		form = ProductoForm()
	return render(request, 'tienda/prodadd.html', {'form': form})


def prodedit(request, id):
	try:
		prod = Producto.objects.get(id=id)
	except Exception as e:
		messages.error(request, e)
	if request.method == 'POST':
		form = ProductoForm(request.POST, instance=prod)
		if form.is_valid():
			try:
				prod = form.save(commit=False)
				prod.save()
				form.save_m2m()#save the many-to-many data for the form.
				messages.success(request, 'Se ha realizado con éxito!')
				return redirect('/')
			except Exception as e:
				messages.error(request, e)
	else:
		form = ProductoForm(instance=prod)
	return render(request, 'tienda/prodadd.html', {'form': form})


#inventario de productos de por tienda
def prodlist(request, id):
	tienda = Tienda.objects.get(id=id)
	t = 'Bienvenido a ' + tienda.usuario.username
	f = ProductoFilter(request.GET, queryset=Producto.objects.filter(tienda=id))
	return render(request, 'tienda/prodlist.html', {'filter': f, 'titulo':t})	


#todos los productos de todas las tiendas
def prodlistall(request):
	t = 'Todos los productos'
	f = ProductoFilter(request.GET, queryset=Producto.objects.all())
	return render(request, 'tienda/prodlist.html', {'filter': f, 'titulo':t})


def prodcons(request, id):
	if request.method == 'POST':
		form = ProdconsForm(request.POST)
		if form.is_valid():
			try:
				prod = Producto.objects.get(id=id)
				Message.new_message(from_user=request.user, to_users=[prod.tienda.usuario],\
										subject=id, content=form.cleaned_data['contenido'])
				messages.success(request, 'Se ha realizado con éxito!')
				return redirect('/')
			except Exception as e:
				messages.error(request, e)
	else:
		form = ProdconsForm()
	return render(request, 'pinax/messages/message_create.html', {'form': form})