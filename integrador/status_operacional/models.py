# status_operacional/models.py
from django.db import models

class StatusOperacional(models.Model):
    descricao = models.CharField("Descrição", max_length=150, unique=True)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Status Operacional"
        verbose_name_plural = "Status Operacionais"
        ordering = ["descricao"]
        indexes = [models.Index(fields=["descricao"])]

    def __str__(self):
        return self.descricao

