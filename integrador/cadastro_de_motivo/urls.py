# tecnologias/urls.py
from django.urls import path
from .views import (motivo
 
)

urlpatterns = [
    path("cadastro_motivo/", motivo.as_view(), name="CadastroDeMotivo"),
]
