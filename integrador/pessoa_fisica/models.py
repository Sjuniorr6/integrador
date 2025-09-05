# pessoas/models.py
from django.db import models
from django.core.validators import RegexValidator


class PessoaFisica(models.Model):
    # ---- selects ----
    class Status(models.TextChoices):
        ATIVO = "ATIVO", "ATIVO"
        INATIVO = "INATIVO", "INATIVO"

    class Sexo(models.TextChoices):
        MASCULINO = "MASCULINO", "MASCULINO"
        FEMININO = "FEMININO", "FEMININO"

    class EstadoCivil(models.TextChoices):
        SOLTEIRO = "SOLTEIRO", "SOLTEIRO"
        CASADO = "CASADO", "CASADO"
        DIVORCIADO = "DIVORCIADO", "DIVORCIADO"
        VIUVO = "VIÚVO", "VIÚVO"

    class Profissao(models.TextChoices):
        MOTORISTA = "MOTORISTA", "MOTORISTA"
        AJUDANTE = "AJUDANTE", "AJUDANTE"
        MOTORISTA_FOLGUISTA = "MOTORISTA FOLGUISTA", "MOTORISTA FOLGUISTA"
        OP_REFRIGERA = "OP DE REFRIGERA", "OP DE REFRIGERA"
        AJUD_CARGA_DESC = "AJUDANTE DE CARGA E DESCARGA", "AJUDANTE DE CARGA E DESCARGA"
        AUX_ADM_PLENO = "AUXILIAR ADM PLENO", "AUXILIAR ADM PLENO"

          # --- NOVO: tipo de pessoa ---
    class TipoPessoa(models.TextChoices):
        PESSOA_FISICA = "PF", "Pessoa Física"
        AJUDANTE = "AJ", "Ajudante"

    tipo_pessoa = models.CharField(
        max_length=2,
        choices=TipoPessoa.choices,
        default=TipoPessoa.PESSOA_FISICA,
        verbose_name="Tipo de Pessoa",
        db_index=True,
    )


    status = models.CharField(max_length=8, choices=Status.choices, default=Status.ATIVO)
    nome = models.CharField(max_length=200)

    # endereço/cabeçalho
    logradouro = models.CharField(max_length=200)
    numero = models.CharField(max_length=20)
    complemento = models.CharField(max_length=100, blank=True)
    matricula = models.CharField(max_length=50, blank=True)

    # documentos
    rg = models.CharField(max_length=20)
    orgao_emissor_rg = models.CharField(max_length=50)
    estado_emissor_rg = models.CharField(max_length=2)  
    data_emissao_rg = models.DateField(blank=True, null=True)

    cpf = models.CharField(
        max_length=11,
        unique=True,
        validators=[RegexValidator(r"^\d{11}$", "Informe 11 dígitos numéricos para o CPF.")],
    )

    # dados pessoais
    sexo = models.CharField(max_length=10, choices=Sexo.choices)
    naturalidade = models.CharField(max_length=100)
    data_nascimento = models.DateField()

    nome_pai = models.CharField(max_length=200)
    nome_mae = models.CharField(max_length=200)

    estado_civil = models.CharField(max_length=15, choices=EstadoCivil.choices)
    profissao = models.CharField(max_length=40, choices=Profissao.choices)

   
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Pessoa Física"
        verbose_name_plural = "Pessoas Físicas"
        ordering = ["nome"]
        indexes = [
            models.Index(fields=["nome"]),
            models.Index(fields=["cpf"]),
            models.Index(fields=["status"]),
            models.Index(fields=["tipo_pessoa"]),
        ]

    def __str__(self):
        return f"{self.nome} ({self.cpf})"

    def clean(self):
        # normaliza
        if self.cpf:
            self.cpf = "".join(ch for ch in self.cpf if ch.isdigit())
        if self.estado_emissor_rg:
            self.estado_emissor_rg = self.estado_emissor_rg.upper()
