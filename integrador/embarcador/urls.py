from django.urls import path
from .views import (
    EmbarcadorListView, EmbarcadorCreateView, EmbarcadorUpdateView,
    EmbarcadorDetailView, EmbarcadorDeleteView
)

app_name = "embarcadores"

urlpatterns = [
    path("", EmbarcadorListView.as_view(), name="embarcador_list"),
    path("novo/", EmbarcadorCreateView.as_view(), name="embarcador_create"),
    path("<int:pk>/", EmbarcadorDetailView.as_view(), name="embarcador_detail"),
    path("<int:pk>/editar/", EmbarcadorUpdateView.as_view(), name="embarcador_update"),
    path("<int:pk>/excluir/", EmbarcadorDeleteView.as_view(), name="embarcador_delete"),
]
