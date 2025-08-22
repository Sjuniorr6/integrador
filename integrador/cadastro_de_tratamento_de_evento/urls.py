# tecnologias/urls.py
from django.urls import path
from .views import (
    TratamentoEventoCreateView,
    TratamentoEventoListView,
    TratamentoEventoUpdateView,
    delete_tratamento_evento
)

urlpatterns = [
    path("cadastrar/", TratamentoEventoCreateView.as_view(), name="cadastro_de_tratamento_de_evento"),
    path("listar/", TratamentoEventoListView.as_view(), name="cadastro_de_tratamento_de_evento_list"),
    path("editar/<int:pk>/", TratamentoEventoUpdateView.as_view(), name="edit_tratamento_evento"),
    path("excluir/<int:pk>/", delete_tratamento_evento, name="delete_tratamento_evento"),
]   
