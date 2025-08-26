from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from .models import Embarcador
from .forms import EmbarcadorForm


class EmbarcadorListView(LoginRequiredMixin, ListView):
    model = Embarcador
    template_name = "embarcadores/embarcador_list.html"
    context_object_name = "embarcadores"
    paginate_by = 25
    ordering = ["nome"]

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get("q")
        if q:
            qs = qs.filter(
                Q(nome__icontains=q)
                | Q(documento__icontains=q)
                | Q(razao_social__icontains=q)
            )
        return qs


class EmbarcadorCreateView(LoginRequiredMixin, CreateView):
    model = Embarcador
    form_class = EmbarcadorForm
    template_name = "embarcadores/embarcador_form.html"
    success_url = reverse_lazy("embarcadores:embarcador_list")

    def form_valid(self, form):
        messages.success(self.request, "Embarcador cadastrado com sucesso.")
        return super().form_valid(form)


class EmbarcadorUpdateView(LoginRequiredMixin, UpdateView):
    model = Embarcador
    form_class = EmbarcadorForm
    template_name = "embarcadores/embarcador_form.html"
    success_url = reverse_lazy("embarcadores:embarcador_list")

    def form_valid(self, form):
        messages.success(self.request, "Embarcador atualizado com sucesso.")
        return super().form_valid(form)


class EmbarcadorDetailView(LoginRequiredMixin, DetailView):
    model = Embarcador
    template_name = "embarcadores/embarcador_detail.html"
    context_object_name = "embarcador"


class EmbarcadorDeleteView(LoginRequiredMixin, DeleteView):
    model = Embarcador
    template_name = "embarcadores/embarcador_confirm_delete.html"
    success_url = reverse_lazy("embarcadores:embarcador_list")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Embarcador removido com sucesso.")
        return super().delete(request, *args, **kwargs)
