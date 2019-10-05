from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'tienda'

urlpatterns = [

	path("prod/add/", views.prodadd, name="prodadd"),

]