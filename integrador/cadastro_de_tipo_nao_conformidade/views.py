from django.shortcuts import render
from django.views.generic import  CreateView,ListView,UpdateView
from.models import cadastro
from django.urls import reverse_lazy
from.forms import CadastroForm
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect

# Create your views here.
class cadastro_de_tipo_nao_conformidade(CreateView) :
    model = cadastro
    form_class = CadastroForm
    template_name = "tipo_nao_conformidade_form.html"
    success_url = reverse_lazy("cadastro_de_tipo_nao_conformidade")
    
class cadastro_de_tipo_nao_conformidade_list(ListView):
    model = cadastro
    form_class = CadastroForm
    template_name = "tipo_nao_conformidade_list.html"
    context_object_name = "cadastro"
    ordering = ["-id"]
    paginate_by = 10
    
class cadastro_de_tipo_nao_conformidade_update(UpdateView):
    model = cadastro
    form_class = CadastroForm
    template_name = "tipo_nao_conformidade_form.html"
    success_url = reverse_lazy("cadastro_de_tipo_nao_conformidade_list")
    
    def form_valid(self, form):
        messages.success(self.request, "Tipo de não conformidade atualizado com sucesso!")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Erro ao atualizar tipo de não conformidade. Verifique os dados.")
        return super().form_invalid(form)