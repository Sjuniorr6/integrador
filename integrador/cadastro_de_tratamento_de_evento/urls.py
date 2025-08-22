# tecnologias/urls.py
from django.urls import path
from .views import (cadastro_de_tratamento_de_evento
 
)

urlpatterns = [
    path("cadastrar/", cadastro_de_tratamento_de_evento.as_view(), name="cadastro_de_tratamento_de_evento"),
]
