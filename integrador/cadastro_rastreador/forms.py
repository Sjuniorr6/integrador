from django import forms
from .models import Rastreador


class RastreadorForm(forms.ModelForm):
    class Meta:
        model = Rastreador
        fields = [
            "nome",
            "id_dispositivo",
            "versao_tecnologia",
            "conta_tecnologia",
            "grupo_comandos",
            "tempo_satelital_min",
            "tempo_gprs_min",
            "tempo_medio_posicionamento_min",
            "fator_velocidade",
            "faixa_temperatura",
            "status_rastreador",
            "ativo_ws",
            "ativo_gestao_risco",
            "lista_branca_autotrac_ade",
            "inteligencia_embarcada",
        ]
        widgets = {
            "tempo_satelital_min": forms.NumberInput(attrs={"min": 0}),
            "tempo_gprs_min": forms.NumberInput(attrs={"min": 0}),
            "tempo_medio_posicionamento_min": forms.NumberInput(attrs={"min": 0}),
            "fator_velocidade": forms.NumberInput(attrs={"step": "0.01"}),
        }

    def clean_nome(self):
        return self.cleaned_data["nome"].strip()

    def clean_conta_tecnologia(self):
        v = self.cleaned_data.get("conta_tecnologia", "")
        return v.strip()

    def clean_grupo_comandos(self):
        v = self.cleaned_data.get("grupo_comandos", "")
        return v.strip()
