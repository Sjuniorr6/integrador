from django import forms
from .models import SaidaIscas

class SaidaIscasForm(forms.ModelForm):
    class Meta:
        model = SaidaIscas
        fields = ['cliente', 'quantidade', 'data_saida', 'lote_de', 'lote_ate', 'observacoes']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'data_saida': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'lote_de': forms.TextInput(attrs={'class': 'form-control'}),
            'lote_ate': forms.TextInput(attrs={'class': 'form-control'}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'cliente': 'Cliente',
            'quantidade': 'Quantidade',
            'data_saida': 'Data de Saída',
            'lote_de': 'Lote De',
            'lote_ate': 'Lote Até',
            'observacoes': 'Observações',
        }
