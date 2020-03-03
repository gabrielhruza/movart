import datetime
from django.conf 	import settings
from django.db 		import models
from tienda.models 	import Producto, Tienda


class Transaccion(models.Model):
	cliente     = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, default=None)
	producto    = models.ForeignKey(Producto, on_delete=models.CASCADE, default=None)
	tienda      = models.ForeignKey(Tienda, on_delete=models.CASCADE, default=None)
	cantidad    = models.PositiveIntegerField(default=1)
	precio      = models.PositiveIntegerField(default=1)
	fecha 		= models.DateField(default=datetime.date.today)


	def __str__(self):
		return self.cliente.username


class Movimiento(models.Model):
	LISTO 		= 1
	CONFIRMADO 	= 2
	ENVIADO 	= 3
	RECIBIDO 	= 4
	CANCELADO	= 5
	SUSPENDIDO   = 6
	ESTADO = (
		(LISTO, 'Listo'),
		(CONFIRMADO, 'Cofirmado'),
		(ENVIADO, 'Enviado'),
		(RECIBIDO, 'Recibido'),
		(CANCELADO, 'Cancelado'),
		(SUSPENDIDO, 'Suspendido'),
	)
	transaccion = models.ForeignKey(Transaccion, on_delete=models.CASCADE, default=None) 	
	estado 		= models.PositiveSmallIntegerField( choices=ESTADO, default=LISTO ,)
	fecha 		= models.DateField(default=datetime.date.today)

	
	def __str__(self):
		return self.get_estado_display()

	def suspender(self):
		self.estado = 6
		return self

	def cancelar(self):
		self.estado = 5
		return self

	def escalar(self):
		if self.estado <= 4:
			self.estado += 1
		return self