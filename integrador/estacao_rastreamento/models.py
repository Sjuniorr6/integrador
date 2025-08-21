from django.db import models

# Create your models here.
class EstacaoRastreamento(models.Model):
    Rastreamento = [       
             ("Acompanhamento de Gerenci. de Risco e Logistica", "Acompanhamento de Gerenci. de Risco e Logistica" "ônix"),
                  ("Acompanhamento de Gerenciamento de Risco", "Acompanhamento de Gerenciamento de Risco"),
                  ("Acompanhamento de Logistica", "Acompanhamento de Logistica"),
    
    ]

    Separacaodorastreamento = [
            ("Separado por embarcador transportador", "Separado por embarcador transportador"),
              ("Separado por Grau de Rsico", "Separado por Grau de Rsico"),
            ("Separado por Tecnologia", "Separado por Tecnologia"),
              ("Separado por tipo Manual", "Separado por Tipo Manual"),
                ("Separado por tipo de operação", "Separado por tipo de operação"),
    ]           
    descricao = models.CharField(max_length=500)
    tipo_de_estacao_de_rastreamento = models.CharField(max_length=50,choices=Rastreamento)
    Separacao_de_rastreamento = models.CharField(max_length=50,choices=Separacaodorastreamento)
    Numero_maximo_de_veiculos_da_estacao = models.IntegerField()
    Eventos_sem_tratamento = models.BooleanField(default=False)
    Mostrar_no_monitor_de_operacoes = models.BooleanField(default=False)
    Estacao_de_alto_risco = models.BooleanField(default=False)
    Usar_importancia_do_evento_para_redirecionar = models.BooleanField(default=False)