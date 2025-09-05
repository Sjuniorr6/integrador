from django.db import models

class TipoSegmento(models.Model):
    descricao = models.CharField(max_length=120, unique=True, verbose_name="Descrição")
    tipo_carroceria = models.CharField(max_length=120, verbose_name="Tipo de carroceria") 

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta: 
        verbose_name = "Tipo de segmento"
        verbose_name_plural = "Tipos de segmento"
        ordering = ["descricao"]
        indexes = [
            models.Index(fields=["descricao"]),
            models.Index(fields=["tipo_carroceria"]),
        ]

        def __str__(self):
            return f"{self.descricao} - {self.tipo_carroceria}"