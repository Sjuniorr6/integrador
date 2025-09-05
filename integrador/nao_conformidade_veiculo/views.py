# nao_conformidade_veiculo/views.py
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from .models import NaoConformidadeVeiculo
from .forms import NaoConformidadeVeiculoForm


class NaoConformidadeVeiculoListView(LoginRequiredMixin, ListView):
    model = NaoConformidadeVeiculo
    template_name = "nao_conformidade_veiculo/ncv_list.html"
    context_object_name = "itens"
    paginate_by = 25
    ordering = ["-suspenso_desde", "cliente"]

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get("q")
        if q:
            qs = qs.filter(
                Q(cliente__icontains=q) |
                Q(veiculo__icontains=q) |
                Q(viagem__icontains=q) |
                Q(frota__icontains=q) |
                Q(transportador__icontains=q) |
                Q(situacao__icontains=q)
            )
        return qs


class NaoConformidadeVeiculoCreateView(LoginRequiredMixin, CreateView):
    model = NaoConformidadeVeiculo
    form_class = NaoConformidadeVeiculoForm
    template_name = "nao_conformidade_veiculo/ncv_form.html"
    success_url = reverse_lazy("nao_conformidade_veiculo:ncv_list")

    def form_valid(self, form):
        messages.success(self.request, "Não conformidade cadastrada com sucesso.")
        return super().form_valid(form)


class NaoConformidadeVeiculoUpdateView(LoginRequiredMixin, UpdateView):
    model = NaoConformidadeVeiculo
    form_class = NaoConformidadeVeiculoForm
    template_name = "nao_conformidade_veiculo/ncv_form.html"
    success_url = reverse_lazy("nao_conformidade_veiculo:ncv_list")

    def form_valid(self, form):
        messages.success(self.request, "Cadastro atualizado com sucesso.")
        return super().form_valid(form)


class NaoConformidadeVeiculoDetailView(LoginRequiredMixin, DetailView):
    model = NaoConformidadeVeiculo
    template_name = "nao_conformidade_veiculo/ncv_detail.html"
    context_object_name = "item"


class NaoConformidadeVeiculoDeleteView(LoginRequiredMixin, DeleteView):
    model = NaoConformidadeVeiculo
    template_name = "nao_conformidade_veiculo/ncv_confirm_delete.html"
    success_url = reverse_lazy("nao_conformidade_veiculo:ncv_list")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Cadastro removido com sucesso.")
        return super().delete(request, *args, **kwargs)
