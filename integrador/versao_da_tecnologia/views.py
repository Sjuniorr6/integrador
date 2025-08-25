from django.shortcuts import render
from django.views.generic import  CreateView
from.models import cadastrotecnologia
from django.urls import reverse_lazy
from.forms import CadastroTecnologiaForm
# Create your views here.
class VersaoDaTecnologiaCreateView (CreateView) :
    model = cadastrotecnologia
    form_class = CadastroTecnologiaForm
    template_name = "versaotecnologia_form.html"
    success_url = reverse_lazy("versao_da_tecnologia")