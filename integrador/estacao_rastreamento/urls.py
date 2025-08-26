# estacao_rastreamento/urls.py
from django.urls import path
from .views import (
    EstacaoRastreamentoCreateView,
    EstacaoRastreamentoListView,
    EstacaoRastreamentoUpdateView,
    delete_estacao_rastreamento
)

urlpatterns = [
    path("cadastrar/", EstacaoRastreamentoCreateView.as_view(), name="estacao_rastreamento_create"),
    path("listar/", EstacaoRastreamentoListView.as_view(), name="estacao_rastreamento_list"),
    path("editar/<int:pk>/", EstacaoRastreamentoUpdateView.as_view(), name="estacao_rastreamento_update"),
    path("excluir/<int:pk>/", delete_estacao_rastreamento, name="delete_estacao_rastreamento"),
]
