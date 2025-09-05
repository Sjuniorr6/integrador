# truck/forms.py
from django import forms
from .models import Truck

class TruckForm(forms.ModelForm):
    class Meta:
        model = Truck
        fields = '__all__'
        widgets = {
            'data_validade_licenciamento': forms.DateInput(attrs={'type': 'date'}),
            'validade_rntrc': forms.DateInput(attrs={'type': 'date'}),
            'validade_tac': forms.DateInput(attrs={'type': 'date'}),
            'criado_em': forms.HiddenInput(),
            'atualizado_em': forms.HiddenInput(),
        }
