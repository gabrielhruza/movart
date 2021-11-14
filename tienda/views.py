from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from pinax.messages.models import Message
from core.models import Perfil
from reputacion.models import Reputacion
from .models 	import Tienda, Producto, Imagen
from .forms 	import TiendaForm, ProductoForm, ProdconsForm
from .filters 	import ProductoFilter


@login_required
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


def tiendaver(request, tid):
	try:
		tienda = Tienda.objects.get(id=tid)
		perfil = Perfil.objects.get(usuario=tienda.usuario)
		reputacion = Reputacion.objects.get(tienda=tienda)
	except Exception as e:
		messages.error(request, e)
		return redirect('/')
	return render(request, 'tienda/tiendaver.html', {'perfil': perfil, 'reputacion': reputacion})


def prodver(request, pid):
	producto = Producto.objects.get(id=pid)
	producto.visita()
	return render(request, 'tienda/prodver.html', {'producto': producto})


@login_required
def prodadd(request, url, img):
	if request.method == 'POST':
		form = ProductoForm(request.POST)
		if form.is_valid():
			try:
				prod = form.save(commit=False)
				prod.tienda = Tienda.objects.get(usuario=request.user)
				prod.shortcode = url
				prod.save()
				form.save_m2m()#save the many-to-many data for the form.
				imagen = Imagen()
				imagen.url = img
				imagen.producto = prod
				imagen.save()
				messages.success(request, 'Se ha realizado con éxito!')
				return redirect('/')
			except Exception as e:
				messages.error(request, e)
	else:
		form = ProductoForm()
	return render(request, 'tienda/prodadd.html', {'form': form, 'url':url, 'img':img})


@login_required
def prodedit(request, pid):
	try:
		prod = Producto.objects.get(id=pid)
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


#inventario de productos por tienda
def prodlist(request, tid):
	tienda = Tienda.objects.get(id=tid)
	t = 'Bienvenido a ' + tienda.usuario.username
	f = ProductoFilter(request.GET, queryset=Producto.objects.filter(tienda=tid))
	return render(request, 'tienda/prodlist.html', {'filter':f, 'titulo':t, 'tid':tid})	


#todos los productos de todas las tiendas
def prodlistall(request):
	t = 'Todos los productos'
	f = ProductoFilter(request.GET, queryset=Producto.objects.all())
	return render(request, 'tienda/prodlist.html', {'filter': f, 'titulo':t})


@login_required
def prodcons(request, pid):
	if request.method == 'POST':
		form = ProdconsForm(request.POST)
		if form.is_valid():
			try:
				prod = Producto.objects.get(id=pid)
				Message.new_message(from_user=request.user, to_users=[prod.tienda.usuario],\
										subject=pid, content=form.cleaned_data['contenido'])
				messages.success(request, 'Se ha realizado con éxito!')
				return redirect('/')
			except Exception as e:
				messages.error(request, e)
	else:
		form = ProdconsForm()
	return render(request, 'pinax/messages/message_create.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class ProductoDeleteView(DeleteView):
    model = Producto
    success_url = '/'