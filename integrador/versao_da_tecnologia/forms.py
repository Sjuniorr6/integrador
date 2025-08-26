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
            'descricao': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite a descrição da tecnologia',
                'aria-label': 'Descrição da tecnologia'
            }),
            'versao': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: 1.0.0',
                'aria-label': 'Versão da tecnologia'
            }),
            'tempo_satelital': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tempo em segundos',
                'aria-label': 'Tempo satelital'
            }),
            'tempo_gprs': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tempo em segundos',
                'aria-label': 'Tempo GPRS'
            }),
            'homologado_para_risco': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'aria-label': 'Homologado para risco'
            }),
            'homologado_para_logistica': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'aria-label': 'Homologado para logística'
            }),
            'permitir_mensagem_livre': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'aria-label': 'Permitir mensagem livre'
            }),
            'tipo_de_comunicacao': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tipo de comunicação',
                'aria-label': 'Tipo de comunicação'
            }),
            'posicoes_calculo_posicionamento': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número de posições',
                'aria-label': 'Posições para cálculo de posicionamento'
            }),
            'comunicacao': forms.Select(attrs={
                'class': 'form-select',
                'aria-label': 'Tipo de comunicação'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adiciona form-control a todos os campos automaticamente
        for field_name, field in self.fields.items():
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = 'form-control'
