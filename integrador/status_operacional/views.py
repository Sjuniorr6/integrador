# status_operacional/views.py
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import StatusOperacional
from .forms import StatusOperacionalForm

class StatusOperacionalListView(LoginRequiredMixin, ListView):
    model = StatusOperacional
    template_name = "status_operacional/status_list.html"
    context_object_name = "itens"
    paginate_by = 25
    ordering = ["descricao"]

class StatusOperacionalCreateView(LoginRequiredMixin, CreateView):
    model = StatusOperacional
    form_class = StatusOperacionalForm
    template_name = "status_operacional/status_form.html"
    success_url = reverse_lazy("status_operacional:list")

    def form_valid(self, form):
        messages.success(self.request, "Status criado com sucesso.")
        return super().form_valid(form)

class StatusOperacionalUpdateView(LoginRequiredMixin, UpdateView):
    model = StatusOperacional
    form_class = StatusOperacionalForm
    template_name = "status_operacional/status_form.html"
    success_url = reverse_lazy("status_operacional:list")

    def form_valid(self, form):
        messages.success(self.request, "Status atualizado com sucesso.")
        return super().form_valid(form)

class StatusOperacionalDeleteView(LoginRequiredMixin, DeleteView):
    model = StatusOperacional
    template_name = "status_operacional/status_confirm_delete.html"
    success_url = reverse_lazy("status_operacional:list")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Status excluído com sucesso.")
        return super().delete(request, *args, **kwargs)
