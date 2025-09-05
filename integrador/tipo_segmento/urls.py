from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_segmentos, name='listar_segmentos'),
    path('novo/', views.criar_segmento, name='criar_segmento'),
]
