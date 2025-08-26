from django.urls import path
from . import views

app_name = 'saida_de_iscas'

urlpatterns = [
    # URLs para views baseadas em classe
    path('', views.SaidaIscasListView.as_view(), name='saida_iscas_list'),
    path('nova/', views.SaidaIscasCreateView.as_view(), name='saida_iscas_create'),
    path('<int:pk>/editar/', views.SaidaIscasUpdateView.as_view(), name='saida_iscas_update'),
    path('<int:pk>/excluir/', views.SaidaIscasDeleteView.as_view(), name='saida_iscas_delete'),
    
    # URLs alternativas para views baseadas em função
    # path('', views.saida_iscas_list, name='saida_iscas_list'),
    # path('nova/', views.saida_iscas_create, name='saida_iscas_create'),
    # path('<int:pk>/editar/', views.saida_iscas_update, name='saida_iscas_update'),
    # path('<int:pk>/excluir/', views.saida_iscas_delete, name='saida_iscas_delete'),
]
