import datetime
from django.conf    import settings
from django.db      import models
from tienda.models  import Producto, Tienda


class Transaccion(models.Model):
	cliente     = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, default=None)
	producto    = models.ForeignKey(Producto, on_delete=models.CASCADE, default=None)
	tienda      = models.ForeignKey(Tienda, on_delete=models.CASCADE, default=None)
	cantidad    = models.PositiveIntegerField(default=1)
	precio      = models.PositiveIntegerField(default=1)
	fecha       = models.DateField(default=datetime.date.today)
	estado_act 	= models.PositiveIntegerField(default=1)

	def __str__(self):
		return self.cliente.username

	def guardar(self):
		self.save()
		return self


class Movimiento(models.Model):
	ENPROGRESO  = 1
	CONFIRMADO  = 2
	RETIRAR     = 3
	RECIBIDO    = 4
	CANCELADO   = 5
	SUSPENDIDO   = 6
	ESTADO = (
		(ENPROGRESO, 'En progreso'),
		(CONFIRMADO, 'Confirmado'),
		(RETIRAR, 'Retirar'),
		(RECIBIDO, 'Recibido'),
		(CANCELADO, 'Cancelado'),
		(SUSPENDIDO, 'Suspendido'),
	)
	transaccion = models.ForeignKey(Transaccion, on_delete=models.CASCADE, default=None)    
	estado      = models.PositiveSmallIntegerField( choices=ESTADO, default=ENPROGRESO ,)
	fecha       = models.DateField(default=datetime.date.today)

	class Meta:
		ordering = ('-fecha',)
	
	def __str__(self):
		return self.get_estado_display()

	def suspender(self):
		self.estado = 6
		self.transaccion.estado_act = self.estado
		self.transaccion.guardar()
		self.save()
		return self

	def cancelar(self):
		self.estado = 5
		self.transaccion.estado_act = self.estado
		self.transaccion.guardar()
		self.save()
		return self

	def escalar(self):
		if self.estado <= 4:
			self.estado = self.estado + 1
			self.transaccion.estado_act = self.estado
			self.transaccion.guardar()			
			self.save()
		return self