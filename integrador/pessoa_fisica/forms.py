# pessoas/forms.py
from django import forms
from .models import PessoaFisica


class DateInput(forms.DateInput):
    input_type = "date"


class PessoaFisicaForm(forms.ModelForm):
    class Meta:
        model = PessoaFisica
        # Campos de auditoria fora do form
        exclude = ("criado_em", "atualizado_em")
        labels = {
            "tipo_pessoa": "Tipo de Pessoa",
            "status": "Status",
            "nome": "Nome",
            "logradouro": "Logradouro",
            "numero": "Número",
            "complemento": "Complemento",
            "matricula": "Matrícula",
            "rg": "RG",
            "orgao_emissor_rg": "Órgão Emissor RG",
            "estado_emissor_rg": "Estado Emissor RG (UF)",
            "data_emissao_rg": "Data Emissão RG",
            "cpf": "CPF",
            "sexo": "Sexo",
            "naturalidade": "Naturalidade",
            "data_nascimento": "Data de Nascimento",
            "nome_pai": "Nome do Pai",
            "nome_mae": "Nome da Mãe",
            "estado_civil": "Estado Civil",
            "profissao": "Profissão",
        }
        help_texts = {
            "cpf": "Somente números (11 dígitos).",
            "estado_emissor_rg": "UF com 2 letras (ex.: SP).",
        }
        widgets = {
            # selects (choices)
            "tipo_pessoa": forms.Select(attrs={"class": "form-select"}),
            "status": forms.Select(attrs={"class": "form-select"}),
            "sexo": forms.Select(attrs={"class": "form-select"}),
            "estado_civil": forms.Select(attrs={"class": "form-select"}),
            "profissao": forms.Select(attrs={"class": "form-select"}),

            # textos
            "nome": forms.TextInput(attrs={"class": "form-control", "maxlength": 200}),
            "logradouro": forms.TextInput(attrs={"class": "form-control"}),
            "numero": forms.TextInput(attrs={"class": "form-control"}),
            "complemento": forms.TextInput(attrs={"class": "form-control"}),
            "matricula": forms.TextInput(attrs={"class": "form-control"}),
            "rg": forms.TextInput(attrs={"class": "form-control"}),
            "orgao_emissor_rg": forms.TextInput(attrs={"class": "form-control"}),
            "estado_emissor_rg": forms.TextInput(attrs={"class": "form-control", "maxlength": 2}),
            "cpf": forms.TextInput(attrs={"class": "form-control", "maxlength": 14, "placeholder": "Somente números"}),
            "naturalidade": forms.TextInput(attrs={"class": "form-control"}),
            "nome_pai": forms.TextInput(attrs={"class": "form-control"}),
            "nome_mae": forms.TextInput(attrs={"class": "form-control"}),

            # datas
            "data_emissao_rg": DateInput(attrs={"class": "form-control"}),
            "data_nascimento": DateInput(attrs={"class": "form-control"}),
        }

    # Se quiser aceitar CPF COM máscara no formulário, descomente:
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields["cpf"].validators = []  # remove o RegexValidator do model no nível do form
    #     self.fields["cpf"].help_text = "CPF com ou sem máscara; será salvo só com dígitos."

    def clean_cpf(self):
        """Remove máscara e garante 11 dígitos."""
        raw = self.cleaned_data.get("cpf") or ""
        digits = "".join(ch for ch in raw if ch.isdigit())
        if len(digits) != 11:
            raise forms.ValidationError("CPF deve ter 11 dígitos (somente números).")
        return digits

    def clean_estado_emissor_rg(self):
        """Garante UF com 2 letras maiúsculas (ex.: SP)."""
        uf = (self.cleaned_data.get("estado_emissor_rg") or "").strip().upper()
        if uf and len(uf) != 2:
            raise forms.ValidationError("Informe a UF com 2 letras (ex.: SP).")
        return uf
