from django.urls 	import path
from . 				import views


app_name = 'reputacion'

urlpatterns = [
	path('votar/<tid>/<calif>', views.votar, name='votar'),
]