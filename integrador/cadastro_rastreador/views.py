from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from .models import Rastreador
from .forms import RastreadorForm


class RastreadorListView(LoginRequiredMixin, ListView):
    model = Rastreador
    template_name = "cadastro_rastreador/rastreador_list.html"
    context_object_name = "rastreadores"
    paginate_by = 25
    ordering = ["nome"]

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get("q")
        if q:
            qs = qs.filter(
                Q(nome__icontains=q)
                | Q(id_dispositivo__icontains=q)
                | Q(versao_tecnologia__icontains=q)
                | Q(conta_tecnologia__icontains=q)
            )
        return qs


class RastreadorCreateView(LoginRequiredMixin, CreateView):
    model = Rastreador
    form_class = RastreadorForm
    template_name = "cadastro_rastreador/rastreador_form.html"
    success_url = reverse_lazy("cadastro_rastreador:list")

    def form_valid(self, form):
        messages.success(self.request, "Rastreador cadastrado com sucesso.")
        return super().form_valid(form)


class RastreadorUpdateView(LoginRequiredMixin, UpdateView):
    model = Rastreador
    form_class = RastreadorForm
    template_name = "cadastro_rastreador/rastreador_form.html"
    success_url = reverse_lazy("cadastro_rastreador:list")

    def form_valid(self, form):
        messages.success(self.request, "Rastreador atualizado com sucesso.")
        return super().form_valid(form)


class RastreadorDetailView(LoginRequiredMixin, DetailView):
    model = Rastreador
    template_name = "cadastro_rastreador/rastreador_detail.html"
    context_object_name = "rastreador"


class RastreadorDeleteView(LoginRequiredMixin, DeleteView):
    model = Rastreador
    template_name = "cadastro_rastreador/rastreador_confirm_delete.html"
    success_url = reverse_lazy("cadastro_rastreador:list")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Rastreador removido com sucesso.")
        return super().delete(request, *args, **kwargs)
