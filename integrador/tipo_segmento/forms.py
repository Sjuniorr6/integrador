from django import forms
from .models import TipoSegmento

class TipoSegmentoForm(forms.ModelForm):
    class Meta:
        model = TipoSegmento
        fields = ['descricao', 'tipo_carroceria']
        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_carroceria': forms.TextInput(attrs={'class': 'form-control'}),
        }
