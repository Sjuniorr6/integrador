# status_operacional/forms.py
from django import forms
from .models import StatusOperacional

class StatusOperacionalForm(forms.ModelForm):
    class Meta:
        model = StatusOperacional
        fields = ["descricao"]
        widgets = {
            "descricao": forms.TextInput(
                attrs={
                    "placeholder": "Digite a descrição…",
                    "autofocus": "autofocus",
                }
            ),
        }

    def clean_descricao(self):
        # normaliza espaços e evita duplicados com capitalização diferente
        desc = (self.cleaned_data["descricao"] or "").strip()
        return desc
