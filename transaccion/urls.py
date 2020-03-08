from django.urls 	import path
from . 				import views


app_name = 'transaccion'

urlpatterns = [
	path('compras/', views.compras, name='compras'),
	path('ventas/', views.ventas, name='ventas'),
	path('add/<pid>/<q>/', views.add, name='add'),
	path('tracking/<trid>/', views.tracking, name='tracking'),
	path('cancelar/<trid>/', views.cancelar, name='cancelar'),
	path('suspender/<trid>/', views.suspender, name='suspender'),
	path('confirmar/<trid>/', views.confirmar, name='confirmar'),
	#path('rem/<pid>/<q>/', views.rem, name='rem'),
]
