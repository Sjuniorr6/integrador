from django.urls import path
from .views import (
    MotoListView, MotoCreateView, MotoUpdateView,
    MotoDetailView, MotoDeleteView,
)

app_name = "moto"

urlpatterns = [
    path("", MotoListView.as_view(), name="moto_list"),
    path("novo/", MotoCreateView.as_view(), name="moto_create"),
    path("<int:pk>/", MotoDetailView.as_view(), name="moto_detail"),
    path("<int:pk>/editar/", MotoUpdateView.as_view(), name="moto_update"),
    path("<int:pk>/excluir/", MotoDeleteView.as_view(), name="moto_delete"),
]
