import datetime
from django.conf 	import settings
from django.db 		import models
from tienda.models 	import Producto


class Denuncia(models.Model):
	denunciante = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, default=None)
	publicacion = models.ForeignKey(Producto, on_delete=models.CASCADE)
	descripcion = models.CharField(max_length=500)
	fecha 		= models.DateField(default=datetime.date.today)


	def __str__(self):
		return self.publicacion.nombre
	
