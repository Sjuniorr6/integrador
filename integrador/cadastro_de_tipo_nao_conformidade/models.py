from django.db import models
from django.utils import timezone

# Create your models here.
class cadastro(models.Model):
    NIVEL_IMPORTANCIA_CHOICES = [
        ("Alta", "Alta"),
        ("Média", "Média"),
        ("Baixa", "Baixa"),
    ]
    
    descricao = models.CharField(max_length=250, verbose_name="Descrição")
    nivel_de_importancia = models.CharField(
        max_length=250, 
        choices=NIVEL_IMPORTANCIA_CHOICES,
        verbose_name="Nível de Importância"
    )
    acao_a_realizar = models.CharField(max_length=250, verbose_name="Ação a Realizar")
    processo_administrativo = models.BooleanField(
        default=False, 
        verbose_name="Processo Administrativo"
    )
    data_criacao = models.DateTimeField(default=timezone.now, verbose_name="Data de Criação")
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")

    class Meta:
        verbose_name = "Tipo de Não Conformidade"
        verbose_name_plural = "Tipos de Não Conformidade"
        ordering = ['-data_criacao']

    def __str__(self):
        return f"{self.descricao[:50]}... - {self.nivel_de_importancia}"

    @property
    def is_processo_administrativo(self):
        return self.processo_administrativo

    @property
    def nivel_importancia_color(self):
        """Return Bootstrap color class based on importance level"""
        colors = {
            "Alta": "danger",
            "Média": "warning", 
            "Baixa": "success"
        }
        return colors.get(self.nivel_de_importancia, "secondary")

