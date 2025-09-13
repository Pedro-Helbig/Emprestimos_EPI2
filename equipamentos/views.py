from django.shortcuts import render
# equipamentos/views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from colaboradores.models import Equipamento
from .forms import EquipamentoForm

# LIST
class EquipamentoListView(ListView):
    model = Equipamento
    template_name = 'equipamentos/equipamento_list.html'
    context_object_name = 'equipamentos'
    ordering = ['nome']

# DETAIL
class EquipamentoDetailView(DetailView):
    model = Equipamento
    template_name = 'equipamentos/equipamento_detail.html'
    context_object_name = 'equipamento'

# CREATE
class EquipamentoCreateView(CreateView):
    model = Equipamento
    form_class = EquipamentoForm
    template_name = 'equipamentos/equipamento_form.html'
    success_url = reverse_lazy('equipamento_list')

# UPDATE
class EquipamentoUpdateView(UpdateView):
    model = Equipamento
    form_class = EquipamentoForm
    template_name = 'equipamentos/equipamento_form.html'
    success_url = reverse_lazy('equipamento_list')

# DELETE
class EquipamentoDeleteView(DeleteView):
    model = Equipamento
    template_name = 'equipamentos/equipamento_confirm_delete.html'
    success_url = reverse_lazy('equipamento_list')