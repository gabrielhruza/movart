from django.forms import ModelForm
from django import forms

from .models import Calificacion


class CalificacionForm(ModelForm):
	class Meta:
		model = Calificacion
		fields = ['valor']
		