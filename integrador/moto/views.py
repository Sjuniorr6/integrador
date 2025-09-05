from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from .models import Moto
from .forms import MotoForm


class MotoListView(LoginRequiredMixin, ListView):
    model = Moto
    template_name = "moto/moto_list.html"
    context_object_name = "motos"
    paginate_by = 25
    ordering = ["placa"]

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get("q")
        if q:
            qs = qs.filter(
                Q(placa__icontains=q) |
                Q(modelo__icontains=q) |
                Q(renavam__icontains=q) |
                Q(proprietario_posse__icontains=q)
            )
        status = self.request.GET.get("status")
        if status in dict(Moto.Status.choices):
            qs = qs.filter(status=status)
        return qs


class MotoCreateView(LoginRequiredMixin, CreateView):
    model = Moto
    form_class = MotoForm
    template_name = "moto/moto_form.html"
    success_url = reverse_lazy("moto:moto_list")

    def form_valid(self, form):
        messages.success(self.request, "Moto cadastrada com sucesso.")
        return super().form_valid(form)


class MotoUpdateView(LoginRequiredMixin, UpdateView):
    model = Moto
    form_class = MotoForm
    template_name = "moto/moto_form.html"
    success_url = reverse_lazy("moto:moto_list")

    def form_valid(self, form):
        messages.success(self.request, "Cadastro de moto atualizado com sucesso.")
        return super().form_valid(form)


class MotoDetailView(LoginRequiredMixin, DetailView):
    model = Moto
    template_name = "moto/moto_detail.html"
    context_object_name = "moto"


class MotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Moto
    template_name = "moto/moto_confirm_delete.html"
    success_url = reverse_lazy("moto:moto_list")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Moto removida com sucesso.")
        return super().delete(request, *args, **kwargs)
