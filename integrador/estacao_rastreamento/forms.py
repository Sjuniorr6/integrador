from django import forms
from .models import EstacaoRastreamento


class EstacaoRastreamentoForm(forms.ModelForm):
    class Meta:
        model = EstacaoRastreamento
        fields = [
            "descricao",
            "tipo_de_estacao_de_rastreamento",
            "Separacao_de_rastreamento",
            "Numero_maximo_de_veiculos_da_estacao",
            "Eventos_sem_tratamento",
            "Mostrar_no_monitor_de_operacoes",
            "Estacao_de_alto_risco",
            "Usar_importancia_do_evento_para_redirecionar",
        ]
        labels = {
            "descricao": "Descrição",
            "tipo_de_estacao_de_rastreamento": "Tipo de Estação de Rastreamento",
            "Separacao_de_rastreamento": "Separação de Rastreamento",
            "Numero_maximo_de_veiculos_da_estacao": "Nº Máximo de Veículos da Estação",
            "Eventos_sem_tratamento": "Eventos sem tratamento",
            "Mostrar_no_monitor_de_operacoes": "Mostrar no monitor de operações",
            "Estacao_de_alto_risco": "Estação de alto risco",
            "Usar_importancia_do_evento_para_redirecionar": "Usar importância do evento para redirecionar",
        }
        widgets = {
            "descricao": forms.Textarea(attrs={
                "class": "form-control", 
                "placeholder": "Digite a descrição da estação de rastreamento",
                "rows": 3
            }),
            "tipo_de_estacao_de_rastreamento": forms.Select(attrs={
                "class": "form-select",
                "aria-label": "Selecione o tipo de estação de rastreamento"
            }),
            "Separacao_de_rastreamento": forms.Select(attrs={
                "class": "form-select",
                "aria-label": "Selecione o tipo de separação de rastreamento"
            }),
            "Numero_maximo_de_veiculos_da_estacao": forms.NumberInput(attrs={
                "class": "form-control", 
                "min": 1,
                "placeholder": "Ex: 10"
            }),
            "Eventos_sem_tratamento": forms.CheckboxInput(attrs={
                "class": "form-check-input"
            }),
            "Mostrar_no_monitor_de_operacoes": forms.CheckboxInput(attrs={
                "class": "form-check-input"
            }),
            "Estacao_de_alto_risco": forms.CheckboxInput(attrs={
                "class": "form-check-input"
            }),
            "Usar_importancia_do_evento_para_redirecionar": forms.CheckboxInput(attrs={
                "class": "form-check-input"
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = 'form-control'
