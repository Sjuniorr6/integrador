# estoque/forms.py
from django import forms
from django.core.exceptions import ValidationError
from .models import Cliente, EntradaIscas


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nome"]
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
        }


class EntradaIscasForm(forms.ModelForm):
    class Meta:
        model = EntradaIscas
        fields = [
            "cliente",
            "quantidade",
            "estoque_minimo",
            "lote_de",
            "lote_ate",
            "data_inicio_lancamento",
        ]
        labels = {
            "cliente": "Cliente",
            "quantidade": "Quantidade",
            "estoque_minimo": "Estoque Mínimo",
            "lote_de": "Lote (De)",
            "lote_ate": "Lote (Até)",
            "data_inicio_lancamento": "Data Início Lançamento",
        }
        widgets = {
            "cliente": forms.Select(attrs={"class": "form-select"}),                 # dropdown
            "quantidade": forms.NumberInput(attrs={"class": "form-control", "min": 1}),
            "estoque_minimo": forms.NumberInput(attrs={"class": "form-control", "min": 0}),
            "lote_de": forms.TextInput(attrs={"class": "form-control"}),
            "lote_ate": forms.TextInput(attrs={"class": "form-control"}),
            "data_inicio_lancamento": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # garante lista de clientes ordenada
        self.fields["cliente"].queryset = Cliente.objects.order_by("nome")

    def clean(self):
        """
        Validação opcional:
        - Se 'lote_de' e 'lote_ate' forem numéricos, garante que (até) >= (de).
        - Garante que estoque_minimo não seja maior que a quantidade (se quiser manter essa regra).
        """
        cleaned = super().clean()
        lote_de = cleaned.get("lote_de")
        lote_ate = cleaned.get("lote_ate")
        quantidade = cleaned.get("quantidade")
        estoque_minimo = cleaned.get("estoque_minimo")

        if lote_de and lote_ate and lote_de.isdigit() and lote_ate.isdigit():
            if int(lote_ate) < int(lote_de):
                raise ValidationError("Lote (Até) não pode ser menor que Lote (De).")

        if quantidade is not None and estoque_minimo is not None:
            if estoque_minimo > quantidade:
                raise ValidationError("Estoque mínimo não pode ser maior que a quantidade.")
        return cleaned
