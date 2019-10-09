from django.shortcuts import render, redirect
from django.contrib import messages
from fav.models import Favorite
from tienda.models import Tienda, Producto


def plist(request):
	favs = Favorite.objects.for_user(request.user, model=Producto)
	return render(request, 'favs/plist.html', {'favs' : favs})


def padd(request, pid):
	try:
		prod = Producto.objects.get(id=pid)
		fav = Favorite.objects.create(request.user, prod)
		fav.save()
		messages.success(request, 'Se ha agregado a favoritos!')
	except Exception as e:
		messages.error(request, 'Ha ocurrido un error, intente de nuevo por favor')
	url = request.META.get('HTTP_REFERER')
	return redirect(url)


def premove(request, pid):
	try:
		prod = Producto.objects.get(id=pid)
		fav = Favorite.objects.get_favorite(request.user, prod)
		fav.delete()
		messages.warning(request, 'Se ha eliminado de favoritos!')
	except Exception as e:
		messages.error(request, 'Ha ocurrido un error, intente de nuevo por favor')
	url = request.META.get('HTTP_REFERER')
	return redirect(url)


def tlist(request):
	favs = Favorite.objects.for_user(request.user, model=Tienda)
	return render(request, 'favs/tlist.html', {'favs' : favs})


def tadd(request, tid):
	try:
		tienda = Tienda.objects.get(id=tid)
		fav = Favorite.objects.create(request.user, tienda)
		fav.save()
		messages.success(request, 'Se ha agregado a favoritos!')
	except Exception as e:
		messages.error(request, 'Ha ocurrido un error, intente de nuevo por favor')
	url = request.META.get('HTTP_REFERER')
	return redirect(url)


def tremove(request, tid):
	try:
		tienda = Tienda.objects.get(id=tid)
		fav = Favorite.objects.get_favorite(request.user, tienda)
		fav.delete()
		messages.warning(request, 'Se ha eliminado de favoritos!')
	except Exception as e:
		messages.error(request, 'Ha ocurrido un error, intente de nuevo por favor')
	url = request.META.get('HTTP_REFERER')
	return redirect(url)
