# tecnologias/urls.py
from django.urls import path
from .views import (cadastro_de_tipo_nao_conformidade_update,cadastro_de_tipo_nao_conformidade,cadastro_de_tipo_nao_conformidade_list
 
)

urlpatterns = [
    path("cadastrar/", cadastro_de_tipo_nao_conformidade.as_view(), name="cadastro_de_tipo_nao_conformidade"),
    path("listar/", cadastro_de_tipo_nao_conformidade_list.as_view(), name="cadastro_de_tipo_nao_conformidade_list"),
    path("editar/<int:pk>/", cadastro_de_tipo_nao_conformidade_update.as_view(), name="cadastro_de_tipo_nao_conformidade_update"),
]
