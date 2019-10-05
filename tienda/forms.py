from django.forms import ModelForm
from django import forms

from .models import Tienda, Producto


class TiendaForm(ModelForm):
	class Meta:
		model = Tienda
		fields = ['estado']


class ProductoForm(ModelForm):
	class Meta:
		model = Producto
		fields = ['nombre', 'precio', 'etiquetas', 'descripcion']


class ProdconsForm(forms.Form):
	contenido = forms.CharField(label='Contenido', widget=forms.Textarea)