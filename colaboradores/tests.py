from django.test import TestCase
from django.urls import reverse
from .models import Colaborador
from datetime import date

class TestColaborador(TestCase):  # <-- mudou aqui, começa com "Test"

    def setUp(self):
        self.colaborador = Colaborador.objects.create(
            nome="João Silva",
            cpf="123.456.789-00",
            cargo="Técnico de Segurança",
            setor="Segurança do Trabalho",
            data_admissao=date.today(),
            ativo=True
        )

    def test_listagem_colaboradores(self):
        response = self.client.get(reverse("colaboradores:listar"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "João Silva")

    def test_detalhe_colaborador(self):
        response = self.client.get(reverse("colaboradores:detalhar", args=[self.colaborador.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "João Silva")

    def test_criar_colaborador(self):
        response = self.client.post(reverse("colaboradores:criar"), {
            "nome": "Maria Souza",
            "cpf": "987.654.321-00",
            "cargo": "Engenheira",
            "setor": "Obras",
            "data_admissao": "2023-01-01",
            "ativo": True
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Colaborador.objects.filter(nome="Maria Souza").exists())

    def test_editar_colaborador(self):
        response = self.client.post(reverse("colaboradores:editar", args=[self.colaborador.pk]), {
            "nome": "João Silva Alterado",
            "cpf": "123.456.789-00",
            "cargo": "Supervisor",
            "setor": "Segurança",
            "data_admissao": "2023-01-01",
            "ativo": True
        })
        self.assertEqual(response.status_code, 302)
        self.colaborador.refresh_from_db()
        self.assertEqual(self.colaborador.nome, "João Silva Alterado")

    def test_excluir_colaborador(self):
        response = self.client.post(reverse("colaboradores:excluir", args=[self.colaborador.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Colaborador.objects.filter(pk=self.colaborador.pk).exists())

# Create your tests here.
