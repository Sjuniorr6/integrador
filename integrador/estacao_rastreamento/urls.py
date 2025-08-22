# tecnologias/urls.py
from django.urls import path
from .views import (estacao_rastreamento
 
)

urlpatterns = [
    path("estacao_rastreamento/", estacao_rastreamento.as_view(), name="estacao_rastreamento"),
]
