from django.shortcuts import render
from django.views.generic import  CreateView
from.models import cadastro_de_tratamento_de_evento
from django.urls import reverse_lazy
from.forms import CadastroDeTratamentoDeEventoForm 
# Create your views here.
class cadastro_nao_conformidade(CreateView) :
    model = cadastro_de_tratamento_de_evento
    form_class = CadastroDeTratamentoDeEventoForm 
    template_name = "tratamento_de_evento_form.html"
    success_url = reverse_lazy("cadastro_de_tratamento_de_evento")

