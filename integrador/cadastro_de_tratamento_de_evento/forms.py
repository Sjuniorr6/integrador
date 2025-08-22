from django import forms
from .models import cadastro_de_tratamento_de_evento

class CadastroDeTratamentoDeEventoForm(forms.ModelForm):
    class Meta:
        model = cadastro_de_tratamento_de_evento
        fields = ['descricao']  # quais campos do model vão aparecer no form
