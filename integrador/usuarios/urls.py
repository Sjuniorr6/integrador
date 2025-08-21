from django.urls import path
from django.shortcuts import redirect
from . import views

app_name = 'usuarios'

def redirect_to_login(request):
    """Redireciona para a página de login"""
    return redirect('usuarios:login')

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
]
