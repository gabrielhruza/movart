import datetime
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.conf 	import settings
from django.db 		import models
from tienda.models 	import Tienda


class Calificacion(models.Model):
	evaluador 	= models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, default=None)
	tienda 		= models.ForeignKey(Tienda, on_delete=models.CASCADE)
	valor 		= models.PositiveIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])


	def __str__(self):
		return self.valor
	
