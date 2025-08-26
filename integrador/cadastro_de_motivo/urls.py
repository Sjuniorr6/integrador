# cadastro_de_motivo/urls.py
from django.urls import path
from .views import MotivoCreateView, MotivoListView, MotivoUpdateView, delete_motivo

urlpatterns = [
    path("cadastro_motivo/", MotivoCreateView.as_view(), name="Motivo_create"),
    path('motivo_list/', MotivoListView.as_view(), name="Motivo_list"),
    path('edit_motivo/<int:pk>/', MotivoUpdateView.as_view(), name="Motivo_update"),
    path('delete_motivo/<int:pk>/', delete_motivo, name="delete_motivo"),
]
