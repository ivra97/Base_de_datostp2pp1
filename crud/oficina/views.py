from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Oficina
from django.urls import reverse_lazy


# Create your views here.
class OficinaListView(ListView):
    model = Oficina
    template_name = 'oficina/oficina_list.html'
    context_object_name = 'oficinas'

class OficinaDetailView(DetailView):
    model = Oficina
    template_name = 'oficina/oficina_detail.html'
    context_object_name = 'oficina'

class OficinaCreateView(CreateView):
    model = Oficina
    template_name = 'oficina/oficina_form.html'
    context_object_name = 'oficina'
    success_url = reverse_lazy('oficina:lista')

class OficinaUpdateView(UpdateView):
    model = Oficina
    template_name = 'oficina/oficina_form.html'
    context_object_name = 'oficina'
    success_url = reverse_lazy('oficina:lista')

class OficinaDeleteView(DeleteView):
    model = Oficina
    template_name = 'oficina/oficina_confirm_delete.html'
    context_object_name = 'oficina'
    success_url = reverse_lazy('oficina:lista')