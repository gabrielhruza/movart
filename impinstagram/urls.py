from django.urls import path
from . import views

app_name = 'impinstagram'

urlpatterns = [
	path("feed/", views.feed, name="feed"),
]