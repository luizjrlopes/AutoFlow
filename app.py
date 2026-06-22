"""
app.py — Servidor do AutoFlow IA (somente biblioteca padrão do Python).

Sobe uma API REST e serve o frontend (chat estilo WhatsApp/Telegram).

Como rodar:
    python app.py
Depois abra no navegador:
    http://localhost:8000

Mapa rápido (cada item é um requisito da vaga):
  • API REST .............. métodos GET/POST, JSON e status codes (abaixo)
  • Automação / webhook ... POST /api/mensagem simula uma mensagem chegando
                            do WhatsApp/Telegram e DISPARA o agente.
                            (mesma ideia de um 'gatilho' no n8n/Make)
  • Agente de IA .......... módulo agente.py
  • Modelagem de dados .... módulo banco.py (SQLite relacional + JSON NoSQL)
"""
import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import banco
import agente

PASTA = os.path.dirname(os.path.abspath(__file__))
FRONT = os.path.join(PASTA, "frontend", "index.html")
PORTA = 8000


class Handler(BaseHTTPRequestHandler):
    # ---- utilitários ----
    def _json(self, dados, status=200):
        corpo = json.dumps(dados, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Content-Length", str(len(corpo)))
        self.end_headers()
        self.wfile.write(corpo)

    def _ler_corpo(self):
        tamanho = int(self.headers.get("Content-Length", 0))
        if tamanho == 0:
            return {}
        try:
            return json.loads(self.rfile.read(tamanho).decode("utf-8"))
        except Exception:
            return {}

    def log_message(self, *args):
        pass  # silencia o log padrão no terminal

    # ---- rotas GET (ler dados) ----
    def do_GET(self):
        if self.path == "/":
            self._servir_html()
        elif self.path == "/api/clientes":
            self._json(banco.listar_clientes())
        elif self.path == "/api/pedidos":
            self._json(banco.listar_pedidos())
        elif self.path == "/api/conversas":
            self._json(banco.listar_conversas())
        else:
            self._json({"erro": "rota não encontrada"}, 404)

    # ---- rotas POST (criar / acionar) ----
    def do_POST(self):
        corpo = self._ler_corpo()

        # WEBHOOK do WhatsApp/Telegram -> dispara o agente (a automação)
        if self.path == "/api/mensagem":
            mensagem = (corpo.get("mensagem") or "").strip()
            canal = corpo.get("canal", "whatsapp")
            if not mensagem:
                return self._json({"erro": "mensagem vazia"}, 400)
            return self._json(agente.responder(mensagem, canal))

        # criar cliente via API REST
        if self.path == "/api/clientes":
            nome = corpo.get("nome")
            telefone = corpo.get("telefone")
            if not nome:
                return self._json({"erro": "nome é obrigatório"}, 400)
            novo_id = banco.criar_cliente(nome, telefone)
            return self._json({"id": novo_id, "nome": nome, "telefone": telefone}, 201)

        self._json({"erro": "rota não encontrada"}, 404)

    # ---- frontend ----
    def _servir_html(self):
        with open(FRONT, "rb") as f:
            corpo = f.read()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(corpo)))
        self.end_headers()
        self.wfile.write(corpo)


if __name__ == "__main__":
    banco.inicializar()
    print(f"AutoFlow IA rodando em http://localhost:{PORTA}  (Ctrl+C para parar)")
    ThreadingHTTPServer(("0.0.0.0", PORTA), Handler).serve_forever()
