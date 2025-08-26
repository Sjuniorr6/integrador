from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import SaidaIscas
from .forms import SaidaIscasForm

# Views baseadas em classe
class SaidaIscasListView(LoginRequiredMixin, ListView):
    model = SaidaIscas
    template_name = 'saida_de_iscas/saida_iscas_list.html'
    context_object_name = 'saidas_iscas'
    paginate_by = 10

class SaidaIscasCreateView(LoginRequiredMixin, CreateView):
    model = SaidaIscas
    form_class = SaidaIscasForm
    template_name = 'saida_de_iscas/saida_iscas_form.html'
    success_url = reverse_lazy('saida_iscas_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Saída de iscas registrada com sucesso!')
        return super().form_valid(form)

class SaidaIscasUpdateView(LoginRequiredMixin, UpdateView):
    model = SaidaIscas
    form_class = SaidaIscasForm
    template_name = 'saida_de_iscas/saida_iscas_form.html'
    success_url = reverse_lazy('saida_iscas_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Saída de iscas atualizada com sucesso!')
        return super().form_valid(form)

class SaidaIscasDeleteView(LoginRequiredMixin, DeleteView):
    model = SaidaIscas
    template_name = 'saida_de_iscas/saida_iscas_confirm_delete.html'
    success_url = reverse_lazy('saida_iscas_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Saída de iscas excluída com sucesso!')
        return super().delete(request, *args, **kwargs)

# Views baseadas em função (alternativa)
@login_required
def saida_iscas_list(request):
    saidas_iscas = SaidaIscas.objects.all().order_by('-data_saida')
    return render(request, 'saida_de_iscas/saida_iscas_list.html', {'saidas_iscas': saidas_iscas})

@login_required
def saida_iscas_create(request):
    if request.method == 'POST':
        form = SaidaIscasForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Saída de iscas registrada com sucesso!')
            return redirect('saida_iscas_list')
    else:
        form = SaidaIscasForm()
    
    return render(request, 'saida_de_iscas/saida_iscas_form.html', {'form': form, 'title': 'Nova Saída de Iscas'})

@login_required
def saida_iscas_update(request, pk):
    saida_iscas = get_object_or_404(SaidaIscas, pk=pk)
    if request.method == 'POST':
        form = SaidaIscasForm(request.POST, instance=saida_iscas)
        if form.is_valid():
            form.save()
            messages.success(request, 'Saída de iscas atualizada com sucesso!')
            return redirect('saida_iscas_list')
    else:
        form = SaidaIscasForm(instance=saida_iscas)
    
    return render(request, 'saida_de_iscas/saida_iscas_form.html', {
        'form': form, 
        'title': 'Editar Saída de Iscas',
        'saida_iscas': saida_iscas
    })

@login_required
def saida_iscas_delete(request, pk):
    saida_iscas = get_object_or_404(SaidaIscas, pk=pk)
    if request.method == 'POST':
        saida_iscas.delete()
        messages.success(request, 'Saída de iscas excluída com sucesso!')
        return redirect('saida_iscas_list')
    
    return render(request, 'saida_de_iscas/saida_iscas_confirm_delete.html', {'saida_iscas': saida_iscas})
