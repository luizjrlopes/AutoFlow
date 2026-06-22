# Checklist de Construção — AutoFlow IA

**Stack:** Python 3.x stdlib + SQLite + JSON  
**Status:** ✅ MVP completo  
**Última atualização:** 2026-06-22

---

## BLOCO 0 — Setup

- [x] **0.1** Estrutura de pastas: `app.py`, `agente.py`, `banco.py`, `frontend/`
- [x] **0.2** Sem dependências externas — stdlib only
- [x] **0.3** `.gitignore` com `dados.db`, `conversas.json`, `__pycache__/`

## BLOCO 1 — Servidor HTTP e API REST (`app.py`)

- [x] **1.1** `ThreadingHTTPServer` na porta 8000
- [x] **1.2** GET `/` — serve `frontend/index.html`
- [x] **1.3** GET `/api/clientes` — lista clientes (SQLite)
- [x] **1.4** GET `/api/pedidos` — lista pedidos com JOIN (SQLite)
- [x] **1.5** GET `/api/conversas` — lista conversas (JSON)
- [x] **1.6** POST `/api/mensagem` — webhook → agente
- [x] **1.7** POST `/api/clientes` — criar cliente
- [x] **1.8** Status codes corretos: 200, 201, 400, 404
- [x] **1.9** CORS header (`Access-Control-Allow-Origin: *`)

## BLOCO 2 — Agente de IA (`agente.py`)

- [x] **2.1** Dicionário `FERRAMENTAS` com 5 ferramentas
- [x] **2.2** `tool_consultar_cliente`: busca por nome/telefone
- [x] **2.3** `tool_criar_pedido`: verifica cliente, cria pedido com FK
- [x] **2.4** `tool_status_pedido`: busca status via JOIN
- [x] **2.5** `tool_listar_produtos`: retorna lista de produtos
- [x] **2.6** `tool_fallback`: orienta o usuário
- [x] **2.7** `classificar(mensagem)`: regex + keywords → (ferramenta, args)
- [x] **2.8** `responder(mensagem, canal)`: loop completo + registro
- [x] **2.9** `chamar_llm_real()`: esqueleto documentado para extensão futura

## BLOCO 3 — Banco de Dados (`banco.py`)

- [x] **3.1** `inicializar()`: cria tabelas + seed na primeira execução
- [x] **3.2** Tabela `clientes` com PK, nome NOT NULL, telefone UNIQUE
- [x] **3.3** Tabela `pedidos` com PK, FK → clientes, status default 'recebido'
- [x] **3.4** CRUD relacional: listar, buscar, criar clientes e pedidos
- [x] **3.5** JOIN em `listar_pedidos()` e `buscar_pedido()`
- [x] **3.6** `registrar_conversa()`: append ao JSON como documento
- [x] **3.7** `listar_conversas()`: lê arquivo JSON

## BLOCO 4 — Frontend (`frontend/index.html`)

- [x] **4.1** Chat estilo WhatsApp com campo `canal`
- [x] **4.2** Botões de exemplos rápidos
- [x] **4.3** Etiqueta roxa mostrando ferramenta usada
- [x] **4.4** Painel de pedidos (consome GET /api/pedidos)
- [x] **4.5** Painel de conversas (consome GET /api/conversas)
- [x] **4.6** Sem dependências externas de JS

---

## Progresso

**Total:** 27 itens | **Concluídos:** 27

```
Progresso: [██████████] 100%
```
