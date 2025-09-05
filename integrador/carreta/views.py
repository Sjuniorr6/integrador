# carretas/views.py
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import Carreta
from .forms import CarretaForm

class CarretaListView(LoginRequiredMixin, ListView):
    model = Carreta
    template_name = "carretas/carreta_list.html"
    context_object_name = "carretas"
    paginate_by = 25
    ordering = ["placa"]

class CarretaCreateView(LoginRequiredMixin, CreateView):
    model = Carreta
    form_class = CarretaForm
    template_name = "carretas/carreta_form.html"
    success_url = reverse_lazy("carretas:list")

    def form_valid(self, form):
        messages.success(self.request, "Carreta cadastrada com sucesso.")
        return super().form_valid(form)

class CarretaUpdateView(LoginRequiredMixin, UpdateView):
    model = Carreta
    form_class = CarretaForm
    template_name = "carretas/carreta_form.html"
    success_url = reverse_lazy("carretas:list")

    def form_valid(self, form):
        messages.success(self.request, "Carreta atualizada com sucesso.")
        return super().form_valid(form)

class CarretaDetailView(LoginRequiredMixin, DetailView):
    model = Carreta
    template_name = "carretas/carreta_detail.html"
    context_object_name = "carreta"

class CarretaDeleteView(LoginRequiredMixin, DeleteView):
    model = Carreta
    template_name = "carretas/carreta_confirm_delete.html"
    success_url = reverse_lazy("carretas:list")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Carreta excluída com sucesso.")
        return super().delete(request, *args, **kwargs)
