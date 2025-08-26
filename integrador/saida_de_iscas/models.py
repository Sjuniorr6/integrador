from django.db import models
from datetime import date
from django.core.validators import MinValueValidator
from entrada_de_iscas.models import Cliente

class SaidaIscas(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name='saidas_iscas')
    quantidade = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    data_saida = models.DateField(default=date.today)
    lote_de = models.CharField(max_length=50)
    lote_ate = models.CharField(max_length=50)
    observacoes = models.TextField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Saída de Iscas"
        verbose_name_plural = "Saídas de Iscas"
        ordering = ['-data_saida']
    
    def __str__(self):
        return f"Saída {self.quantidade} iscas para {self.cliente} em {self.data_saida}"
