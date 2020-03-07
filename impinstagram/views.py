from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def feed(request):
	t = 'Importa tu contenido de Instagram'
	username = request.user.username			
	return render(request, 'impinstagram/impinstagram.html', {'username' : username, 'titulo': t})


