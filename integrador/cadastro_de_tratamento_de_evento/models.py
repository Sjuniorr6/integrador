from django.db import models
from django.utils import timezone

# Create your models here.
class cadastro_de_tratamento_de_evento(models.Model):
    TIPO_EVENTO_CHOICES = [
        ("Emergência", "Emergência"),
        ("Urgente", "Urgente"),
        ("Normal", "Normal"),
        ("Baixa Prioridade", "Baixa Prioridade"),
    ]
    
    STATUS_CHOICES = [
        ("Ativo", "Ativo"),
        ("Inativo", "Inativo"),
    ]
    
    descricao = models.CharField(max_length=250, verbose_name="Descrição")
    tipo_evento = models.CharField(
        max_length=50, 
        choices=TIPO_EVENTO_CHOICES,
        verbose_name="Tipo de Evento"
    )
    procedimento = models.TextField(verbose_name="Procedimento de Tratamento")
    responsavel = models.CharField(max_length=100, verbose_name="Responsável")
    tempo_estimado = models.CharField(max_length=50, verbose_name="Tempo Estimado")
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES,
        default="Ativo",
        verbose_name="Status"
    )
    data_criacao = models.DateTimeField(default=timezone.now, verbose_name="Data de Criação")
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")

    class Meta:
        verbose_name = "Tratamento de Evento"
        verbose_name_plural = "Tratamentos de Eventos"
        ordering = ['-data_criacao']

    def __str__(self):
        return f"{self.descricao[:50]}... - {self.tipo_evento}"

    @property
    def is_ativo(self):
        return self.status == "Ativo"

    @property
    def tipo_evento_color(self):
        """Return Bootstrap color class based on event type"""
        colors = {
            "Emergência": "danger",
            "Urgente": "warning",
            "Normal": "primary", 
            "Baixa Prioridade": "success"
        }
        return colors.get(self.tipo_evento, "secondary")
