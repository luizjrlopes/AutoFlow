"""
test_agente.py — Testes do agente (classificação de intenção + loop completo).

Roda com: python -m unittest test_agente.py
"""
import os
import tempfile
import unittest

import banco
import agente


class TestClassificar(unittest.TestCase):
    def test_status_pedido(self):
        ferramenta, args = agente.classificar("qual o status do pedido #7?")
        self.assertEqual(ferramenta, "status_pedido")
        self.assertEqual(args, {"id": 7})

    def test_criar_pedido(self):
        ferramenta, args = agente.classificar("quero criar um pedido para Maria de Plano Pro")
        self.assertEqual(ferramenta, "criar_pedido")
        self.assertEqual(args["cliente"], "Maria")
        self.assertEqual(args["produto"], "Plano Pro")

    def test_consultar_cliente(self):
        ferramenta, args = agente.classificar("qual o telefone do cliente Joao")
        self.assertEqual(ferramenta, "consultar_cliente")

    def test_listar_produtos(self):
        ferramenta, args = agente.classificar("quais planos vocês tem?")
        self.assertEqual(ferramenta, "listar_produtos")

    def test_fallback(self):
        ferramenta, args = agente.classificar("bom dia")
        self.assertEqual(ferramenta, "fallback")
        self.assertEqual(args, {})


class TestResponder(unittest.TestCase):
    def setUp(self):
        self._tmpdir = tempfile.TemporaryDirectory()
        self._db_original = banco.DB
        self._doc_original = banco.DOC
        banco.DB = os.path.join(self._tmpdir.name, "dados.db")
        banco.DOC = os.path.join(self._tmpdir.name, "conversas.json")
        banco.inicializar()

    def tearDown(self):
        banco.DB = self._db_original
        banco.DOC = self._doc_original
        self._tmpdir.cleanup()

    def test_responder_consultar_cliente_existente(self):
        resultado = agente.responder("qual o telefone do cliente Maria", "whatsapp")
        self.assertEqual(resultado["ferramenta_usada"], "consultar_cliente")
        self.assertIn("Maria Silva", resultado["resposta"])

    def test_responder_registra_conversa(self):
        agente.responder("bom dia", "telegram")
        conversas = banco.listar_conversas()
        self.assertEqual(len(conversas), 1)
        self.assertEqual(conversas[0]["canal"], "telegram")
        self.assertEqual(conversas[0]["ferramenta_usada"], "fallback")


if __name__ == "__main__":
    unittest.main()
