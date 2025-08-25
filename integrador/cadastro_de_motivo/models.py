from django.db import models
from django.utils import timezone

# Create your models here.
class CadastroDeMotivo(models.Model):
    Motivo = [
        ("Embarque cancelado", "Embarque cancelado"),
        ("Veiculo com problemas", "Veiculo com problemas"),
        ("Rastreador com problemas", "Rastreador com problemas"),
        ("Mercadoria com problemas", "Mercadoria com problemas"),
        ("Motorista não autorizado", "Motorista não autorizado"),
        ("Nota fiscal pendente", "Nota fiscal pendente"),
        ("Outros", "Outros"),
        ("Checklist não aprovado","Checklist não aprovado"),
        ("Alteração de status para multiplas viagens","Alteração de status para multiplas viagens"),
        ("Roteiro de atividades prioritário", "Roteiro de atividades prioritário"),
        ("Causa de sinistro", "Causa de sinistro"),
    ]

    Status = [
        ("Ativo", "Ativo"),
        ("Inativo", "Inativo"),
    ]

    descricao = models.CharField(max_length=500, verbose_name="Descrição")
    Tipo_de_motivo = models.CharField(max_length=50, choices=Motivo, verbose_name="Tipo de Motivo")
    Status = models.CharField(max_length=50, choices=Status, verbose_name="Status")
    data_criacao = models.DateTimeField(default=timezone.now, verbose_name="Data de Criação")
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")

    class Meta:
        verbose_name = "Cadastro de Motivo"
        verbose_name_plural = "Cadastros de Motivos"
        ordering = ['-data_criacao']

    def __str__(self):
        return f"{self.descricao[:50]}... - {self.Tipo_de_motivo}"

    @property
    def is_ativo(self):
        return self.Status == "Ativo"