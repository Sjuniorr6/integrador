# nao_conformidade_veiculo/forms.py
from django import forms
from django.forms import ModelForm
from .models import NaoConformidadeVeiculo

class DateInput(forms.DateInput):
    input_type = "date"

class NaoConformidadeVeiculoForm(ModelForm):
    class Meta:
        model = NaoConformidadeVeiculo
        fields = [
            "cliente", "viagem", "veiculo", "frota",
            "suspenso_desde", "situacao", "agendamento_liberacao",
            "transportador", "problemas_mecanicos", "problemas_rastreador",
            "observacao", "motivo_interno",
        ]
        widgets = {
            "suspenso_desde": DateInput(attrs={"class": "form-control"}),
            "agendamento_liberacao": DateInput(attrs={"class": "form-control"}),
            "problemas_mecanicos": forms.Textarea(attrs={"rows": 3}),
            "problemas_rastreador": forms.Textarea(attrs={"rows": 3}),
            "observacao": forms.Textarea(attrs={"rows": 3}),
            "motivo_interno": forms.Textarea(attrs={"rows": 3}),
        }
        labels = {
            "agendamento_liberacao": "Agendamento de liberação",
        }
