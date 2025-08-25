from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib import messages
from django.urls import reverse_lazy
from .models import cadastro_de_tratamento_de_evento
from .forms import CadastroDeTratamentoDeEventoForm

# Create your views here.
class TratamentoEventoCreateView(CreateView):
    model = cadastro_de_tratamento_de_evento
    form_class = CadastroDeTratamentoDeEventoForm
    template_name = "tratamento_de_evento_form.html"
    success_url = reverse_lazy("cadastro_de_tratamento_de_evento_list")
    
    def form_valid(self, form):
        messages.success(self.request, "Tratamento de evento cadastrado com sucesso!")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Erro ao cadastrar tratamento de evento. Verifique os dados.")
        return super().form_invalid(form)

class TratamentoEventoUpdateView(UpdateView):
    model = cadastro_de_tratamento_de_evento
    form_class = CadastroDeTratamentoDeEventoForm
    template_name = "tratamento_de_evento_form.html"
    success_url = reverse_lazy("cadastro_de_tratamento_de_evento_list")
    
    def form_valid(self, form):
        messages.success(self.request, "Tratamento de evento atualizado com sucesso!")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Erro ao atualizar tratamento de evento. Verifique os dados.")
        return super().form_invalid(form)

class TratamentoEventoListView(ListView):
    model = cadastro_de_tratamento_de_evento
    template_name = "tratamento_de_evento_list.html"
    context_object_name = "tratamentos_evento"
    ordering = ["-data_criacao"]
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_tratamentos'] = cadastro_de_tratamento_de_evento.objects.count()
        context['tratamentos_ativos'] = cadastro_de_tratamento_de_evento.objects.filter(status="Ativo").count()
        context['tratamentos_inativos'] = cadastro_de_tratamento_de_evento.objects.filter(status="Inativo").count()
        return context

def delete_tratamento_evento(request, pk):
    """Delete a Tratamento de Evento record"""
    tratamento = get_object_or_404(cadastro_de_tratamento_de_evento, pk=pk)
    if request.method == 'POST':
        tratamento.delete()
        messages.success(request, "Tratamento de evento excluído com sucesso!")
        return redirect('cadastro_de_tratamento_de_evento_list')
    return redirect('cadastro_de_tratamento_de_evento_list')
    
    
    