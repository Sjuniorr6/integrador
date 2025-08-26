from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Cliente, EntradaIscas
from .forms import ClienteForm, EntradaIscasForm


class EntradaIscasCreateView(CreateView):
    model = EntradaIscas
    form_class = EntradaIscasForm
    template_name = "entradas/entrada_iscas_form.html"
    success_url = reverse_lazy("entradas:entrada_list")  


class EntradaIscasListView(ListView):
    model = EntradaIscas
    template_name = "entradas/entrada_iscas_list.html"
    context_object_name = "entradas"
    ordering = ["-id"]          
    paginate_by = 25           


class EntradaIscasUpdateView(UpdateView):
    model = EntradaIscas
    form_class = EntradaIscasForm
    template_name = "entradas/entrada_iscas_form.html"
    success_url = reverse_lazy("entradas:entrada_list")


class EntradaIscasDeleteView(DeleteView):
    model = EntradaIscas
    template_name = "entradas/entrada_iscas_confirm_delete.html"
    success_url = reverse_lazy("entradas:entrada_list")


class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "clientes/cliente_form.html"
    success_url = reverse_lazy("entradas:entrada_create")  


class ClienteListView(ListView):
    model = Cliente
    template_name = "clientes/cliente_list.html"
    context_object_name = "clientes"
    ordering = ["nome"]