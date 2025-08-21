# tecnologias/urls.py
from django.urls import path
from .views import (
    TecnologiaListView, TecnologiaCreateView, TecnologiaUpdateView,
    TecnologiaDetailView, TecnologiaDeleteView
)

urlpatterns = [
    path("", TecnologiaListView.as_view(), name="lista_tecnologias"),
    path("novo/", TecnologiaCreateView.as_view(), name="criar_tecnologia"),
    path("<int:pk>/", TecnologiaDetailView.as_view(), name="detalhar_tecnologia"),
    path("<int:pk>/editar/", TecnologiaUpdateView.as_view(), name="editar_tecnologia"),
    path("<int:pk>/excluir/", TecnologiaDeleteView.as_view(), name="excluir_tecnologia"),
]
