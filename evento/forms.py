from django.forms import ModelForm
from django import forms

from .models import Evento


class EventoForm(ModelForm):
	class Meta:
		model = Evento
		fields = ['nombre', 'inicio', 'fin', 'descripcion', 'flyer']
		