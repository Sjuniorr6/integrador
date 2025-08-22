from django import forms
from .models import CadastroDeMotivo


class CadastroDeMotivoForm(forms.ModelForm):
    class Meta:
        model = CadastroDeMotivo
        fields = [
            "descricao",
            "Tipo_de_motivo",
            "Status",
        ]
        labels = {
            "descricao": "Descrição",
            "Tipo_de_motivo": "Tipo de Motivo",
            "Status": "Status",
        }
        widgets = {
            "descricao": forms.TextInput(attrs={"class": "form-control", "placeholder": "Digite a descrição"}),
            "Tipo_de_motivo": forms.Select(attrs={"class": "form-select"}),
            "Status": forms.Select(attrs={"class": "form-select"}),
        }
