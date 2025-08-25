# tecnologias/urls.py
from django.urls import path
from .views import (versao_da_tecnologia
 
)

urlpatterns = [
    path("versao_da_tecnologia/", versao_da_tecnologia.as_view(), name="versao_da_tecnologia"),
]
