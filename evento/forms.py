from django.forms import ModelForm
from django import forms

from .models import Evento


class EventoForm(ModelForm):
	class Meta:
		model  = Evento
		fields = '__all__'
		widgets = {
            'inicio': forms.DateInput(attrs={'type': 'date'}),
			'fin': forms.DateInput(attrs={'type': 'date'})
		}
