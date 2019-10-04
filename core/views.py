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
	return render(request, 'core/ig.html')