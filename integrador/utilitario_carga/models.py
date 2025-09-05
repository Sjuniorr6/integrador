from django.db import models
from django.core.validators import RegexValidator

class UtilitarioCarga(models.Model):
    class Status(models.TextChoices):
        ATIVO = "ATIVO", "Ativo"
        INATIVO = "INATIVO", "Inativo"

    class TipoCarroceria(models.TextChoices):
        ABERTA = "ABERTA", "Aberta"
        FECHADA = "FECHADA", "Fechada"
        BAU = "BAU", "Baú"
        REFRIGERADA = "REFRIGERADA", "Refrigerada"
        OUTRA = "OUTRA", "Outra"

    status = models.CharField(max_length=7, choices=Status.choices, default=Status.ATIVO)
    placa = models.CharField(
        max_length=7, unique=True,
        validators=[RegexValidator(r"^[A-Z0-9]{7}$", "Informe 7 caracteres (placa).")]
    )
    modelo = models.CharField(max_length=60)
    tipo_carroceria = models.CharField(max_length=20, choices=TipoCarroceria.choices)
    renavam = models.CharField(max_length=20, unique=True)
    chassi = models.CharField(max_length=25)
    ano_fabricacao = models.CharField(max_length=4)
    cor = models.CharField(max_length=30)
    capacidade_kg = models.PositiveIntegerField(blank=True, null=True, verbose_name="Capacidade (kg)")
    proprietario = models.CharField(max_length=100)
    observacao = models.TextField(blank=True)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Utilitário de Carga"
        verbose_name_plural = "Utilitários de Carga"
        ordering = ["placa"]
        indexes = [
            models.Index(fields=["placa"]),
            models.Index(fields=["status"]),
        ]

    def __str__(self):
        return f"{self.placa} - {self.modelo}"

    def clean(self):
        if self.placa:
            self.placa = self.placa.strip().upper()
        if self.renavam:
            self.renavam = self.renavam.strip()
