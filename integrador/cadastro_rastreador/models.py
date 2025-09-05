from django.db import models
from django.core.validators import MinValueValidator, RegexValidator


class Rastreador(models.Model):
    class StatusRastreador(models.TextChoices):
        DESABILITADO = "DESABILITADO", "Desabilitado para sinal/espelhamento"
        ESP_RASTREANDO = "ESP_RASTREANDO", "Espelhado com rastreamento"
        ESP_SEM_RASTREIO = "ESP_SEM_RASTREIO", "Espelhado sem rastreamento"
        NORMAL = "NORMAL", "Normal"
        TRANSFERIDO = "TRANSFERIDO", "Transferido"

    class FaixaTemperatura(models.TextChoices):
        TESTE = "TESTE", "Teste"
        FAIXA_TESTE = "FAIXA_TESTE", "Faixa Teste"

    # Identificação
    nome = models.CharField(max_length=120, verbose_name="Rastreador", db_index=True)
    id_dispositivo = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="ID do dispositivo",
        help_text="Identificador único do equipamento na tecnologia.",
    )

    # Parametrização de tecnologia (mantidos como CharField para simplicidade/integração futura)
    versao_tecnologia = models.CharField(
        max_length=120, verbose_name="Versão da tecnologia", blank=True
    )
    conta_tecnologia = models.CharField(
        max_length=120,
        verbose_name="Conta de tecnologia",
        blank=True,
        help_text="Ex.: TELEMONITORADOS",
    )
    grupo_comandos = models.CharField(
        max_length=120,
        verbose_name="Grupo de comandos",
        blank=True,
        help_text="Seleção do grupo de comandos aplicável.",
    )

    # Timers / desempenho
    tempo_satelital_min = models.PositiveIntegerField(
        validators=[MinValueValidator(0)],
        verbose_name="Tempo Satelital (min)",
        default=0,
    )
    tempo_gprs_min = models.PositiveIntegerField(
        validators=[MinValueValidator(0)],
        verbose_name="Tempo GPRS (min)",
        default=0,
    )
    tempo_medio_posicionamento_min = models.PositiveIntegerField(
        validators=[MinValueValidator(0)],
        verbose_name="Tempo médio de posicionamento (min)",
        default=0,
    )
    fator_velocidade = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name="Fator de velocidade",
        blank=True,
        null=True,
    )

    # Faixas e status
    faixa_temperatura = models.CharField(
        max_length=20,
        choices=FaixaTemperatura.choices,
        verbose_name="Faixa de temperatura",
        blank=True,
    )
    status_rastreador = models.CharField(
        max_length=20,
        choices=StatusRastreador.choices,
        default=StatusRastreador.NORMAL,
        verbose_name="Status do rastreador",
        db_index=True,
    )

    # Flags
    ativo_ws = models.BooleanField(default=False, verbose_name="Ativo WS")
    ativo_gestao_risco = models.BooleanField(
        default=False, verbose_name="Ativo para gerenciamento de risco"
    )
    lista_branca_autotrac_ade = models.BooleanField(
        default=False, verbose_name="Lista branca do Autotrac ADE"
    )
    inteligencia_embarcada = models.BooleanField(
        default=False, verbose_name="Possui inteligência embarcada"
    )

    # Auditoria
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Rastreador"
        verbose_name_plural = "Rastreadores"
        ordering = ["nome"]
        indexes = [
            models.Index(fields=["nome"]),
            models.Index(fields=["id_dispositivo"]),
            models.Index(fields=["status_rastreador"]),
        ]

    def __str__(self):
        return f"{self.nome} ({self.id_dispositivo})"

    def clean(self):
        # normaliza id / tira espaços
        if self.id_dispositivo:
            self.id_dispositivo = self.id_dispositivo.strip()
