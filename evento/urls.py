from django.urls 	import path

from .views import (
    EventoList,
    EventoDetail,
    EventoCreation,
    EventoUpdate,
    EventoDelete
)

app_name = 'evento'

urlpatterns = [

    path('list/', EventoList.as_view(), name='list'),
    path('ver/<int:pk>/', EventoDetail.as_view(), name='detail'),
    path('add/', EventoCreation.as_view(), name='add'),
    path('edit/<int:pk>/', EventoUpdate.as_view(), name='edit'),
    path('delete/<int:pk>/', EventoDelete.as_view(), name='delete'),

]