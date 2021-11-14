from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from .models    	import Denuncia
from .forms     	import DenunciaForm
from tienda.models  import Producto


def dlist(request):
	denuncias = Denuncia.objects.all()
	return render(request, 'denuncia/list.html', {'denuncias' : denuncias})

class DenunciaDelete(DeleteView):
    model = Denuncia
    success_url = '/'
    template_name = 'denuncia/confirm_delete.html'  

def dadd(request, pid):
	if request.method == 'POST':
		form = DenunciaForm(request.POST)
		if form.is_valid():
			try:
				producto                = Producto.objects.get(id=pid)
				denunciante             = request.user
				denuncia                = form.save(commit=False)
				denuncia.publicacion    = producto
				denuncia.denunciante    = denunciante
				denuncia.save()
				messages.success(request, 'Se ha realizado correctamente!')
				return HttpResponseRedirect('/')   
			except Exception as e:
				messages.error(request, e)         
	else:   
		form = DenunciaForm()
	return render(request, 'denuncia/add.html', {'form': form})



# def premove(request, pid):
# 	try:
# 		prod = Producto.objects.get(id=pid)
# 		fav = Favorite.objects.get_favorite(request.user, prod)
# 		fav.delete()
# 		messages.warning(request, 'Se ha eliminado de favoritos!')
# 	except Exception as e:
# 		messages.error(request, 'Ha ocurrido un error, intente de nuevo por favor')
# 	url = request.META.get('HTTP_REFERER')
# 	return redirect(url)