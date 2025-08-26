# estoque/models.py
from django.db import models
from django.utils import timezone
from datetime import date
from django.core.validators import MinValueValidator

class Cliente(models.Model):
    nome = models.CharField(
        max_length=150, 
        unique=True,
        verbose_name="Nome do Cliente"
    )
    data_criacao = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Data de Criação"
    )
    data_atualizacao = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Data de Atualização"
    )
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ["nome"]
    
    def __str__(self): 
        return self.nome
    
    def save(self, *args, **kwargs):
        if not self.data_criacao:
            self.data_criacao = timezone.now()
        self.data_atualizacao = timezone.now()
        super().save(*args, **kwargs)

class EntradaIscas(models.Model):
    cliente = models.ForeignKey(
        Cliente, 
        on_delete=models.PROTECT, 
        related_name='entradas_iscas',
        verbose_name="Cliente"
    )
    quantidade = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        verbose_name="Quantidade"
    )
    estoque_minimo = models.PositiveIntegerField(
        validators=[MinValueValidator(0)],
        verbose_name="Estoque Mínimo"
    )
    lote_de = models.CharField(
        max_length=50,
        verbose_name="Lote (De)"
    )
    lote_ate = models.CharField(
        max_length=50,
        verbose_name="Lote (Até)"
    )
    data_inicio_lancamento = models.DateField(
        default=date.today,
        verbose_name="Data Início Lançamento"
    )
    data_criacao = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Data de Criação"
    )
    data_atualizacao = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Data de Atualização"
    )
    
    class Meta:
        verbose_name = "Entrada de Iscas"
        verbose_name_plural = "Entradas de Iscas"
        ordering = ["-data_criacao"]
    
    def __str__(self):
        return f"{self.cliente.nome} - {self.quantidade} iscas (Lote {self.lote_de}-{self.lote_ate})"
    
    def save(self, *args, **kwargs):
        if not self.data_criacao:
            self.data_criacao = timezone.now()
        self.data_atualizacao = timezone.now()
        super().save(*args, **kwargs)
    
    @property
    def estoque_atual(self):
        """Calcula o estoque atual (quantidade - estoque mínimo)"""
        return max(0, self.quantidade - self.estoque_minimo)
    
    @property
    def status_estoque(self):
        """Retorna o status do estoque"""
        if self.quantidade <= self.estoque_minimo:
            return "Crítico"
        elif self.quantidade <= self.estoque_minimo * 1.5:
            return "Baixo"
        else:
            return "Normal"
    
    @property
    def status_estoque_color(self):
        """Retorna a cor do status do estoque"""
        colors = {
            "Crítico": "danger",
            "Baixo": "warning", 
            "Normal": "success"
        }
        return colors.get(self.status_estoque, "secondary")
