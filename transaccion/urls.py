from django.urls 	import path
from . 				import views


app_name = 'transaccion'

urlpatterns = [
	path('compras/', views.compras, name='compras'),
	path('ventas/', views.ventas, name='ventas'),
	path('add/<pid>/<q>/', views.add, name='add'),
	#path('rem/<pid>/<q>/', views.rem, name='rem'),
]