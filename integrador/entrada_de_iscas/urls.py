# estoque/urls.py
from django.urls import path
from .views import (
    EntradaIscasCreateView, EntradaIscasListView, EntradaIscasUpdateView, EntradaIscasDeleteView,
    ClienteCreateView, ClienteListView,
)

app_name = "estoque"

urlpatterns = [
   
    path("iscas/nova/",        EntradaIscasCreateView.as_view(), name="entrada_create"),
    path("iscas/",             EntradaIscasListView.as_view(),   name="entrada_list"),
    path("iscas/<int:pk>/editar/",  EntradaIscasUpdateView.as_view(), name="entrada_update"),
    path("iscas/<int:pk>/remover/", EntradaIscasDeleteView.as_view(), name="entrada_delete"),

   
    path("clientes/novo/",     ClienteCreateView.as_view(), name="cliente_create"),
    path("clientes/",          ClienteListView.as_view(),   name="cliente_list"),
]
