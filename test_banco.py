"""
test_banco.py — Testes da camada de dados (SQLite relacional + JSON documento).

Roda com: python -m unittest test_banco.py
"""
import os
import tempfile
import unittest

import banco


class TestBanco(unittest.TestCase):
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

    def test_inicializar_popula_dados_de_exemplo(self):
        clientes = banco.listar_clientes()
        self.assertEqual(len(clientes), 2)
        self.assertEqual(clientes[0]["nome"], "Maria Silva")

    def test_criar_e_buscar_cliente(self):
        novo_id = banco.criar_cliente("Ana Souza", "5521999990099")
        cliente = banco.buscar_cliente("Ana")
        self.assertEqual(cliente["id"], novo_id)
        self.assertEqual(cliente["telefone"], "5521999990099")

    def test_buscar_cliente_inexistente(self):
        self.assertIsNone(banco.buscar_cliente("Ninguem"))

    def test_criar_pedido_e_listar_com_join(self):
        cliente_id = banco.criar_cliente("Carlos Reis", "5521999990088")
        pedido_id = banco.criar_pedido(cliente_id, "Plano Pro")
        pedidos = banco.listar_pedidos()
        pedido = next(p for p in pedidos if p["id"] == pedido_id)
        self.assertEqual(pedido["cliente"], "Carlos Reis")
        self.assertEqual(pedido["produto"], "Plano Pro")
        self.assertEqual(pedido["status"], "recebido")

    def test_buscar_pedido(self):
        cliente_id = banco.criar_cliente("Debora Lima", "5521999990077")
        pedido_id = banco.criar_pedido(cliente_id, "Consultoria")
        pedido = banco.buscar_pedido(pedido_id)
        self.assertEqual(pedido["cliente"], "Debora Lima")

    def test_buscar_pedido_inexistente(self):
        self.assertIsNone(banco.buscar_pedido(99999))

    def test_registrar_e_listar_conversas(self):
        banco.registrar_conversa("whatsapp", "oi", "ola!", "fallback")
        conversas = banco.listar_conversas()
        self.assertEqual(len(conversas), 1)
        self.assertEqual(conversas[0]["mensagem"], "oi")


if __name__ == "__main__":
    unittest.main()
