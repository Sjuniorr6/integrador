from django import forms
from .models import Cavalo

class CavaloForm(forms.ModelForm):
    class Meta:
        model = Cavalo
        fields = "__all__"
        widgets = {
            "validade_licenciamento": forms.DateInput(attrs={"type": "date"}),
            "validade_antt": forms.DateInput(attrs={"type": "date"}),
            "validade_rntrc": forms.DateInput(attrs={"type": "date"}),
            "validade_tac": forms.DateInput(attrs={"type": "date"}),
        }
        help_texts = {
            "foto_crlv": "Arquivos PDF/JPG/PNG. (Use FileField, não precisa de Pillow)",
        }
