# tecnologias/urls.py
from django.urls import path
from .views import (cadastro_de_tipo_nao_conformidade
 
)

urlpatterns = [
    path("cadastrar/", cadastro_de_tipo_nao_conformidade.as_view(), name="cadastro_de_tipo_nao_conformidade"),
]
