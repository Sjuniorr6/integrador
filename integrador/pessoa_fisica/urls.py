from django.urls import path
from .views import (
    PessoaFisicaListView, PessoaFisicaCreateView,
    PessoaFisicaUpdateView, PessoaFisicaDetailView,
    PessoaFisicaDeleteView,
)

app_name = "pessoa_fisica"

urlpatterns = [
    path("", PessoaFisicaListView.as_view(), name="pf_list"),
    path("novo/", PessoaFisicaCreateView.as_view(), name="pf_create"),
    path("<int:pk>/", PessoaFisicaDetailView.as_view(), name="pf_detail"),
    path("<int:pk>/editar/", PessoaFisicaUpdateView.as_view(), name="pf_update"),
    path("<int:pk>/excluir/", PessoaFisicaDeleteView.as_view(), name="pf_delete"),
]
