from django.shortcuts import render
from django.views.generic import  CreateView
from.models import cadastro
from django.urls import reverse_lazy
from.forms import CadastroForm
# Create your views here.
class cadastro_de_tipo_nao_conformidade(CreateView) :
    model = cadastro
    form_class = CadastroForm
    template_name = "tipo_nao_conformidade_form.html"
    success_url = reverse_lazy("cadastro_de_tipo_nao_conformidade")