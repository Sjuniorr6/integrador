from django import forms
from .models import cadastro


class CadastroForm(forms.ModelForm):
    class Meta:
        model = cadastro
        fields = [
            "descricao",
            "nivel_de_importancia",
            "acao_a_realizar",
            "processo_administrativo",
        ]
        labels = {
            "descricao": "Descrição",
            "nivel_de_importancia": "Nível de Importância",
            "acao_a_realizar": "Ação a Realizar",
            "processo_administrativo": "Processo Administrativo",
        }
        widgets = {
            "descricao": forms.Textarea(attrs={
                "class": "form-control", 
                "placeholder": "Digite a descrição do tipo de não conformidade",
                "rows": 3
            }),
            "nivel_de_importancia": forms.Select(attrs={
                "class": "form-select",
                "aria-label": "Selecione o nível de importância"
            }),
            "acao_a_realizar": forms.Textarea(attrs={
                "class": "form-control", 
                "placeholder": "Digite a ação a ser realizada",
                "rows": 3
            }),
            "processo_administrativo": forms.CheckboxInput(attrs={
                "class": "form-check-input"
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap classes to all fields
        for field_name, field in self.fields.items():
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = 'form-control'
