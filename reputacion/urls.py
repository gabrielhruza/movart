from django.urls 	import path
from . 				import views


app_name = 'denuncia'

urlpatterns = [
	path('list/', views.dlist, name='dlist'),
	path('add/<pid>', views.dadd, name='dadd'),
]