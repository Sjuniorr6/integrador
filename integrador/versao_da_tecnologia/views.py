from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import cadastrotecnologia
from django.urls import reverse_lazy
from .forms import CadastroTecnologiaForm   
from django.contrib import messages

# Create your views here.

class VersaoDaTecnologiaCreateView(CreateView):
    model = cadastrotecnologia
    form_class = CadastroTecnologiaForm
    template_name = "versaotecnologia_form.html"
    success_url = reverse_lazy("versao_da_tecnologia_list")
    
    def form_valid(self, form):
        messages.success(self.request, "Versão da tecnologia cadastrada com sucesso!")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Erro ao cadastrar versão da tecnologia. Verifique os dados.")
        return super().form_invalid(form)

class VersaoDaTecnologiaListView(ListView):
    model = cadastrotecnologia
    template_name = 'versaotecnologia_list.html'
    context_object_name = 'tecnologias'
    ordering = ["-data_criacao"]
    paginate_by = 10
    
    def get_queryset(self):
        queryset = cadastrotecnologia.objects.all()
        comunicacao_filter = self.request.GET.get('comunicacao')
        if comunicacao_filter:
            queryset = queryset.filter(comunicacao=comunicacao_filter)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_tecnologias'] = cadastrotecnologia.objects.count()
        context['homologadas_risco'] = cadastrotecnologia.objects.filter(homologado_para_risco=True).count()
        context['homologadas_logistica'] = cadastrotecnologia.objects.filter(homologado_para_logistica=True).count()
        return context

class VersaoDaTecnologiaUpdateView(UpdateView):
    model = cadastrotecnologia
    form_class = CadastroTecnologiaForm
    template_name = 'versaotecnologia_form.html'
    success_url = reverse_lazy("versao_da_tecnologia_list")

    def form_valid(self, form):
        messages.success(self.request, "Versão da tecnologia atualizada com sucesso!")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Erro ao atualizar versão da tecnologia. Verifique os dados.")
        return super().form_invalid(form)

def delete_versao_tecnologia(request, pk):
    """Delete a Versão da Tecnologia record"""
    tecnologia = get_object_or_404(cadastrotecnologia, pk=pk)
    if request.method == 'POST':
        tecnologia.delete()
        messages.success(request, "Versão da tecnologia excluída com sucesso!")
        return redirect('versao_da_tecnologia_list')
    return redirect('versao_da_tecnologia_list')
    