from django import forms
from .models import cadastrotecnologia

class CadastroTecnologiaForm(forms.ModelForm):
    class Meta:
        model = cadastrotecnologia
        fields = [
            'descricao',
            'versao',
            'tempo_satelital',
            'tempo_gprs',
            'homologado_para_risco',
            'homologado_para_logistica',
            'permitir_mensagem_livre',
            'tipo_de_comunicacao',
            'posicoes_calculo_posicionamento',
            'comunicacao',
        ]
        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'versao': forms.TextInput(attrs={'class': 'form-control'}),
            'tempo_satelital': forms.NumberInput(attrs={'class': 'form-control'}),
            'tempo_gprs': forms.NumberInput(attrs={'class': 'form-control'}),
            'homologado_para_risco': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'homologado_para_logistica': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'permitir_mensagem_livre': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'tipo_de_comunicacao': forms.TextInput(attrs={'class': 'form-control'}),
            'posicoes_calculo_posicionamento': forms.NumberInput(attrs={'class': 'form-control'}),
            'comunicacao': forms.Select(attrs={'class': 'form-select'}),
        }
