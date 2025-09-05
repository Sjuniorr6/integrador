from django.db import models
from django.core.validators import RegexValidator

class Truck(models.Model):
    class Status(models.TextChoices):
        ATIVO = "ATIVO", "Ativo"
        INATIVO = "INATIVO", "Inativo"

    class SimNao(models.TextChoices):
        SIM = "SIM", "Sim"
        NAO = "NAO", "Não"

    class TipoSuspensao(models.TextChoices):
        AR = "AR", "AR"
        HIDR = "HIDR", "Hidropneumática"
        MECA = "MECA", "Mecânica"
        ROSC = "ROSC", "Rosca"

    status = models.CharField(max_length=7, choices=Status.choices, default=Status.ATIVO)
    placa = models.CharField(
        max_length=7, unique=True,
        validators=[RegexValidator(r"^[A-Z0-9]{7}$", "Informe 7 caracteres (placa).")],
    )
    modelo = models.CharField(max_length=60)
    ano_fabricacao = models.CharField(max_length=4, verbose_name="Ano de fabricação")
    ano_modelo = models.CharField(max_length=4, verbose_name="Ano do modelo")
    cor = models.CharField(max_length=30)
    renavam = models.CharField(max_length=20, unique=True)
    chassi = models.CharField(max_length=25)
    crlv = models.CharField(max_length=40, verbose_name="CRLV")
    telefone_veiculo = models.CharField(max_length=20, blank=True, verbose_name="Telefone do veículo")
    cidade_emplacamento = models.CharField(max_length=100, verbose_name="Cidade do emplacamento")

    frota = models.CharField(max_length=30, blank=True)
    proprietario = models.CharField(max_length=100)
    fator_rpm = models.CharField(max_length=20, blank=True, verbose_name="Fator de RPM")
    fator_velocidade = models.CharField(max_length=20, blank=True, verbose_name="Fator de velocidade")

    numero_eixos = models.PositiveIntegerField()
    tipo_suspensao = models.CharField(max_length=4, choices=TipoSuspensao.choices, default=TipoSuspensao.MECA)
    blindado = models.CharField(max_length=3, choices=SimNao.choices, default=SimNao.NAO)
    tipo_equipamento = models.CharField(max_length=60, blank=True)

    tecnologia_rastreador = models.CharField(max_length=60, blank=True)
    rastreador = models.CharField(max_length=60, blank=True)

    antt = models.CharField(max_length=30, blank=True, verbose_name="ANTT")
    validade_antt = models.CharField(max_length=30, blank=True, verbose_name="Validade ANTT")
    rntrc = models.CharField(max_length=30, blank=True, verbose_name="RNTRC")
    validade_rntrc = models.DateField(blank=True, null=True, verbose_name="Validade RNTRC")

    capacidade_kg = models.PositiveIntegerField(blank=True, null=True, verbose_name="Capacidade (kg)")
    tara_kg = models.PositiveIntegerField(blank=True, null=True, verbose_name="Tara (kg)")
    cubagem = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    observacao = models.TextField(blank=True)

    foto_crlv = models.FileField(upload_to="trucks/crlv/", blank=True, null=True)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Caminhão"
        verbose_name_plural = "Caminhões"
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
