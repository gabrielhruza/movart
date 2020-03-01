from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

from .models    	import Reputacion
from tienda.models  import Tienda


def votar(request, tid, calif):
	try:
		reputacion = Reputacion.objects.get(tienda=tid)
	except ObjectDoesNotExist:
		try:
			tienda = Tienda.objects.get(id=tid)
		except Exception as e:
			raise e
		reputacion = Reputacion(tienda=tienda)

	reputacion.votar(calif)
	reputacion.save()
	return redirect('/')
