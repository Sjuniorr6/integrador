from django.db import models

# Create your models here.
class cadastro(models.Model):
    descricao = models.CharField(max_length=250)
    nivel_de_importancia = models.CharField(max_length=250)
    acao_a_realizar = models.CharField(max_length=250)
    processo_administrativo = models.BooleanField(default=False)

