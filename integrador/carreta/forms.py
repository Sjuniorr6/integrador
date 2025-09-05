# carretas/forms.py
from django import forms
from .models import Carreta

class CarretaForm(forms.ModelForm):
    class Meta:
        model = Carreta
        fields = "__all__"
        widgets = {
            "data_validade_licenciamento": forms.DateInput(attrs={"type": "date"}),
            "validade_rntrc": forms.DateInput(attrs={"type": "date"}),
            "validade_tac": forms.DateInput(attrs={"type": "date"}),
            "observacao": forms.Textarea(attrs={"rows": 3}),
            "justificativa": forms.Textarea(attrs={"rows": 3}),
        }

    def clean_placa(self):
        return (self.cleaned_data.get("placa") or "").strip().upper()
