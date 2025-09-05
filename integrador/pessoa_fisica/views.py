from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from .models import PessoaFisica
from .forms import PessoaFisicaForm


class PessoaFisicaListView(LoginRequiredMixin, ListView):
    model = PessoaFisica
    template_name = "pessoa_fisica/pessoafisica_list.html"
    context_object_name = "pessoas"
    paginate_by = 25  
    ordering = ["nome"]

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get("q") 
        if q:
            qs = qs.filter(
                Q(nome__icontains=q) |
                Q(cpf__icontains=q) |
                Q(rg__icontains=q)
            )
        return qs


class PessoaFisicaCreateView(LoginRequiredMixin, CreateView):
    model = PessoaFisica
    form_class = PessoaFisicaForm
    template_name = "pessoa_fisica/pessoafisica_form.html"
    success_url = reverse_lazy("pessoa_fisica:pf_list")

    def form_valid(self, form):
        messages.success(self.request, "Pessoa cadastrada com sucesso.")
        return super().form_valid(form)


class PessoaFisicaUpdateView(LoginRequiredMixin, UpdateView):
    model = PessoaFisica
    form_class = PessoaFisicaForm
    template_name = "pessoa_fisica/pessoafisica_form.html"
    success_url = reverse_lazy("pessoa_fisica:pf_list")

    def form_valid(self, form):
        messages.success(self.request, "Cadastro atualizado com sucesso.")
        return super().form_valid(form)


class PessoaFisicaDetailView(LoginRequiredMixin, DetailView):
    model = PessoaFisica
    template_name = "pessoa_fisica/pessoafisica_detail.html"
    context_object_name = "pessoa"


class PessoaFisicaDeleteView(LoginRequiredMixin, DeleteView):
    model = PessoaFisica
    template_name = "pessoa_fisica/pessoafisica_confirm_delete.html"
    success_url = reverse_lazy("pessoa_fisica:pf_list")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Cadastro removido com sucesso.")
        return super().delete(request, *args, **kwargs)
