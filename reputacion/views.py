from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.contrib import messages

from .models    	import Calificacion
from .forms     	import CalificacionForm
from tienda.models  import Tienda


def list(request):
	calificaciones = Calificacion.objects.all()
	return render(request, 'reputacion/list.html', {'calificaciones' : calificaciones})


def calificar(request, tid):
	if request.method == 'POST':
		form = CalificacionForm(request.POST)
		if form.is_valid():
			try:
				calif 			= form.save(commit=False)
				calif.tienda    = Tienda.objects.get(id=tid)
				calif.evaluador = request.user
				calif.save()
				messages.success(request, 'Se ha realizado correctamente!')
				return HttpResponseRedirect('/')   
			except Exception as e:
				messages.error(request, e)         
	else:   
		form = CalificacionForm()
	return render(request, 'reputacion/add.html', {'form': form})

