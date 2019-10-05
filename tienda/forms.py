from django.forms import ModelForm
from django import forms

from .models import Producto


class ProductoForm(ModelForm):
	class Meta:
		model = Producto
		fields = ['nombre', 'precio', 'etiquetas', 'descripcion']