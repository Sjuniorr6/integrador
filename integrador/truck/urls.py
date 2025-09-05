# truck/urls.py
from django.urls import path
from .views import (
    TruckListView,
    TruckCreateView,
    TruckUpdateView,
    TruckDeleteView,
)

urlpatterns = [
    path("", TruckListView.as_view(), name="truck_list"),
    path("novo/", TruckCreateView.as_view(), name="truck_create"),
    path("editar/<int:pk>/", TruckUpdateView.as_view(), name="truck_update"),
    path("remover/<int:pk>/", TruckDeleteView.as_view(), name="truck_delete"),
]
