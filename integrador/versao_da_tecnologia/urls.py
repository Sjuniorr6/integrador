# tecnologias/urls.py
from django.urls import path
from .views import (
    VersaoDaTecnologiaCreateView,
    VersaoDaTecnologiaListView,
    VersaoDaTecnologiaUpdateView,
    delete_versao_tecnologia
)

urlpatterns = [
    path("versao_da_tecnologia/", VersaoDaTecnologiaCreateView.as_view(), name="versao_da_tecnologia"),
    path("versao_da_tecnologia/list/", VersaoDaTecnologiaListView.as_view(), name="versao_da_tecnologia_list"),
    path("versao_da_tecnologia/update/<int:pk>/", VersaoDaTecnologiaUpdateView.as_view(), name="versao_da_tecnologia_update"),
    path("versao_da_tecnologia/delete/<int:pk>/", delete_versao_tecnologia, name="versao_da_tecnologia_delete"),
]
