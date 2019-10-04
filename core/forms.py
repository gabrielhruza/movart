from django.forms import ModelForm
from .models import Perfil


class PerfilForm(ModelForm):
	class Meta:
		model   = Perfil
		fields  = ['url_profile_picture', 'domicilio','telefono', 'descripcion']