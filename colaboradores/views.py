from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Colaborador
from .forms import ColaboradorForm

class ColaboradorListView(ListView):
    model = Colaborador
    template_name = "colaboradores/colaborador_list.html"
    context_object_name = "colaboradores"
    paginate_by = 10


class ColaboradorDetailView(DetailView):
    model = Colaborador
    template_name = "colaboradores/colaborador_detail.html"
    context_object_name = "colaborador"


class ColaboradorCreateView(CreateView):
    model = Colaborador
    form_class = ColaboradorForm
    template_name = "colaboradores/colaborador_form.html"
    success_url = reverse_lazy("colaboradores:listar")


class ColaboradorUpdateView(UpdateView):
    model = Colaborador
    form_class = ColaboradorForm
    template_name = "colaboradores/colaborador_form.html"
    success_url = reverse_lazy("colaboradores:listar")


class ColaboradorDeleteView(DeleteView):
    model = Colaborador
    template_name = "colaboradores/colaborador_confirm_delete.html"
    success_url = reverse_lazy("colaboradores:listar")

# Create your views here.
