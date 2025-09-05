# status_operacional/urls.py
from django.urls import path
from .views import (
    StatusOperacionalListView,
    StatusOperacionalCreateView,
    StatusOperacionalUpdateView,
    StatusOperacionalDeleteView,
)

app_name = "status_operacional"

urlpatterns = [
    path("", StatusOperacionalListView.as_view(), name="list"),
    path("novo/", StatusOperacionalCreateView.as_view(), name="create"),
    path("<int:pk>/editar/", StatusOperacionalUpdateView.as_view(), name="update"),
    path("<int:pk>/excluir/", StatusOperacionalDeleteView.as_view(), name="delete"),
]
