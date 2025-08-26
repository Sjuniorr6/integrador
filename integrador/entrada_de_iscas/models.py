# estoque/models.py
from django.db import models
from datetime import date
from django.core.validators import MinValueValidator

class Cliente(models.Model):
    nome = models.CharField(max_length=150, unique=True)
    def __str__(self): return self.nome

class EntradaIscas(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name='entradas_iscas')
    quantidade = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    estoque_minimo = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    lote_de = models.CharField(max_length=50)
    lote_ate = models.CharField(max_length=50)
    data_inicio_lancamento = models.DateField(default=date.today)
