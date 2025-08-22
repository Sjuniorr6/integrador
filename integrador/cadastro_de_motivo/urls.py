# tecnologias/urls.py
from django.urls import path
from .views import MotivoCreateView, MotivoListView, MotivoUpdateView, delete_motivo

urlpatterns = [
    path("cadastro_motivo/", MotivoCreateView.as_view(), name="CadastroDeMotivo"),
    path('motivo_list/', MotivoListView.as_view(), name="Motivo_list"),
    path('edit_motivo/<int:pk>/', MotivoUpdateView.as_view(), name="edit_motivo"),
    path('delete_motivo/<int:pk>/', delete_motivo, name="delete_motivo"),
]
