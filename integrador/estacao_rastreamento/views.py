from django.shortcuts import render
from django.views.generic import  CreateView
from.models import EstacaoRastreamento
from django.urls import reverse_lazy
from.forms import EstacaoRastreamentoForm
# Create your views here.
class estacao_rastreamento (CreateView) :
    model = EstacaoRastreamento
    form_class = EstacaoRastreamentoForm
    template_name = "estrastreamento_form.html"
    success_url = reverse_lazy("estacao_rastreamento")
    