from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models    	import Evento
from .forms     	import EventoForm


class EventoList(ListView):
    model = Evento
    template_name = 'evento/list.html'    


class EventoDetail(DetailView):
    model = Evento
    template_name = 'evento/detail.html'    


class EventoCreation(CreateView):
    model = Evento
    success_url = reverse_lazy('evento:list')
    fields = ['nombre', 'inicio', 'fin','descripcion','flyer']
    template_name = 'evento/add.html'


class EventoUpdate(UpdateView):
    model = Evento
    success_url = reverse_lazy('evento:list')
    fields = ['nombre', 'inicio', 'fin','descripcion','flyer']
    template_name = 'evento/add.html'    


class EventoDelete(DeleteView):
    model = Evento
    success_url = reverse_lazy('evento:list')
    template_name = 'evento/confirm_delete.html'    
    