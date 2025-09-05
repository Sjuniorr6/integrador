# carretas/models.py
from django.db import models
from django.core.validators import RegexValidator

class Carreta(models.Model):
    # ----------------- choices -----------------
    class Status(models.TextChoices):
        ATIVO = "ATIVO", "Ativo"
        INATIVO = "INATIVO", "Inativo"

    class StatusAssociacao(models.TextChoices):
        ATIVO = "ATIVO", "Ativo"
        INATIVO = "INATIVO", "Inativo"

    class StatusCarga(models.TextChoices):
        CARREGADO = "CARREGADO", "Carregado"
        DESCARREGADO = "DESCARREGADO", "Descarregado"

    class UnidadeMedida(models.TextChoices):
        FARDO = "FARDO", "Fardo"
        LITRO = "LITRO", "Litro"
        QUILOGRAMA = "QUILOGRAMA", "Quilograma"
        PALLET = "PALLET", "Pallet"
        METRO_CUBICO = "METRO_CUBICO", "Metro cúbico"

    class SimNao(models.TextChoices):
        NAO = "NAO", "Não"
        SIM = "SIM", "Sim"

    class Suspensao(models.TextChoices):
        AR = "AR", "AR"
        HIDR = "HIDR", "Hidropneumática"
        MECA = "MECA", "Mecânica"
        ROSC = "ROSC", "Rosca"

    # ----------------- campos -----------------
    status = models.CharField(max_length=7, choices=Status.choices, default=Status.ATIVO)
    status_associacao = models.CharField(
        max_length=7, choices=StatusAssociacao.choices, default=StatusAssociacao.ATIVO,
        verbose_name="Status da associação"
    )

    placa = models.CharField(
        max_length=7, unique=True,
        validators=[RegexValidator(r"^[A-Z0-9]{7}$", "Informe 7 caracteres (placa).")],
    )

    ano_fabricacao = models.CharField(max_length=4, verbose_name="Ano de fabricação")
    ano_modelo = models.CharField(max_length=4, verbose_name="Ano do modelo")
    cor = models.CharField(max_length=30)
    modelo = models.CharField(max_length=60)
    renavam = models.CharField(max_length=20, unique=True)
    chassi = models.CharField(max_length=25)
    crlv = models.CharField(max_length=40, verbose_name="CRLV")
    telefone_veiculo = models.CharField(max_length=20, blank=True, verbose_name="Telefone do veículo")
    data_validade_licenciamento = models.DateField(verbose_name="Data de validade do licenciamento")

    frota = models.CharField(max_length=30, blank=True)
    gr_golden = models.CharField(max_length=30, blank=True, verbose_name="GR GOLDEN")
    senha_veiculo = models.CharField(max_length=30, blank=True)
    senha_coacao = models.CharField(max_length=30, blank=True, verbose_name="Senha de coação")
    proprietario = models.CharField(max_length=100)
    cidade_emplacamento = models.CharField(max_length=100, verbose_name="Cidade do emplacamento")

    fator_rpm = models.CharField(max_length=20, verbose_name="Fator de RPM", blank=True)
    fator_velocidade = models.CharField(max_length=20, verbose_name="Fator de velocidade", blank=True)
    numero_eixos = models.CharField(max_length=10, verbose_name="Número de eixos")

    status_carga = models.CharField(max_length=15, choices=StatusCarga.choices, default=StatusCarga.DESCARREGADO)
    unidade_medida = models.CharField(max_length=15, choices=UnidadeMedida.choices, default=UnidadeMedida.QUILOGRAMA)
    numero_pallets = models.CharField(max_length=10, blank=True, verbose_name="Número de pallets")
    pgr_minimo = models.CharField(max_length=30, blank=True, verbose_name="PGR Mínimo")

    tecnologia_rastreador_principal = models.CharField(max_length=60, blank=True)
    rastreador_principal = models.CharField(max_length=60, blank=True)
    tipo_carroceria = models.CharField(max_length=60, blank=True)

    tecnologia_rastreador_secundario = models.CharField(max_length=60, blank=True)
    rastreador_secundario = models.CharField(max_length=60, blank=True)

    sigla_base = models.CharField(max_length=20, blank=True)
    bases_operacionais = models.CharField(max_length=200, blank=True)

    antt = models.CharField(max_length=30, blank=True, verbose_name="ANTT")
    validade_antt = models.CharField(max_length=30, blank=True, verbose_name="Validade ANTT")  # conforme pedido (CharField)
    rntrc = models.CharField(max_length=30, blank=True, verbose_name="RNTRC")
    validade_rntrc = models.DateField(blank=True, null=True, verbose_name="Validade RNTRC")
    tac = models.CharField(max_length=30, blank=True, verbose_name="TAC")
    validade_tac = models.DateField(blank=True, null=True, verbose_name="Validade TAC")

    tara_kg = models.PositiveIntegerField(verbose_name="Tara (kg)", blank=True, null=True)
    cubagem = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    capacidade_kg = models.PositiveIntegerField(blank=True, null=True, verbose_name="Capacidade (kg)")

    quarteirizando = models.CharField(max_length=3, choices=SimNao.choices, default=SimNao.NAO)
    velocidade_alto_desempenho = models.CharField(
        max_length=3, choices=SimNao.choices, default=SimNao.NAO, verbose_name="Velocidade de alto desempenho"
    )
    blindado = models.CharField(max_length=3, choices=SimNao.choices, default=SimNao.NAO)
    suspensao = models.CharField(max_length=4, choices=Suspensao.choices, default=Suspensao.MECA)

    tipo_equipamento = models.CharField(max_length=60, blank=True)

    observacao = models.TextField(blank=True)
    justificativa = models.TextField(blank=True)

    foto_crlv = models.FileField(upload_to="carretas/crlv/", blank=True, null=True)


    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Carreta"
        verbose_name_plural = "Carretas"
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
            self.placa = self.placa.strip().upper()
        if self.renavam:
            self.renavam = self.renavam.strip()
