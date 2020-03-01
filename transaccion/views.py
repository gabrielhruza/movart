from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models 		import Transaccion
from .forms 		import TransaccionForm
from tienda.models  import Producto, Tienda



def compras(request):
	try:
		ts = Transaccion.objects.filter(cliente=request.user)
	except Exception as e:
		messages.error(request, e)
		ts = {} 		
	return render(request, 'transaccion/compras.html', {'ts' : ts})


def ventas(request):
	try:
		tienda = Tienda.objects.get(usuario=request.user)
		ts = Transaccion.objects.filter(tienda=tienda)
	except Exception as e:
		messages.error(request, e)
		ts = {} 			
	return render(request, 'transaccion/ventas.html', {'ts' : ts})


def add(request, pid, q):
	try:
		producto 	= Producto.objects.get(id=pid)
		tienda 		= producto.tienda
		cliente     = request.user
		t           = Transaccion(cliente=request.user, 
										producto=producto, 
										tienda=producto.tienda,
										precio=producto.precio,
										cantidad = q )
		t.save()
		messages.success(request, 'Se ha realizado correctamente!')
		return HttpResponseRedirect('/transaccion/compras')   
	except Exception as e:
		messages.error(request, e)         
	return HttpResponseRedirect('/transaccion/compras')