from django.urls import path
from .views import (
    RastreadorListView, RastreadorCreateView, RastreadorUpdateView,
    RastreadorDetailView, RastreadorDeleteView,
)

app_name = "cadastro_rastreador"

urlpatterns = [
    path("", RastreadorListView.as_view(), name="list"),
    path("novo/", RastreadorCreateView.as_view(), name="create"),
    path("<int:pk>/", RastreadorDetailView.as_view(), name="detail"),
    path("<int:pk>/editar/", RastreadorUpdateView.as_view(), name="update"),
    path("<int:pk>/excluir/", RastreadorDeleteView.as_view(), name="delete"),
]
