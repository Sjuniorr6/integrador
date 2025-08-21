from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from .models import Tecnologia
from .forms import TecnologiaForm


class TecnologiaListView(LoginRequiredMixin, ListView):
    model = Tecnologia
    template_name = "tecnologias/tecnologia_list.html"
    paginate_by = 10
    ordering = ["nome_da_conta"]
    
class TecnologiaCreateView(LoginRequiredMixin, CreateView):
    model = Tecnologia
    form_class = TecnologiaForm
    template_name = "tecnologias/tecnologia_form.html"
    success_url = reverse_lazy("lista_tecnologias")
    
    def form_valid(self, form):
        messages.success(self.request, "Integração cadastrada com sucesso.")
        return super().form_valid(form)
    
class TecnologiaUpdateView(LoginRequiredMixin, UpdateView):
    model = Tecnologia
    form_class = TecnologiaForm
    template_name = "tecnologias/tecnologia_form.html"
    success_url = reverse_lazy("lista_tecnologias")
    
    def form_valid(self, form):
        messages.success(self.request, "Integração atualizada com sucesso.")
        return super().form_valid(form)
    
class TecnologiaDetailView(LoginRequiredMixin, DetailView):
    model = Tecnologia
    template_name = "tecnologias/tecnologia_detail.html"
    object_name = "tecnologia"

class TecnologiaDeleteView(LoginRequiredMixin, DeleteView):
    model = Tecnologia
    template_name = "tecnologias/tecnologia_delete.html"
    success_url = reverse_lazy("lista_tecnologias")
    
    def form_valid(self, form):
        messages.success(self.request, "Integração deletada com sucesso.")
        return super().form_valid(form)

