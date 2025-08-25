from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib import messages
from django.urls import reverse_lazy
from .models import EstacaoRastreamento
from .forms import EstacaoRastreamentoForm

# Create your views here.
class EstacaoRastreamentoCreateView(CreateView):
    model = EstacaoRastreamento
    form_class = EstacaoRastreamentoForm
    template_name = "estacao_rastreamento_form.html"
    success_url = reverse_lazy("estacao_rastreamento_list")
    
    def form_valid(self, form):
        messages.success(self.request, "Estação de rastreamento cadastrada com sucesso!")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Erro ao cadastrar estação de rastreamento. Verifique os dados.")
        return super().form_invalid(form)

class EstacaoRastreamentoListView(ListView):
    model = EstacaoRastreamento
    template_name = "estacao_rastreamento_list.html"
    context_object_name = "estacoes_rastreamento"
    ordering = ["-data_criacao"]
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_estacoes'] = EstacaoRastreamento.objects.count()
        context['estacoes_alto_risco'] = EstacaoRastreamento.objects.filter(Estacao_de_alto_risco=True).count()
        context['estacoes_monitor'] = EstacaoRastreamento.objects.filter(Mostrar_no_monitor_de_operacoes=True).count()
        context['estacoes_eventos_sem_tratamento'] = EstacaoRastreamento.objects.filter(Eventos_sem_tratamento=True).count()
        return context

class EstacaoRastreamentoUpdateView(UpdateView):
    model = EstacaoRastreamento
    form_class = EstacaoRastreamentoForm
    template_name = "estacao_rastreamento_form.html"
    success_url = reverse_lazy("estacao_rastreamento_list")
    
    def form_valid(self, form):
        messages.success(self.request, "Estação de rastreamento atualizada com sucesso!")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Erro ao atualizar estação de rastreamento. Verifique os dados.")
        return super().form_invalid(form)

def delete_estacao_rastreamento(request, pk):
    estacao = get_object_or_404(EstacaoRastreamento, pk=pk)
    if request.method == 'POST':
        estacao.delete()
        messages.success(request, "Estação de rastreamento excluída com sucesso!")
        return redirect('estacao_rastreamento_list')
    return redirect('estacao_rastreamento_list')
    