from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import UtilitarioCarga
from .forms import UtilitarioCargaForm

class UtilitarioCargaListView(ListView):
    model = UtilitarioCarga
    template_name = "utilitario_carga/list.html"
    context_object_name = "utilitarios"

class UtilitarioCargaCreateView(CreateView):
    model = UtilitarioCarga
    form_class = UtilitarioCargaForm
    template_name = "utilitario_carga/form.html"
    success_url = reverse_lazy("utilitario_carga:list")

class UtilitarioCargaUpdateView(UpdateView):
    model = UtilitarioCarga
    form_class = UtilitarioCargaForm
    template_name = "utilitario_carga/form.html"
    success_url = reverse_lazy("utilitario_carga:list")

class UtilitarioCargaDeleteView(DeleteView):
    model = UtilitarioCarga
    template_name = "utilitario_carga/delete.html"
    success_url = reverse_lazy("utilitario_carga:list")
