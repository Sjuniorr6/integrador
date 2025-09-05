from django import forms
from .models import Moto

class MotoForm(forms.ModelForm):
    class Meta:
        model = Moto
        fields = "__all__"
        widgets = {
            "validade_licenciamento": forms.DateInput(attrs={"type": "date"}),
            "validade_antt": forms.DateInput(attrs={"type": "date"}),
            "validade_rntrc": forms.DateInput(attrs={"type": "date"}),
            "validade_tac": forms.DateInput(attrs={"type": "date"}),
        }
        help_texts = {
            "foto_crlv": "Anexe PDF/JPG/PNG do CRLV.",
        }
