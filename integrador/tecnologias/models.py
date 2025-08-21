from django.db import models

# Create your models here.
class Tecnologia(models.Model):
    tecnologia = [ 
                  ("ônix", "ônix"),
                  ("omnilink", "omnilink"),
                  ("sascar", "sascar"),
                  ("autotrack", "autotrack"),
                  ("siga", "siga"),
                 
                  ]
    status = [ 
              ("ativo", "ativo"),
              ("inativo", "inativo"),
              ]
    nome_da_conta = models.CharField(max_length=255)
    ip_da_integracao = models.CharField(max_length=255)
    tolerancia_tempo_sem_resposta = models.IntegerField()
    tolerancia_de_envio_de_comandos = models.IntegerField()
    quantidade_de_erros_simuntaneos = models.IntegerField()
    tempo_aguardar_retorno = models.IntegerField()
    tecnologia = models.CharField(max_length=255, choices=tecnologia)
    caminho_aplicacao = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=status)
    inicio_horario_tolerancia = models.TimeField()
    fim_horario_tolerancia = models.TimeField()
    empresa_contato = models.CharField(max_length=255)
    monitorado_guardiao = models.BooleanField(default=False)
    ignorado_monitor_integracoes = models.BooleanField(default=False)
    enviar_comandos = models.BooleanField(default=False)
    
 