from django.db import models
from django.utils import timezone

# Create your models here.
class EstacaoRastreamento(models.Model):
    Rastreamento = [       
        ("Acompanhamento de Gerenci. de Risco e Logistica", "Acompanhamento de Gerenci. de Risco e Logistica"),
        ("Acompanhamento de Gerenciamento de Risco", "Acompanhamento de Gerenciamento de Risco"),
        ("Acompanhamento de Logistica", "Acompanhamento de Logistica"),
    ]

    Separacaodorastreamento = [
        ("Separado por embarcador transportador", "Separado por embarcador transportador"),
        ("Separado por Grau de Rsico", "Separado por Grau de Rsico"),
        ("Separado por Tecnologia", "Separado por Tecnologia"),
        ("Separado por tipo Manual", "Separado por Tipo Manual"),
        ("Separado por tipo de operação", "Separado por tipo de operação"),
    ]           
    
    descricao = models.CharField(max_length=500, verbose_name="Descrição")
    tipo_de_estacao_de_rastreamento = models.CharField(
        max_length=50, 
        choices=Rastreamento, 
        verbose_name="Tipo de Estação de Rastreamento"
    )
    Separacao_de_rastreamento = models.CharField(
        max_length=50, 
        choices=Separacaodorastreamento, 
        verbose_name="Separação de Rastreamento"
    )
    Numero_maximo_de_veiculos_da_estacao = models.IntegerField(
        verbose_name="Nº Máximo de Veículos da Estação"
    )
    Eventos_sem_tratamento = models.BooleanField(
        default=False, 
        verbose_name="Eventos sem Tratamento"
    )
    Mostrar_no_monitor_de_operacoes = models.BooleanField(
        default=False, 
        verbose_name="Mostrar no Monitor de Operações"
    )
    Estacao_de_alto_risco = models.BooleanField(
        default=False, 
        verbose_name="Estação de Alto Risco"
    )
    Usar_importancia_do_evento_para_redirecionar = models.BooleanField(
        default=False, 
        verbose_name="Usar Importância do Evento para Redirecionar"
    )
    data_criacao = models.DateTimeField(default=timezone.now, verbose_name="Data de Criação")
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")

    class Meta:
        verbose_name = "Estação de Rastreamento"
        verbose_name_plural = "Estações de Rastreamento"
        ordering = ['-data_criacao']

    def __str__(self):
        return f"{self.descricao[:50]}... - {self.tipo_de_estacao_de_rastreamento}"

    @property
    def is_alto_risco(self):
        return self.Estacao_de_alto_risco

    @property
    def tipo_estacao_color(self):
        """Return Bootstrap color class based on station type"""
        colors = {
            "Acompanhamento de Gerenci. de Risco e Logistica": "danger",
            "Acompanhamento de Gerenciamento de Risco": "warning",
            "Acompanhamento de Logistica": "primary",
        }
        return colors.get(self.tipo_de_estacao_de_rastreamento, "secondary")

    @property
    def status_indicators(self):
        """Return list of active status indicators"""
        indicators = []
        if self.Eventos_sem_tratamento:
            indicators.append(("Eventos sem Tratamento", "danger"))
        if self.Mostrar_no_monitor_de_operacoes:
            indicators.append(("Monitor de Operações", "info"))
        if self.Estacao_de_alto_risco:
            indicators.append(("Alto Risco", "warning"))
        if self.Usar_importancia_do_evento_para_redirecionar:
            indicators.append(("Redirecionamento por Importância", "success"))
        return indicators