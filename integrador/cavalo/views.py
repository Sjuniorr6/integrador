from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from .models import Cavalo
from .forms import CavaloForm


class CavaloListView(LoginRequiredMixin, ListView):
    model = Cavalo
    template_name = "cavalo/cavalo_list.html"
    context_object_name = "cavalos"
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
                Q(proprietario__icontains=q)
            )
        status = self.request.GET.get("status")
        if status in dict(Cavalo.Status.choices):
            qs = qs.filter(status=status)
        return qs


class CavaloCreateView(LoginRequiredMixin, CreateView):
    model = Cavalo
    form_class = CavaloForm
    template_name = "cavalo/cavalo_form.html"
    success_url = reverse_lazy("cavalo:cavalo_list")

    def form_valid(self, form):
        messages.success(self.request, "Cavalo cadastrado com sucesso.")
        return super().form_valid(form)


class CavaloUpdateView(LoginRequiredMixin, UpdateView):
    model = Cavalo
    form_class = CavaloForm
    template_name = "cavalo/cavalo_form.html"
    success_url = reverse_lazy("cavalo:cavalo_list")

    def form_valid(self, form):
        messages.success(self.request, "Cadastro de cavalo atualizado com sucesso.")
        return super().form_valid(form)


class CavaloDetailView(LoginRequiredMixin, DetailView):
    model = Cavalo
    template_name = "cavalo/cavalo_detail.html"
    context_object_name = "cavalo"


class CavaloDeleteView(LoginRequiredMixin, DeleteView):
    model = Cavalo
    template_name = "cavalo/cavalo_confirm_delete.html"
    success_url = reverse_lazy("cavalo:cavalo_list")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Cavalo removido com sucesso.")
        return super().delete(request, *args, **kwargs)
