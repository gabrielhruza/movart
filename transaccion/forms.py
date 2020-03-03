from django.forms import ModelForm
from django import forms

from .models import Transaccion, Movimiento


class TransaccionForm(ModelForm):
	class Meta:
		model = Transaccion
		fields = ['cantidad']


class MovimientoForm(ModelForm):
    class Meta:
        model = Movimiento
        fields = ['estado']