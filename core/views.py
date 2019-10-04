from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Perfil


def home(request):
    return render(request, 'core/home.html')

def login(request):
    return render(request, 'core/login.html')

def privacy(request):
	return render(request, 'core/privacy.html')


def actualizar_perfil(request):
	pass
	# try:
	# 	perfil = Perfil.objects.get(usuario=request.user)
	# except Exception as e:
	# 	perfil = Perfil()


	# if request.method == 'POST':
 #        form = ContactForm(request.POST)
 #        if form.is_valid():
 #            pass  # does nothing, just trigger the validation
 #    else:
 #        form = ContactForm()
 #    return render(request, 'home.html', {'form': form})