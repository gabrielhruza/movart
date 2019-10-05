from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager


class Tienda(models.Model):
    usuario     = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=None) 
    estado      = models.PositiveIntegerField(default=1)

    def catalogo(self):
        return self.producto_set


class Producto(models.Model):
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    nombre 	     = models.CharField(max_length=100)
    descripcion  = models.CharField(max_length=500)
    shortcode    = models.CharField(max_length=100)
    precio       = models.PositiveIntegerField()
    etiquetas    = TaggableManager()
    album        = models.BooleanField(default=False)

    class Meta:
        unique_together = ('tienda', 'shortcode')


class Imagen(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    url = models.CharField(max_length=300)