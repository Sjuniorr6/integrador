from django.db import models

# Create your models here.
class cadastro_de_tratamento_de_evento(models.Model):
    descricao = models.CharField(max_length=250)
