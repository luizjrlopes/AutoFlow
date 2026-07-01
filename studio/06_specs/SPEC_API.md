# SPEC — API REST (AutoFlow IA)

> Etapa: `06_SPECS` | Status: IMPLEMENTADO | Data: 2026-07-01

---

## Responsabilidade

Servidor HTTP que expõe os recursos do sistema via API REST. Serve também o frontend estático e é o ponto de entrada do webhook de automação.

**Arquivo:** `app.py`

---

## Endpoints

### GET /
Serve `frontend/index.html`.
- Response: `200 OK` — HTML

### GET /api/clientes
Lista todos os clientes cadastrados.
- Response: `200 OK` — `[{id, nome, email, telefone}]`

### POST /api/clientes
Cria novo cliente.
- Body: `{"nome": str, "email": str, "telefone": str}`
- Response: `201 Created` — `{"id": int, "nome": str}`
- Erro: `400 Bad Request` se campos obrigatórios ausentes

### GET /api/pedidos
Lista todos os pedidos com dados do cliente (JOIN).
- Response: `200 OK` — `[{id, produto, valor, status, cliente_nome}]`

### GET /api/conversas
Lista histórico de conversas do agente.
- Response: `200 OK` — `[{timestamp, mensagem, resposta}]`

### POST /api/mensagem ⭐ (Webhook principal)
Recebe mensagem e aciona o agente automaticamente.
- Body: `{"mensagem": str}`
- Response: `200 OK` — `{"resposta": str}`
- Erro: `400 Bad Request` se campo `mensagem` ausente

---

## Padrões adotados

- Status codes corretos: `200` GET/ação sem criação, `201` POST com criação, `400` dados inválidos, `404` recurso não encontrado
- Content-Type: `application/json` em todas as respostas da API
- CORS: não configurado — apenas uso local
- Autenticação: não aplicável neste MVP

---

## Critérios de aceite (retroativos)

- [x] Todos os endpoints respondem com o status code correto
- [x] `POST /api/mensagem` chama `agente.py` automaticamente (webhook)
- [x] Body inválido retorna `400`, não `500`
- [x] GET `/api/pedidos` retorna JOIN com nome do cliente
- [x] Servidor aceita múltiplas conexões simultâneas (`ThreadingHTTPServer`)
