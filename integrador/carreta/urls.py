# carretas/urls.py
from django.urls import path
from .views import (
    CarretaListView, CarretaCreateView, CarretaUpdateView,
    CarretaDetailView, CarretaDeleteView
)

app_name = "carretas"

urlpatterns = [
    path("", CarretaListView.as_view(), name="list"),
    path("novo/", CarretaCreateView.as_view(), name="create"),
    path("<int:pk>/", CarretaDetailView.as_view(), name="detail"),
    path("<int:pk>/editar/", CarretaUpdateView.as_view(), name="update"),
    path("<int:pk>/excluir/", CarretaDeleteView.as_view(), name="delete"),
]
