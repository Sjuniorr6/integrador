"""
URL configuration for integrador project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def redirect_to_login(request):
    """Redireciona a página raiz para o login"""
    return redirect('usuarios:login')

urlpatterns = [
    path('', redirect_to_login, name='root'),
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('tecnologias/', include('tecnologias.urls')),
    path('estacao_rastreamento/', include('estacao_rastreamento.urls')),
    path('cadastro_de_motivo/', include('cadastro_de_motivo.urls')),
    path('cadastro_de_tipo_nao_conformidade/', include('cadastro_de_tipo_nao_conformidade.urls')),
    path('cadastro_de_tratamento_de_evento/', include('cadastro_de_tratamento_de_evento.urls')),
    path('versao_da_tecnologia/', include('versao_da_tecnologia.urls')),
    path('entrada_de_iscas/', include('entrada_de_iscas.urls')),
]

