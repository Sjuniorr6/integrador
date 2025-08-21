# usuarios/models.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import MinLengthValidator

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra):
        if not email:
            raise ValueError("Email é obrigatório")
        email = self.normalize_email(email).strip().lower()
        user = self.model(email=email, **extra)
        user.set_password(password)  # HASH seguro
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra):
        extra.setdefault("is_staff", True)
        extra.setdefault("is_superuser", True)
        extra.setdefault("is_active", True)
        return self.create_user(email, password, **extra)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name="Email", help_text="Email único para login")
    nome = models.CharField(
        max_length=50, verbose_name="Nome",
        validators=[MinLengthValidator(2, "Nome deve ter pelo menos 2 caracteres")]
    )
    is_active = models.BooleanField(default=True, verbose_name="Ativo", help_text="Usuário ativo")
    is_staff = models.BooleanField(default=False, verbose_name="Staff", help_text="Acesso ao admin do Django")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última Atualização")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nome"]  # no createsuperuser pedirá nome

    objects = UserManager()

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.nome} ({self.email})"

    def get_full_name(self):
        return self.nome

    def get_short_name(self):
        return self.nome.split()[0] if self.nome else self.email

    @property
    def is_verified(self):
        """Retorna True se o usuário já está ativo (email verificado)."""
        return self.is_active
