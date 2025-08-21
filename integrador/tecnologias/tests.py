from django.test import TestCase

# Create your tests here.
# tests.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from datetime import time

from .models import Tecnologia
from .forms import TecnologiaForm

User = get_user_model()



class TecnologiaBaseTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="t@t.com", password="pass1234")
        self.client.force_login(self.user) 
        # dados válidos base para criar formulário/objetos
        self.valid_payload = {
            "nome_da_conta": "Conta A",
            "ip_da_integracao": "10.0.0.1",
            "tolerancia_tempo_sem_resposta": 30,
            "tolerancia_de_envio_de_comandos": 15,
            "quantidade_de_erros_simuntaneos": 3,
            "tempo_aguardar_retorno": 60,
            "tecnologia": "omnilink",  # evitar acentos no post
            "caminho_aplicacao": "/opt/app",
            "status": "ativo",
            "inicio_horario_tolerancia": "08:00",
            "fim_horario_tolerancia": "18:00",
            "empresa_contato": "Empresa X",
            "monitorado_guardiao": True,
            "ignorado_monitor_integracoes": False,
            "enviar_comandos": True,
        }

    def create_tecnologia(self, **overrides):
        data = dict(self.valid_payload)
        data.update(overrides)
        return Tecnologia.objects.create(
            nome_da_conta=data["nome_da_conta"],
            ip_da_integracao=data["ip_da_integracao"],
            tolerancia_tempo_sem_resposta=data["tolerancia_tempo_sem_resposta"],
            tolerancia_de_envio_de_comandos=data["tolerancia_de_envio_de_comandos"],
            quantidade_de_erros_simuntaneos=data["quantidade_de_erros_simuntaneos"],
            tempo_aguardar_retorno=data["tempo_aguardar_retorno"],
            tecnologia=data["tecnologia"],
            caminho_aplicacao=data["caminho_aplicacao"],
            status=data["status"],
            inicio_horario_tolerancia=time.fromisoformat(
                data["inicio_horario_tolerancia"]
            ),
            fim_horario_tolerancia=time.fromisoformat(
                data["fim_horario_tolerancia"]
            ),
            empresa_contato=data["empresa_contato"],
            monitorado_guardiao=data["monitorado_guardiao"],
            ignorado_monitor_integracoes=data["ignorado_monitor_integracoes"],
            enviar_comandos=data["enviar_comandos"],
        )


class TecnologiaFormTests(TecnologiaBaseTest):
    def test_form_valid_with_checkbox_and_choices(self):
        form = TecnologiaForm(data=self.valid_payload)
        self.assertTrue(form.is_valid(), form.errors)

    def test_form_invalid_when_end_before_start(self):
        bad = dict(self.valid_payload)
        bad["inicio_horario_tolerancia"] = "18:00"
        bad["fim_horario_tolerancia"] = "08:00"
        form = TecnologiaForm(data=bad)
        self.assertFalse(form.is_valid())
        self.assertIn("fim_horario_tolerancia", form.errors)

    def test_form_invalid_negative_numbers(self):
        for field in [
            "tolerancia_tempo_sem_resposta",
            "tolerancia_de_envio_de_comandos",
            "quantidade_de_erros_simuntaneos",
            "tempo_aguardar_retorno",
        ]:
            bad = dict(self.valid_payload)
            bad[field] = -1
            form = TecnologiaForm(data=bad)
            self.assertFalse(form.is_valid(), f"{field} deveria ser inválido")
            self.assertIn(field, form.errors)

    def test_form_invalid_wrong_choice(self):
        bad = dict(self.valid_payload)
        bad["tecnologia"] = "nao-existe"
        form = TecnologiaForm(data=bad)
        self.assertFalse(form.is_valid())
        self.assertIn("tecnologia", form.errors)

    def test_boolean_fields_checkbox_widgets(self):
        # Garantir que campos booleanos venham como CheckboxInput
        form = TecnologiaForm()
        from django.forms import CheckboxInput

        self.assertIsInstance(form.fields["monitorado_guardiao"].widget, CheckboxInput)
        self.assertIsInstance(
            form.fields["ignorado_monitor_integracoes"].widget, CheckboxInput
        )
        self.assertIsInstance(form.fields["enviar_comandos"].widget, CheckboxInput)


class TecnologiaModelTests(TecnologiaBaseTest):
    def test_create_model(self):
        obj = self.create_tecnologia()
        self.assertEqual(Tecnologia.objects.count(), 1)
        self.assertEqual(obj.nome_da_conta, "Conta A")
        self.assertTrue(obj.monitorado_guardiao)
        self.assertEqual(obj.tecnologia, "omnilink")
        self.assertEqual(obj.status, "ativo")


class TecnologiaViewTests(TecnologiaBaseTest):
    def test_list_requires_login(self):
        # Logout primeiro para garantir que não está logado
        self.client.logout()
        resp = self.client.get(reverse("lista_tecnologias"))
        self.assertIn(resp.status_code, (302, 301))  # redirect to login

    def test_list_logged_in(self):
        self.client.login(email="t@t.com", password="pass1234")
        # popular para paginação
        for i in range(12):
            self.create_tecnologia(nome_da_conta=f"Conta {i}")
        resp = self.client.get(reverse("lista_tecnologias"))
        self.assertEqual(resp.status_code, 200)
        self.assertIn("page_obj", resp.context)
        self.assertEqual(resp.context["page_obj"].paginator.per_page, 10)

    def test_create_view_success(self):
        self.client.login(email="t@t.com", password="pass1234")
        resp = self.client.post(reverse("criar_tecnologia"), data=self.valid_payload)
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(Tecnologia.objects.count(), 1)
        # checar mensagem de sucesso
        messages = list(get_messages(resp.wsgi_request))
        self.assertTrue(any("cadastrada" in m.message for m in messages))

    def test_create_view_invalid(self):
        self.client.login(email="t@t.com", password="pass1234")
        bad = dict(self.valid_payload)
        bad["fim_horario_tolerancia"] = "07:00"  # antes do início (08:00)
        resp = self.client.post(reverse("criar_tecnologia"), data=bad)
        self.assertEqual(resp.status_code, 200)  # re-render do form
        self.assertContains(resp, "deve ser depois do início")
        self.assertEqual(Tecnologia.objects.count(), 0)

    def test_detail_view(self):
        self.client.login(email="t@t.com", password="pass1234")
        obj = self.create_tecnologia()
        resp = self.client.get(reverse("detalhar_tecnologia", args=[obj.pk]))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, obj.nome_da_conta)

    def test_update_view_success(self):
        self.client.login(email="t@t.com", password="pass1234")
        obj = self.create_tecnologia()
        payload = dict(self.valid_payload)
        payload["nome_da_conta"] = "Conta Alterada"
        resp = self.client.post(reverse("editar_tecnologia", args=[obj.pk]), data=payload)
        self.assertEqual(resp.status_code, 302)
        obj.refresh_from_db()
        self.assertEqual(obj.nome_da_conta, "Conta Alterada")
        messages = list(get_messages(resp.wsgi_request))
        self.assertTrue(any("atualizada" in m.message for m in messages))

    def test_delete_view_success(self):
        self.client.login(email="t@t.com", password="pass1234")
        obj = self.create_tecnologia()
        # Primeiro acessa a página de confirmação
        resp = self.client.get(reverse("excluir_tecnologia", args=[obj.pk]))
        self.assertEqual(resp.status_code, 200)
        # Depois confirma a exclusão
        resp = self.client.post(reverse("excluir_tecnologia", args=[obj.pk]))
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(Tecnologia.objects.count(), 0)
        messages = list(get_messages(resp.wsgi_request))
        self.assertTrue(any("deletada" in m.message for m in messages))

    def test_boolean_checkbox_handling(self):
        """Checa que 'on' e ausência funcionam nos booleans."""
        self.client.login(email="t@t.com", password="pass1234")
        payload = dict(self.valid_payload)
        # desmarca um dos checkboxes removendo-o do POST
        payload.pop("ignorado_monitor_integracoes", None)
        resp = self.client.post(reverse("criar_tecnologia"), data=payload)
        self.assertEqual(resp.status_code, 302)
        obj = Tecnologia.objects.get()
        self.assertTrue(obj.monitorado_guardiao)          # enviado como True
        self.assertFalse(obj.ignorado_monitor_integracoes)  # ausente -> False
        self.assertTrue(obj.enviar_comandos)              # enviado como True
