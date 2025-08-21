# tecnologias/forms.py
from django import forms
from .models import Tecnologia

class TecnologiaForm(forms.ModelForm):
    class Meta:
        model = Tecnologia
        fields = [
            "nome_da_conta",
            "ip_da_integracao",
            "tolerancia_tempo_sem_resposta",
            "tolerancia_de_envio_de_comandos",
            "quantidade_de_erros_simuntaneos",
            "tempo_aguardar_retorno",
            "tecnologia",
            "caminho_aplicacao",
            "status",
            "inicio_horario_tolerancia",
            "fim_horario_tolerancia",
            "empresa_contato",
            "monitorado_guardiao",
            "ignorado_monitor_integracoes",
            "enviar_comandos",
        ]
        widgets = {
            "inicio_horario_tolerancia": forms.TimeInput(format="%H:%M", attrs={"type": "time"}),
            "fim_horario_tolerancia": forms.TimeInput(format="%H:%M", attrs={"type": "time"}),
            "monitorado_guardiao": forms.CheckboxInput(),
            "ignorado_monitor_integracoes": forms.CheckboxInput(),
            "enviar_comandos": forms.CheckboxInput(),
        }

    # Helper único e nome CONSISTENTE com os clean_*
    def _non_negative(self, field):
        val = self.cleaned_data.get(field)
        if val is not None and val < 0:
            self.add_error(field, "Não pode ser negativo.")
        return val

    def clean_tolerancia_tempo_sem_resposta(self):
        return self._non_negative("tolerancia_tempo_sem_resposta")

    def clean_tolerancia_de_envio_de_comandos(self):
        return self._non_negative("tolerancia_de_envio_de_comandos")

    def clean_quantidade_de_erros_simuntaneos(self):
        return self._non_negative("quantidade_de_erros_simuntaneos")

    def clean_tempo_aguardar_retorno(self):
        return self._non_negative("tempo_aguardar_retorno")

    def clean(self):
        cleaned = super().clean()
        ini = cleaned.get("inicio_horario_tolerancia")
        fim = cleaned.get("fim_horario_tolerancia")
        if ini and fim and fim <= ini:
            self.add_error("fim_horario_tolerancia", "O fim deve ser depois do início.")
        return cleaned
