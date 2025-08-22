from django.db import models

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
        ("Alteração de status para multiplas viagens", "Alteração de status para multiplas viagens"),
        ("Roteiro de atividades prioritário", "Roteiro de atividades prioritário"),
        ("Causa de sinistro", "Causa de sinistro"),
        
    ]

    Status = [
        ("Ativo", "Ativo"),
        ("Inativo", "Inativo"),

    ]

    descricao = models.CharField(max_length=500)
    Tipo_de_motivo = models.CharField(max_length=50, choices=Motivo)
    Status = models.CharField(max_length=50, choices=Status)