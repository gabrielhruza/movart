from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Perfil
from .forms  import PerfilForm       


def home(request):
	return render(request, 'core/home.html')

def login(request):
	return render(request, 'core/login.html')

def privacy(request):
	return render(request, 'core/privacy.html')


# Luego de realizarse correctamente el registro del nuevo usuario,
# creamos y asignamos un Perfil con los datos personales
def verificar_perfil(request):
	if request.user is not None:
		try:
			perfil = Perfil.objects.get(usuario=request.user)
		except Exception as e:
			perfil = None
		#si el perfil no existe es porque es un usuario nuevo
		if perfil is None:
			perfil = Perfil()
			perfil.usuario = request.user
			perfil.url_profile_picture = 'https://images-na.ssl-images-amazon.com/images/I/51XYolCzVKL._SL1200_.jpg'
			try:
				perfil.save()
			except Exception as e:
				raise e
	return render(request, 'core/home.html')


def actualizar_perfil(request):
	try:
		perfil = Perfil.objects.get(usuario=request.user)
	except Exception as e:
		messages.error(request, e)

	if request.method == 'POST':
		form = PerfilForm(request.POST,instance=perfil)
		if form.is_valid():
			try:
				form.save()
				messages.success(request, 'Se ha realizado con éxito!')
				return redirect('/')
			except Exception as e:
				messages.error(request, e)
			
	else:
		form = PerfilForm(instance=perfil)
	return render(request, 'core/perfiled.html', {'form': form})


def ver_perfil(request):
	try:
		perfil = Perfil.objects.get(usuario=request.user)
	except Exception as e:
		messages.error(request, e)
		return redirect('/')
	return render(request, 'core/perfilver.html', {'perfil': perfil})
	
