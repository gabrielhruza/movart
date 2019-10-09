from django.shortcuts import render, redirect
from fav.models import Favorite
from tienda.models import Producto


def list(request):
	favs = Favorite.objects.for_user(request.user, model=Producto)
	return render(request, 'favs/list.html', {'favs' : favs})


def add(request, pid):
	prod = Producto.objects.get(id=pid)
	fav = Favorite.objects.create(request.user, prod)
	fav.save()
	return redirect('favs:list')

def remove(request, pid):
	prod = Producto.objects.get(id=pid)
	fav = Favorite.objects.get_favorite(request.user, prod)
	fav.delete()
	return redirect('favs:list')
