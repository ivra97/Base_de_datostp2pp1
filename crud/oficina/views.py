from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Oficina
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


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

class OficinaCreateView(LoginRequiredMixin, CreateView):
    model = Oficina
    template_name = 'oficina/crear.html'
    fields = ['nombre', 'nombre_corto']  # Ajusta los campos según tu modelo
    success_url = reverse_lazy('oficina:lista')

class OficinaUpdateView(LoginRequiredMixin, UpdateView):
    model = Oficina
    template_name = 'oficina/crear.html'
    fields = ['nombre', 'nombre_corto']  # Ajusta los campos según tu modelo
    success_url = reverse_lazy('oficina:lista')

class OficinaDeleteView(LoginRequiredMixin, DeleteView):
    model = Oficina
    template_name = 'oficina/eliminar.html'
    success_url = reverse_lazy('oficina:lista')

class OficinaSearchView(ListView):
    model = Oficina
    template_name = 'oficina/buscar.html'
    context_object_name = 'oficinas'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if not query:
            return self.model.objects.none()
        return Oficina.objects.filter(
            Q(nombre__icontains=query) | Q(nombre_corto__icontains=query)
        )