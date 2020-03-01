import datetime
from django.conf 	import settings
from django.db 		import models
from tienda.models 	import Tienda


class Reputacion(models.Model):
	tienda 		= models.ForeignKey(Tienda, on_delete=models.CASCADE)
	valor5 		= models.PositiveIntegerField(default=1)
	valor4 		= models.PositiveIntegerField(default=0)
	valor3 		= models.PositiveIntegerField(default=0)
	valor2 		= models.PositiveIntegerField(default=0)
	valor1 		= models.PositiveIntegerField(default=0)
	votos 		= models.PositiveIntegerField(default=1)

	def __str__(self):
		return "Alta reputacion"
	
	def votar(self, voto):
		if voto == '5': self.valor5 += 1
		if voto == '4': self.valor4 += 1
		if voto == '3': self.valor3 += 1
		if voto == '2': self.valor2 += 1
		if voto == '1': self.valor1 += 1
		self.votos += 1

	def califs(self):
		c5p = round((self.valor5 / self.votos)*100)
		c4p = round((self.valor4 / self.votos)*100)
		c3p = round((self.valor3 / self.votos)*100)
		c2p = round((self.valor2 / self.votos)*100)
		c1p = round((self.valor1 / self.votos)*100)
		suma = self.valor5*5 + self.valor4*4 + self.valor3*3 + self.valor2*2 + self.valor1*1		
		prom = round((suma / self.votos),1)
		califs = {"c5p": c5p, "c4p": c4p, "c3p": c3p, "c2p": c2p, "c1p": c1p, "prom": prom}
		return califs

	def reiniciar(self):
		self.valor5, self.valor4, self.valor3, self.valor2, self.valor1 = 0
		self.votos = 1