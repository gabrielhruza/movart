from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'favs'

urlpatterns = [
	
	path("list/", views.list, name="list"),
	path("<pid>/add/", views.add, name="add"),
	path("<pid>/remove/", views.remove, name="remove"),

]