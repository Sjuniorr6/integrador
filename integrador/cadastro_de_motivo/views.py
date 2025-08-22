from django.shortcuts import render
from django.views.generic import  CreateView
from.models import CadastroDeMotivo
from django.urls import reverse_lazy
from.forms import CadastroDeMotivoForm
# Create your views here.
class motivo (CreateView):
    model = CadastroDeMotivo
    form_class = CadastroDeMotivoForm
    tamplate_name = "Motivo_form.html"
    sucess_url = reverse_lazy("CadastroDeMotivo")