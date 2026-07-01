"""
test_app.py — Smoke test da API HTTP (sobe o servidor de verdade numa porta livre).

Confirma, entre outras coisas, que POST /api/mensagem responde com "origem": "local"
quando N8N_WEBHOOK_URL não está configurada — ou seja, o padrão é 100% local.

Roda com: python -m unittest test_app.py
"""
import json
import os
import tempfile
import threading
import unittest
import urllib.error
import urllib.request
from http.server import ThreadingHTTPServer

import banco
import app


class TestAPISmoke(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._tmpdir = tempfile.TemporaryDirectory()
        cls._db_original = banco.DB
        cls._doc_original = banco.DOC
        banco.DB = os.path.join(cls._tmpdir.name, "dados.db")
        banco.DOC = os.path.join(cls._tmpdir.name, "conversas.json")
        banco.inicializar()

        app.N8N_WEBHOOK = ""  # garante comportamento 100% local no teste

        cls._server = ThreadingHTTPServer(("127.0.0.1", 0), app.Handler)
        cls._porta = cls._server.server_address[1]
        cls._thread = threading.Thread(target=cls._server.serve_forever, daemon=True)
        cls._thread.start()

    @classmethod
    def tearDownClass(cls):
        cls._server.shutdown()
        cls._server.server_close()
        banco.DB = cls._db_original
        banco.DOC = cls._doc_original
        cls._tmpdir.cleanup()

    def _url(self, caminho):
        return f"http://127.0.0.1:{self._porta}{caminho}"

    def _post(self, caminho, corpo):
        payload = json.dumps(corpo).encode("utf-8")
        req = urllib.request.Request(
            self._url(caminho),
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            resp = urllib.request.urlopen(req)
            return resp.status, json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            return e.code, json.loads(e.read().decode("utf-8"))

    def test_get_home_serve_html(self):
        resp = urllib.request.urlopen(self._url("/"))
        self.assertEqual(resp.status, 200)
        self.assertIn(b"<", resp.read())

    def test_get_clientes(self):
        resp = urllib.request.urlopen(self._url("/api/clientes"))
        self.assertEqual(resp.status, 200)
        dados = json.loads(resp.read().decode("utf-8"))
        self.assertIsInstance(dados, list)

    def test_post_mensagem_vazia_retorna_400(self):
        status, dados = self._post("/api/mensagem", {"mensagem": ""})
        self.assertEqual(status, 400)

    def test_post_mensagem_usa_agente_local_por_padrao(self):
        status, dados = self._post("/api/mensagem", {"mensagem": "quais planos vocês tem?"})
        self.assertEqual(status, 200)
        self.assertEqual(dados["origem"], "local")

    def test_post_clientes_cria_cliente(self):
        status, dados = self._post(
            "/api/clientes", {"nome": "Teste Smoke", "telefone": "5521999991111"}
        )
        self.assertEqual(status, 201)
        self.assertEqual(dados["nome"], "Teste Smoke")


if __name__ == "__main__":
    unittest.main()
