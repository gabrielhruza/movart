from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests



def home(request):
    return render(request, 'core/home.html')

def login(request):
    return render(request, 'core/login.html')

def privacy(request):
	return render(request, 'core/login.html')


def ig(request):
	#obtengo las imagenes publicas del usuario del parametro
	url = 'https://www.instagram.com/gabi/?__a=1'
	response = requests.get(url)
	response_json = response.json()
	print(response_json)
	return render(request, 'core/login.html')