# embarcadores/models.py
from django.db import models
from django.core.validators import RegexValidator

class Embarcador(models.Model):
    class Status(models.TextChoices):
        ATIVO = "ATIVO", "Ativo"
        INATIVO = "INATIVO", "Inativo"

    status = models.CharField(
        max_length=7,
        choices=Status.choices,
        default=Status.ATIVO,
        verbose_name="Status",
    )

    nome = models.CharField(max_length=200, unique=True, verbose_name="Nome")

    documento = models.CharField(
        max_length=14,
        unique=True,
        validators=[RegexValidator(r"^(\d{11}|\d{14})$", "Informe 11 (CPF) ou 14 (CNPJ) dígitos.")],
        verbose_name="Documento",
        help_text="Somente números.",
    )

    razao_social = models.CharField(max_length=200, blank=True, verbose_name="Razão Social")
    inscricao_estadual = models.CharField(max_length=30, blank=True, verbose_name="Inscrição Estadual")
    site = models.URLField(blank=True, verbose_name="Site")

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Embarcador"
        verbose_name_plural = "Embarcadores"
        ordering = ["nome"]
        indexes = [
            models.Index(fields=["nome"]),
            models.Index(fields=["documento"]),
            models.Index(fields=["status"]),
        ]

    def __str__(self):
        return self.nome

    def clean(self):
      
        if self.documento:
            self.documento = "".join(ch for ch in self.documento if ch.isdigit())
