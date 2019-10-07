import django_filters

from .models import Producto 


class ProductoFilter(django_filters.FilterSet):
    nombre 		= django_filters.CharFilter(lookup_expr='icontains')       
    etiquetas	= django_filters.CharFilter(lookup_expr='name__icontains')       
    class Meta:
        model 	= Producto
        fields = ['nombre', 'precio', 'etiquetas']