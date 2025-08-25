
from django.db import models
# Create your models here.
class cadastrotecnologia(models.Model):
    comunicacao = [
        ("Satelital", "Satelital"),
        ("Hibrido", "Hibrido"),
        ("Grupo GPRS", "Grupo GPRS"),
        ("Prime", "Prime"),
        ("LBS", "LBS"),


    ]

    descricao = models.CharField(max_length=250)
    versao = models.CharField(max_length=50)
    tempo_satelital = models.IntegerField()
    tempo_gprs = models.IntegerField()
    homologado_para_risco = models.BooleanField(default=False)
    homologado_para_logistica = models.BooleanField(default=False)
    permitir_mensagem_livre = models.BooleanField(default=False)
    tipo_de_comunicacao = models.CharField(max_length=250)
    posicoes_calculo_posicionamento = models.IntegerField()
    comunicacao = models.CharField(max_length=50, choices=comunicacao)