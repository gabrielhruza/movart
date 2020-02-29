from django.urls 	import path
from . 				import views


app_name = 'denuncia'

urlpatterns = [
	path('list/', views.dlist, name='denuncia_list'),
	path('add/<pid>', views.dadd, name='denuncia_add'),
]