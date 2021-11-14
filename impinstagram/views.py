from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import secrets

@login_required
def feed(request):
	t = 'Importa tu contenido de Instagram'
	username = request.user.username		
	recent_media = []	
	for i in range(7):
		shortcode       = secrets.token_urlsafe(16)
		thumbnail_src	= str(i) + ".jpg"
		media 			= dict({'shortcode': shortcode, 'thumbnail_src':thumbnail_src})
		recent_media.append(media) 

	return render(request, 'impinstagram/impinstagram.html', {'username' : username, 'titulo': t, 'recent_media': recent_media})


