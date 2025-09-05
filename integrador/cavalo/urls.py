from django.urls import path
from .views import (
    CavaloListView, CavaloCreateView, CavaloUpdateView,
    CavaloDetailView, CavaloDeleteView,
)

app_name = "cavalo"

urlpatterns = [
    path("", CavaloListView.as_view(), name="cavalo_list"),
    path("novo/", CavaloCreateView.as_view(), name="cavalo_create"),
    path("<int:pk>/", CavaloDetailView.as_view(), name="cavalo_detail"),
    path("<int:pk>/editar/", CavaloUpdateView.as_view(), name="cavalo_update"),
    path("<int:pk>/excluir/", CavaloDeleteView.as_view(), name="cavalo_delete"),
]
