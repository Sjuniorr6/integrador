# cavalo/models.py
from django.db import models
from django.core.validators import MinValueValidator

class Cavalo(models.Model):
    # --- Choices ---
    class Status(models.TextChoices):
        ATIVO = "ATIVO", "Ativo"
        INATIVO = "INATIVO", "Inativo"

    class StatusAssociacao(models.TextChoices):
        ATIVO = "ATIVO", "Ativo"
        INATIVO = "INATIVO", "Inativo"

    class SimNao(models.TextChoices):
        NAO = "NAO", "NÃO"
        SIM = "SIM", "SIM"

    class Suspensao(models.TextChoices):
        AR = "AR", "AR"
        HIDR = "HIDR", "HIDROPNEUMÁTICA"
        MECA = "MECA", "MECÂNICA"
        ROSC = "ROSC", "ROSCA"

    class Combustivel(models.TextChoices):
        GASOLINA = "GASOLINA", "GASOLINA"
        DIESEL = "DIESEL", "DIESEL"
        GNV = "GNV", "GÁS NATURAL VEICULAR"
        ETANOL = "ETANOL", "ETANOL"

    # --- Campos principais / cabeçalho ---
    status = models.CharField(
        max_length=7, choices=Status.choices, default=Status.ATIVO, db_index=True
    )
    status_associacao = models.CharField(
        "Status da associação",
        max_length=7,
        choices=StatusAssociacao.choices,
        default=StatusAssociacao.ATIVO,
        db_index=True,
    )
    placa = models.CharField(max_length=10, unique=True)
    ano_fabricacao = models.CharField(max_length=4)
    ano_modelo = models.CharField(max_length=4)
    cor = models.CharField(max_length=30)
    modelo = models.CharField(max_length=60)
    renavam = models.CharField(max_length=20, blank=True)
    chassi = models.CharField(max_length=25, blank=True)
    crlv = models.CharField("CRLV", max_length=50, blank=True)
    telefone_veiculo = models.CharField(max_length=20, blank=True)
    validade_licenciamento = models.DateField(blank=True, null=True)
    frota = models.CharField(max_length=30, blank=True)

    proprietario_documento = models.CharField(max_length=30, blank=True)
    senha_veiculo = models.CharField(max_length=30, blank=True)
    senha_coacao = models.CharField(max_length=30, blank=True)
    proprietario = models.CharField(max_length=100, blank=True)
    cidade_emplacamento = models.CharField(max_length=60, blank=True)

    estacao_rastreamento_operador = models.CharField(max_length=60, blank=True)
    estacao_rastreamento_supervisor = models.CharField(max_length=60, blank=True)
    gestor_frota = models.CharField(max_length=60, blank=True)

    fator_rpm = models.CharField(max_length=20, blank=True)
    fator_velocidade = models.CharField(max_length=20, blank=True)
    numero_eixos = models.CharField(max_length=10, blank=True)
    pgr_minimo = models.CharField("PGR MÍNIMO", max_length=30, blank=True)

    tecnologia_rastreador_principal = models.CharField(max_length=60, blank=True)
    rastreador_principal = models.CharField(max_length=60, blank=True)
    tipo_operacao = models.CharField("Tipo de operação", max_length=60, blank=True)
    rastreador_secundario = models.CharField(max_length=60, blank=True)
    tecnologia_rastreador_secundario = models.CharField(max_length=60, blank=True)

    sigla_base = models.CharField(max_length=20, blank=True)
    bases_operacionais = models.CharField(max_length=120, blank=True)

    # --- Regulatórios / documentos ---
    escolta = models.CharField(
        max_length=3, choices=SimNao.choices, default=SimNao.NAO
    )
    antt = models.CharField(max_length=30, blank=True)
    validade_antt = models.DateField(blank=True, null=True)
    rntrc = models.CharField(max_length=30, blank=True)
    validade_rntrc = models.DateField(blank=True, null=True)
    tac = models.CharField(max_length=30, blank=True)
    validade_tac = models.DateField(blank=True, null=True)

    # --- Especificações físicas ---
    tara_kg = models.DecimalField(
        "Tara (kg)",
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        blank=True,
        null=True,
    )
    cubagem_m3 = models.DecimalField(
        "Cubagem (m³)",
        max_digits=10,
        decimal_places=3,
        validators=[MinValueValidator(0)],
        blank=True,
        null=True,
    )

    quarteirizando = models.CharField(
        max_length=3, choices=SimNao.choices, default=SimNao.NAO
    )
    veiculo_alto_desempenho = models.CharField(
        max_length=3, choices=SimNao.choices, default=SimNao.NAO
    )
    blindado = models.CharField(
        max_length=3, choices=SimNao.choices, default=SimNao.NAO
    )
    suspensao = models.CharField(
        max_length=4, choices=Suspensao.choices, blank=True
    )
    possui_lock = models.CharField(
        "Possui LOCK", max_length=3, choices=SimNao.choices, default=SimNao.NAO
    )

    area_util_mm = models.PositiveIntegerField(
        "Área útil (mm)", validators=[MinValueValidator(0)], blank=True, null=True
    )
    largura_mm = models.PositiveIntegerField(
        "Largura (mm)", validators=[MinValueValidator(0)], blank=True, null=True
    )
    altura_mm = models.PositiveIntegerField(
        "Altura (mm)", validators=[MinValueValidator(0)], blank=True, null=True
    )
    capacidade_kg = models.DecimalField(
        "Capacidade (kg)",
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        blank=True,
        null=True,
    )
    tipo_equipamento = models.CharField("Tipo de equipamento", max_length=60, blank=True)

    tipo_combustivel = models.CharField(
        "Tipo de combustível",
        max_length=12,
        choices=Combustivel.choices,
        blank=True,
    )

    # --- Observações / anexos ---
    observacao = models.TextField(blank=True)
    justificativa = models.TextField(blank=True)
    foto_crlv = models.FileField(
        upload_to="cavalos/crlv/", blank=True, null=True, verbose_name="Foto (CRLV)"
    )

    # --- Auditoria ---
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Cavalo"
        verbose_name_plural = "Cavalos"
        ordering = ["placa"]
        indexes = [
            models.Index(fields=["placa"]),
            models.Index(fields=["status"]),
            models.Index(fields=["status_associacao"]),
        ]

    def __str__(self):
        return f"{self.placa} - {self.modelo}"
