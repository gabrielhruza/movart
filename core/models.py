from django.db import models
from django.conf import settings

# Create your models here.

class Perfil(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    url_profile_picture = models.CharField(max_length=500, default=None)
    domicilio 	= models.CharField(max_length=100, default=None, null=True)
    descripcion = models.CharField(max_length=250, default=None, null=True)
    telefono    = models.CharField(max_length=50, default=None, null=True) 