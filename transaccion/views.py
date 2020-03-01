from django.shortcuts import render
from django.contrib import messages
from .models 		import Transaccion
from tienda.models  import Producto



def compras(request):
	t = Transaccion.objects.get(usuario=request.user)
	return render(request, 'transaccion/list.html', {'t' : t})


def ventas(request):
	t = Transaccion.objects.get(usuario=request.user)
	return render(request, 'transaccion/list.html', {'t' : t})