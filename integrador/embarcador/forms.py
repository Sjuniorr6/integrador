# embarcadores/forms.py
from django import forms
from .models import Embarcador

class EmbarcadorForm(forms.ModelForm):
    class Meta:
        model = Embarcador
        fields = [
            "status",
            "nome",
            "documento",
            "razao_social",
            "inscricao_estadual",
            "site",
        ]
        labels = {
            "status": "Status",
            "nome": "Nome",
            "documento": "Documento (CPF/CNPJ)",
            "razao_social": "Razão Social",
            "inscricao_estadual": "Inscrição Estadual",
            "site": "Site",
        }
        widgets = {
            "status": forms.Select(attrs={"class": "form-select"}),
            "nome": forms.TextInput(attrs={"class": "form-control", "maxlength": 200}),
            "documento": forms.TextInput(attrs={
                "class": "form-control",
                "maxlength": 18,  # espaço para máscara, se usar no front
                "placeholder": "Somente números (11=CPF, 14=CNPJ)",
            }),
            "razao_social": forms.TextInput(attrs={"class": "form-control"}),
            "inscricao_estadual": forms.TextInput(attrs={"class": "form-control"}),
            "site": forms.URLInput(attrs={"class": "form-control", "placeholder": "https://..."}),
        }
        help_texts = {
            "documento": "Informe CPF (11) ou CNPJ (14) dígitos.",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



    def clean_documento(self):
        
        doc = self.cleaned_data.get("documento", "") or ""
        digits = "".join(ch for ch in doc if ch.isdigit())

        if len(digits) not in (11, 14):
            raise forms.ValidationError("Informe CPF (11) ou CNPJ (14) dígitos.")

        return digits
