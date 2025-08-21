from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.views.generic import CreateView, TemplateView, FormView
from django.urls import reverse_lazy
from django.http import JsonResponse, HttpResponse
from .models import User
from .forms import UserRegistrationForm, UserLoginForm


class HomeView(TemplateView):
    """Página inicial do sistema"""
    template_name = 'usuarios/home.html'
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('usuarios:login')
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_count'] = User.objects.count()
        return context


class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'usuarios/register.html'
    success_url = reverse_lazy('usuarios:login')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Usuário criado com sucesso! Faça login para continuar.')
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, 'Erro no formulário. Verifique os dados.')
        return super().form_invalid(form)

class UserLoginView(FormView):
    """View para login do usuário usando class-based view"""
    form_class = UserLoginForm
    template_name = 'usuarios/login.html'
    
    def get_success_url(self):
        return reverse_lazy('usuarios:home')
    
    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        messages.success(self.request, f'Bem-vindo, {user.nome}!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Email ou senha incorretos.')
        return super().form_invalid(form)
