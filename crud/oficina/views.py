from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Oficina
from django.urls import reverse_lazy


# Create your views here.
class OficinaListView(ListView):
    model = Oficina
    template_name = 'oficina/lista.html'
    context_object_name = 'oficinas'
    paginate_by = 10  # Número de oficinas por página

class OficinaDetailView(DetailView):
    model = Oficina
    template_name = 'oficina/detalle.html'
    context_object_name = 'oficina'

class OficinaCreateView(CreateView):
    model = Oficina
    template_name = 'oficina/crear.html'
    fields = ['nombre', 'nombre_corto']  # Ajusta los campos según tu modelo
    success_url = reverse_lazy('oficina:lista')

class OficinaUpdateView(UpdateView):
    model = Oficina
    template_name = 'oficina/crear.html'
    fields = ['nombre', 'nombre_corto']  # Ajusta los campos según tu modelo
    success_url = reverse_lazy('oficina:lista')

class OficinaDeleteView(DeleteView):
    model = Oficina
    template_name = 'oficina/eliminar.html'
    success_url = reverse_lazy('oficina:lista')