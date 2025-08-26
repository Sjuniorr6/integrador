from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib import messages
from .models import Cliente, EntradaIscas
from .forms import ClienteForm, EntradaIscasForm


class EntradaIscasCreateView(CreateView):
    model = EntradaIscas
    form_class = EntradaIscasForm
    template_name = "entrada_iscas_form.html"
    success_url = reverse_lazy("estoque:entrada_list")
    
    def form_valid(self, form):
        messages.success(self.request, "Entrada de iscas cadastrada com sucesso!")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Erro ao cadastrar entrada de iscas. Verifique os dados.")
        return super().form_invalid(form)


class EntradaIscasListView(ListView):
    model = EntradaIscas
    template_name = "entrada_iscas_list.html"
    context_object_name = "entradas"
    ordering = ["-data_criacao"]
    paginate_by = 25
    
    def get_queryset(self):
        queryset = EntradaIscas.objects.select_related('cliente').all()
        cliente_filter = self.request.GET.get('cliente')
        if cliente_filter:
            queryset = queryset.filter(cliente__nome__icontains=cliente_filter)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_entradas'] = EntradaIscas.objects.count()
        context['total_quantidade'] = sum(entrada.quantidade for entrada in EntradaIscas.objects.all())
        context['estoque_critico'] = sum(1 for entrada in EntradaIscas.objects.all() if entrada.status_estoque == "Crítico")
        context['clientes'] = Cliente.objects.all()
        return context


class EntradaIscasUpdateView(UpdateView):
    model = EntradaIscas
    form_class = EntradaIscasForm
    template_name = "entrada_iscas_form.html"
    success_url = reverse_lazy("estoque:entrada_list")
    
    def form_valid(self, form):
        messages.success(self.request, "Entrada de iscas atualizada com sucesso!")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Erro ao atualizar entrada de iscas. Verifique os dados.")
        return super().form_invalid(form)


def delete_entrada_iscas(request, pk):
    """Delete an EntradaIscas record"""
    entrada = get_object_or_404(EntradaIscas, pk=pk)
    if request.method == 'POST':
        entrada.delete()
        messages.success(request, "Entrada de iscas excluída com sucesso!")
        return redirect('estoque:entrada_list')
    return redirect('estoque:entrada_list')


class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "cliente_form.html"
    success_url = reverse_lazy("estoque:entrada_create")
    
    def form_valid(self, form):
        messages.success(self.request, "Cliente cadastrado com sucesso!")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Erro ao cadastrar cliente. Verifique os dados.")
        return super().form_invalid(form)


class ClienteListView(ListView):
    model = Cliente
    template_name = "cliente_list.html"
    context_object_name = "clientes"
    ordering = ["nome"]
    paginate_by = 20
    
    def get_queryset(self):
        queryset = Cliente.objects.all()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(nome__icontains=search)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_clientes'] = Cliente.objects.count()
        context['clientes_com_entradas'] = Cliente.objects.filter(entradas_iscas__isnull=False).distinct().count()
        return context