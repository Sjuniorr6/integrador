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
            "descricao": forms.Textarea(attrs={
                "class": "form-control", 
                "placeholder": "Digite a descrição do motivo",
                "rows": 3
            }),
            "Tipo_de_motivo": forms.Select(attrs={
                "class": "form-select",
                "aria-label": "Selecione o tipo de motivo"
            }),
            "Status": forms.Select(attrs={
                "class": "form-select",
                "aria-label": "Selecione o status"
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap classes to all fields
        for field_name, field in self.fields.items():
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = 'form-control'
