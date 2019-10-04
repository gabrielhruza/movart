from django.shortcuts import render
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
	if request.method == 'POST':
		form = PerfilForm(request.POST)
		if form.is_valid():
			pass  # does nothing, just trigger the validation
	else:
		form = PerfilForm()
	return render(request, 'core/perfiled.html', {'form': form})