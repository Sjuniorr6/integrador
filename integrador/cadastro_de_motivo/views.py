from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import JsonResponse
from .models import CadastroDeMotivo
from .forms import CadastroDeMotivoForm


# Create your views here.
class MotivoCreateView(CreateView):
    model = CadastroDeMotivo
    form_class = CadastroDeMotivoForm
    template_name = "Motivo_form.html"
    success_url = reverse_lazy("Motivo_list")
    
    def form_valid(self, form):
        messages.success(self.request, "Motivo cadastrado com sucesso!")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Erro ao cadastrar motivo. Verifique os dados.")
        return super().form_invalid(form)

class MotivoUpdateView(UpdateView):
    model = CadastroDeMotivo
    form_class = CadastroDeMotivoForm
    template_name = "Motivo_form.html"
    success_url = reverse_lazy("Motivo_list")
    
    def form_valid(self, form):
        messages.success(self.request, "Motivo atualizado com sucesso!")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Erro ao atualizar motivo. Verifique os dados.")
        return super().form_invalid(form)
    
class MotivoListView(ListView):
    model = CadastroDeMotivo
    template_name = "Motivo_list.html"
    context_object_name = "motivos"
    ordering = ["-data_criacao"]
    paginate_by = 10
    
    def get_queryset(self):
        queryset = CadastroDeMotivo.objects.all()
        status_filter = self.request.GET.get('status')
        if status_filter:
            queryset = queryset.filter(Status=status_filter)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_motivos'] = CadastroDeMotivo.objects.count()
        context['motivos_ativos'] = CadastroDeMotivo.objects.filter(Status="Ativo").count()
        context['motivos_inativos'] = CadastroDeMotivo.objects.filter(Status="Inativo").count()
        return context

def delete_motivo(request, pk):
    """Delete a Motivo record"""
    motivo = get_object_or_404(CadastroDeMotivo, pk=pk)
    if request.method == 'POST':
        motivo.delete()
        messages.success(request, "Motivo excluído com sucesso!")
        return redirect('Motivo_list')
    return redirect('Motivo_list')
    
    
    
    
    