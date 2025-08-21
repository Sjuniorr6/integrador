# usuarios/tests.py
from django.test import TestCase, override_settings
from django.urls import reverse
from django.contrib.messages import get_messages
from django.contrib.auth import get_user_model
from django.db import IntegrityError

User = get_user_model()





@override_settings(PASSWORD_HASHERS=["django.contrib.auth.hashers.MD5PasswordHasher"])
class UserModelTests(TestCase):
    def test_create_user_hash_e_normalize_email(self):
        u = User.objects.create_user(email="sjuniorr6@gmail.com", password="django01", nome="Sidnei")
        self.assertEqual(u.email, "sjuniorr6@gmail.com")
        self.assertTrue(u.check_password("django01"))
        self.assertNotEqual(u.password, 'django01')
        
    def test_create_superuser_flags(self):
        admin = User.objects.create_superuser("admin@test.com", "Adm12345!", nome="Admin")
        self.assertTrue(admin.is_staff)
        self.assertTrue(admin.is_superuser)
        self.assertTrue(admin.is_active)
        
    def test_unique_email(self):
        User.objects.create_user("uniq@test.com", "Abc12345!", nome="A")
        with self.assertRaises(IntegrityError):
            User.objects.create_user("uniq@test.com", "Outra123!", nome="B")
            
    def test_is_verified_reflete_is_active(self):
        u = User.objects.create_user("v@test.com", "Abc12345!", nome="V", is_active=False)
        self.assertFalse(u.is_verified)
        u.is_active = True
        u.save(update_fields=["is_active"])
        self.assertTrue(User.objects.get(pk=u.pk).is_verified)


def _login_payload(email, password):
    """Payload para login usando email como username"""
    return {"username": email, "password": password}


def _register_payload(nome, email, p1, p2):
    """Payload para registro de usuário"""
    return {"nome": nome, "email": email, "password1": p1, "password2": p2}


@override_settings(PASSWORD_HASHERS=["django.contrib.auth.hashers.MD5PasswordHasher"])
class UserAuthTests(TestCase):
    def setUp(self):
        self.senha = "SenhaFort3!"
        self.email_ok = "user@test.com"
        self.user = User.objects.create_user(
            email=self.email_ok, 
            password=self.senha, 
            nome="Fulano", 
            is_active=True
        )

    def test_login_valido_redireciona_home_e_autentica(self):
        url = reverse("usuarios:login")
        r = self.client.post(url, _login_payload(self.email_ok, self.senha), follow=True)
        self.assertRedirects(r, reverse("usuarios:home"))
        self.assertTrue(r.wsgi_request.user.is_authenticated)
        self.assertEqual(r.wsgi_request.user.email, self.email_ok)
        msgs = list(get_messages(r.wsgi_request))
        self.assertTrue(any("Bem-vindo" in str(m) for m in msgs))

    def test_login_invalido_mantem_na_pagina_e_mostra_erro(self):
        url = reverse("usuarios:login")
        r = self.client.post(url, _login_payload(self.email_ok, "SenhaErrada!"))
        self.assertEqual(r.status_code, 200)
        self.assertFalse(r.wsgi_request.user.is_authenticated)
        msgs = list(get_messages(r.wsgi_request))
        self.assertTrue(any("Email ou senha incorretos" in str(m) for m in msgs))

    def test_login_usuario_inativo_falha(self):
        self.user.is_active = False
        self.user.save(update_fields=["is_active"])
        url = reverse("usuarios:login")
        r = self.client.post(url, _login_payload(self.email_ok, self.senha))
        self.assertEqual(r.status_code, 200)
        self.assertFalse(r.wsgi_request.user.is_authenticated)


@override_settings(PASSWORD_HASHERS=["django.contrib.auth.hashers.MD5PasswordHasher"])
class UserRegistroTests(TestCase):
    def test_register_get_abre_form(self):
        r = self.client.get(reverse("usuarios:register"))
        self.assertEqual(r.status_code, 200)

    def test_register_post_valido_cria_usuario_e_redireciona_para_login(self):
        payload = _register_payload("Novo", "novo@test.com", "OutraSenha123!", "OutraSenha123!")
        r = self.client.post(reverse("usuarios:register"), payload, follow=True)
        self.assertRedirects(r, reverse("usuarios:login"))
        self.assertTrue(User.objects.filter(email="novo@test.com").exists())
        msgs = list(get_messages(r.wsgi_request))
        self.assertTrue(any("Usuário criado com sucesso" in str(m) for m in msgs))

    def test_register_post_invalido_nao_cria_usuario(self):
        payload = _register_payload("X", "x@test.com", "S1!", "S2!")
        r = self.client.post(reverse("usuarios:register"), payload)
        self.assertEqual(r.status_code, 200)
        self.assertFalse(User.objects.filter(email="x@test.com").exists())
        msgs = list(get_messages(r.wsgi_request))
        self.assertTrue(any("Erro no formulário" in str(m) for m in msgs))
        