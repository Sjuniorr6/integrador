# nao_conformidade_veiculo/urls.py
from django.urls import path
from .views import (
    NaoConformidadeVeiculoListView,
    NaoConformidadeVeiculoCreateView,
    NaoConformidadeVeiculoUpdateView,
    NaoConformidadeVeiculoDetailView,
    NaoConformidadeVeiculoDeleteView,
)

app_name = "nao_conformidade_veiculo"

urlpatterns = [
    path("", NaoConformidadeVeiculoListView.as_view(), name="ncv_list"),
    path("novo/", NaoConformidadeVeiculoCreateView.as_view(), name="ncv_create"),
    path("<int:pk>/", NaoConformidadeVeiculoDetailView.as_view(), name="ncv_detail"),
    path("<int:pk>/editar/", NaoConformidadeVeiculoUpdateView.as_view(), name="ncv_update"),
    path("<int:pk>/excluir/", NaoConformidadeVeiculoDeleteView.as_view(), name="ncv_delete"),
]
