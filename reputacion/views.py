from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
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
	try: 	
		reputacion.votar(calif)
		reputacion.save()
		messages.success(request, 'Se ha realizado con éxito!')
	except Exception as e:
		messages.error(request, e)
	url = request.META.get('HTTP_REFERER')
	return redirect(url)

