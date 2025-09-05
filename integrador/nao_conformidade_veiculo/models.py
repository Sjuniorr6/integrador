# nao_conformidade_veiculo/models.py
from django.db import models


class NaoConformidadeVeiculo(models.Model):
    class Situacao(models.TextChoices):
        BLOQUEADO = "BLOQUEADO", "Bloqueado"
        DESBLOQUEADO = "DESBLOQUEADO", "Desbloqueado"

    cliente = models.CharField(max_length=150, verbose_name="Cliente")
    viagem = models.CharField(max_length=100, verbose_name="Viagem")
    veiculo = models.CharField(max_length=50, verbose_name="Veículo")
    frota = models.CharField(max_length=50, verbose_name="Frota")

    suspenso_desde = models.DateField(verbose_name="Suspenso desde")
    situacao = models.CharField(
        max_length=13,
        choices=Situacao.choices,
        default=Situacao.BLOQUEADO,
        verbose_name="Situação",
        db_index=True,
    )
    agendamento_liberacao = models.DateField(
        blank=True, null=True, verbose_name="Agendamento de liberação"
    )

    transportador = models.CharField(max_length=150, verbose_name="Transportador")
    problemas_mecanicos = models.CharField(
        max_length=255, verbose_name="Problemas mecânicos", blank=True
    )
    problemas_rastreador = models.CharField(
        max_length=255, verbose_name="Problemas de rastreador", blank=True
    )
    observacao = models.CharField(
        max_length=500, verbose_name="Observação", blank=True
    )
    motivo_interno = models.CharField(
        max_length=255, verbose_name="Motivo interno", blank=True
    )

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Não Conformidade de Veículo"
        verbose_name_plural = "Não Conformidades de Veículo"
        ordering = ["-suspenso_desde", "cliente"]
        indexes = [
            models.Index(fields=["cliente"]),
            models.Index(fields=["veiculo"]),
            models.Index(fields=["situacao"]),
        ]

    def __str__(self):
        return f"{self.cliente} - {self.veiculo} ({self.get_situacao_display()})"
