from django.urls 	import path
from . 				import views
from .views import (DenunciaDelete)

app_name = 'denuncia'

urlpatterns = [
	path('list/', views.dlist, name='dlist'),
	path('add/<pid>', views.dadd, name='dadd'),
	path('delete/<int:pk>/', DenunciaDelete.as_view(), name='delete'),
]