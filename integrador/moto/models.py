from django.db import models
from django.core.validators import MinValueValidator


class Moto(models.Model):
    # ---- Choices ----
    class Status(models.TextChoices):
        ATIVO = "ATIVO", "Ativo"
        INATIVO = "INATIVO", "Inativo"

    class SimNao(models.TextChoices):
        NAO = "NAO", "Não"
        SIM = "SIM", "Sim"

    class Suspensao(models.TextChoices):
        AR = "AR", "AR"
        HIDR = "HIDR", "Hidropneumática"
        MECA = "MECA", "Mecânica"
        ROSC = "ROSC", "Rosca"

    class Combustivel(models.TextChoices):
        GASOLINA = "GASOLINA", "Gasolina"
        DIESEL = "DIESEL", "Diesel"
        GNV = "GNV", "Gás Natural Veicular"
        ETANOL = "ETANOL", "Etanol"

    # ---- Campos principais ----
    status = models.CharField(max_length=7, choices=Status.choices, default=Status.ATIVO)
    status_associacao = models.CharField(max_length=7, choices=Status.choices, default=Status.ATIVO)

    placa = models.CharField(max_length=10, unique=True)
    ano_fabricacao = models.CharField(max_length=4)
    ano_modelo = models.CharField(max_length=4)
    cor = models.CharField(max_length=30)

    modelo = models.CharField(max_length=60)
    renavam = models.CharField(max_length=20, blank=True)
    chassi = models.CharField(max_length=30, blank=True)
    crlv = models.CharField(max_length=30, blank=True)
    telefone_veiculo = models.CharField(max_length=20, blank=True)
    validade_licenciamento = models.DateField(blank=True, null=True)
        
    frota = models.CharField(max_length=30, blank=True)
    proprietario_documento = models.CharField(max_length=30, blank=True)
    senha_veiculo = models.CharField(max_length=30, blank=True)
    senha_coacao = models.CharField(max_length=30, blank=True)
    proprietario_posse = models.CharField(max_length=60, blank=True)
    cidade_emplacamento = models.CharField(max_length=60, blank=True)

    estacao_rastreamento_operador = models.CharField(max_length=60, blank=True)
    estacao_rastreamento_supervisor = models.CharField(max_length=60, blank=True)
    gestor_frota = models.CharField(max_length=60, blank=True)

    pgr_minimo = models.CharField(max_length=30, blank=True)
    tecnologia_rastreador_principal = models.CharField(max_length=60, blank=True)
    rastreador_principal = models.CharField(max_length=60, blank=True)
    tipo_operacao = models.CharField(max_length=60, blank=True)
    rastreador_secundario = models.CharField(max_length=60, blank=True)
    tecnologia_rastreador_secundario = models.CharField(max_length=60, blank=True)

    sigla_base = models.CharField(max_length=20, blank=True)
    bases_operacionais = models.CharField(max_length=120, blank=True)

    escolta = models.CharField(max_length=3, choices=SimNao.choices, default=SimNao.NAO)

    antt = models.CharField(max_length=30, blank=True)
    validade_antt = models.DateField(blank=True, null=True)
    rntrc = models.CharField(max_length=30, blank=True)
    validade_rntrc = models.DateField(blank=True, null=True)
    tac = models.CharField(max_length=30, blank=True)
    validade_tac = models.DateField(blank=True, null=True)

    tara_kg = models.PositiveIntegerField(
        blank=True, null=True, validators=[MinValueValidator(0)], verbose_name="Tara (kg)"
    )
    cubagem = models.CharField(max_length=30, blank=True)  # texto livre (ex.: "m³" ou fórmulas)

    quarteirizando = models.CharField(max_length=3, choices=SimNao.choices, default=SimNao.NAO)
    veiculo_alto_desempenho = models.CharField(max_length=3, choices=SimNao.choices, default=SimNao.NAO)
    blindado = models.CharField(max_length=3, choices=SimNao.choices, default=SimNao.NAO)

    suspensao = models.CharField(max_length=4, choices=Suspensao.choices, blank=True)

    possui_lock = models.CharField(max_length=3, choices=SimNao.choices, default=SimNao.NAO)

    area_util_mm = models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(0)])
    largura_mm = models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(0)])
    altura_mm = models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(0)])
    capacidade_kg = models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(0)])

    tipo_equipamento = models.CharField(max_length=60, blank=True)
    tipo_combustivel = models.CharField(max_length=20, choices=Combustivel.choices, blank=True)

    observacao = models.TextField(blank=True)
    justificativa = models.TextField(blank=True)

    # Arquivo do CRLV (FileField para evitar dependência do Pillow)
    foto_crlv = models.FileField(upload_to="motos/crlv/", blank=True, null=True)

    # Auditoria
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Moto"
        verbose_name_plural = "Motos"
        ordering = ["placa"]
        indexes = [
            models.Index(fields=["placa"]),
            models.Index(fields=["status"]),
            models.Index(fields=["status_associacao"]),
        ]

    def __str__(self):
        return f"{self.placa} - {self.modelo}"

    def clean(self):
        # normalizações simples
        if self.placa:
            self.placa = self.placa.upper().replace(" ", "")
