from django.urls import path
from .views import (
    UtilitarioCargaListView,
    UtilitarioCargaCreateView,
    UtilitarioCargaUpdateView,
    UtilitarioCargaDeleteView,
)

app_name = "utilitario_carga"

urlpatterns = [
    path("", UtilitarioCargaListView.as_view(), name="list"),
    path("novo/", UtilitarioCargaCreateView.as_view(), name="create"),
    path("<int:pk>/editar/", UtilitarioCargaUpdateView.as_view(), name="update"),
    path("<int:pk>/excluir/", UtilitarioCargaDeleteView.as_view(), name="delete"),
]
