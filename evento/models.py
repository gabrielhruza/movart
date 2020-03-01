import datetime
from django.conf 	import settings
from django.db 		import models
from tienda.models 	import Producto


class Evento(models.Model):
	nombre 		= models.CharField(max_length=50)
	descripcion = models.CharField(max_length=500)
	flyer		= models.CharField(max_length=500)
	inicio 		= models.DateField()
	fin 		= models.DateField()


	def __str__(self):
		return self.nombre
	
