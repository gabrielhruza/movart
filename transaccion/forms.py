from django.forms import ModelForm
from django import forms

from .models import Transaccion


class TransaccionForm(ModelForm):
	class Meta:
		model = Transaccion
		fields = ['cantidad']