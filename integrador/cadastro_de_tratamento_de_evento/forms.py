from django import forms
from .models import cadastro_de_tratamento_de_evento

class CadastroDeTratamentoDeEventoForm(forms.ModelForm):
    class Meta:
        model = cadastro_de_tratamento_de_evento
        fields = [
            'descricao',
            'tipo_evento',
            'procedimento',
            'responsavel',
            'tempo_estimado',
            'status',
        ]
        labels = {
            'descricao': 'Descrição',
            'tipo_evento': 'Tipo de Evento',
            'procedimento': 'Procedimento de Tratamento',
            'responsavel': 'Responsável',
            'tempo_estimado': 'Tempo Estimado',
            'status': 'Status',
        }
        widgets = {
            'descricao': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite a descrição do evento'
            }),
            'tipo_evento': forms.Select(attrs={
                'class': 'form-select',
                'aria-label': 'Selecione o tipo de evento'
            }),
            'procedimento': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descreva o procedimento de tratamento',
                'rows': 4
            }),
            'responsavel': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome do responsável'
            }),
            'tempo_estimado': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: 2 horas, 1 dia, etc.'
            }),
            'status': forms.Select(attrs={
                'class': 'form-select',
                'aria-label': 'Selecione o status'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap classes to all fields
        for field_name, field in self.fields.items():
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = 'form-control'
