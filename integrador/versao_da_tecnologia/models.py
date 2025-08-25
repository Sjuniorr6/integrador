
from django.db import models
from django.utils import timezone

# Create your models here.
class cadastrotecnologia(models.Model):
    comunicacao = [
        ("Satelital", "Satelital"),
        ("Hibrido", "Hibrido"),
        ("Grupo GPRS", "Grupo GPRS"),
        ("Prime", "Prime"),
        ("LBS", "LBS"),
    ]

    descricao = models.CharField(max_length=250, verbose_name="Descrição")
    versao = models.CharField(max_length=50, verbose_name="Versão")
    tempo_satelital = models.IntegerField(verbose_name="Tempo Satelital")
    tempo_gprs = models.IntegerField(verbose_name="Tempo GPRS")
    homologado_para_risco = models.BooleanField(default=False, verbose_name="Homologado para Risco")
    homologado_para_logistica = models.BooleanField(default=False, verbose_name="Homologado para Logística")
    permitir_mensagem_livre = models.BooleanField(default=False, verbose_name="Permitir Mensagem Livre")
    tipo_de_comunicacao = models.CharField(max_length=250, verbose_name="Tipo de Comunicação")
    posicoes_calculo_posicionamento = models.IntegerField(verbose_name="Posições Cálculo Posicionamento")
    comunicacao = models.CharField(max_length=50, choices=comunicacao, verbose_name="Comunicação")
    data_criacao = models.DateTimeField(default=timezone.now, verbose_name="Data de Criação")
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")

    class Meta:
        verbose_name = "Versão da Tecnologia"
        verbose_name_plural = "Versões da Tecnologia"
        ordering = ['-data_criacao']

    def __str__(self):
        return f"{self.descricao} - v{self.versao}"

    @property
    def is_homologado_risco(self):
        return self.homologado_para_risco

    @property
    def is_homologado_logistica(self):
        return self.homologado_para_logistica

    @property
    def comunicacao_color(self):
        colors = {
            "Satelital": "primary",
            "Hibrido": "success", 
            "Grupo GPRS": "info",
            "Prime": "warning",
            "LBS": "secondary"
        }
        return colors.get(self.comunicacao, "light")