from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models 		import Transaccion, Movimiento
from .forms 		import TransaccionForm
from tienda.models  import Producto, Tienda


@login_required
def compras(request):
	try:
		ts = Transaccion.objects.filter(cliente=request.user)
	except Exception as e:
		messages.error(request, e)
		ts = {} 		
	return render(request, 'transaccion/compras.html', {'ts' : ts})


@login_required
def ventas(request):
	try:
		tienda = Tienda.objects.get(usuario=request.user)
		ts = Transaccion.objects.filter(tienda=tienda).exclude(estado_act=1)
	except Exception as e:
		messages.error(request, e)
		ts = {} 			
	return render(request, 'transaccion/ventas.html', {'ts' : ts})


@login_required
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
		mov = Movimiento(transaccion=t)
		mov.save()
		messages.success(request, 'Se ha realizado correctamente!')
		return HttpResponseRedirect('/transaccion/compras')   
	except Exception as e:
		messages.error(request, e)         
	return HttpResponseRedirect('/transaccion/compras')



@login_required
def tracking(request, trid):
	try:
		movs = Movimiento.objects.filter(transaccion=trid)
	except Exception as e:
		messages.error(request, e) 
	return render(request, 'transaccion/tracking.html', {'movs' : movs})


@login_required
def cancelar(request, trid):
	try:
		tr 	= Transaccion.objects.get(id=trid)
		mov = Movimiento(transaccion=tr)
		mov.cancelar()
	except Exception as e:
		messages.error(request, e) 
	return HttpResponseRedirect('/transaccion/compras')	


@login_required
def suspender(request, trid):
	try:
		tr 	= Transaccion.objects.get(id=trid)
		mov = Movimiento(transaccion=tr)
		mov.suspender()
	except Exception as e:
		messages.error(request, e) 
	return HttpResponseRedirect('/transaccion/compras')	


@login_required
def confirmar(request, trid):
	try:
		tr 	= Transaccion.objects.get(id=trid)
		mov = Movimiento(transaccion=tr)
		mov.escalar()
	except Exception as e:
		messages.error(request, e) 
	return HttpResponseRedirect('/transaccion/compras')	