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
            "descricao": forms.TextInput(attrs={"class": "form-control", "placeholder": "Digite a descrição"}),
            "nivel_de_importancia": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ex: Alta, Média, Baixa"}),
            "acao_a_realizar": forms.TextInput(attrs={"class": "form-control", "placeholder": "Digite a ação"}),
            "processo_administrativo": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
