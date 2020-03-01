import datetime
from django.conf 	import settings
from django.db 		import models
from tienda.models 	import Tienda


class Reputacion(models.Model):
	tienda 		= models.ForeignKey(Tienda, on_delete=models.CASCADE)
	valor5 		= models.PositiveIntegerField(default=0)
	valor4 		= models.PositiveIntegerField(default=0)
	valor3 		= models.PositiveIntegerField(default=0)
	valor2 		= models.PositiveIntegerField(default=0)
	valor1 		= models.PositiveIntegerField(default=0)
	votos 		= models.PositiveIntegerField(default=0)

	def __str__(self):
		return "Alta reputacion"
	
	def votar(self, voto):
		if voto == 5: self.valor5 += 1
		if voto == 4: self.valor4 += 1
		if voto == 3: self.valor3 += 1
		if voto == 2: self.valor2 += 1
		if voto == 1: self.valor1 += 1
		self.votos += 1
