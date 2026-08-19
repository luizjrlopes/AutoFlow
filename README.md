# AutoFlow IA — Automation and Agent Integration Hub

[English](README.md) | [Português](README.pt-BR.md)

Pure-Python automation hub that demonstrates core AI-integration patterns: a **REST API**, **webhook-driven automation**, an **agent with function calling**, and **relational + document data modeling** — all with zero external runtime dependencies.

## Why this project exists

Modern AI automations combine three layers that are rarely shown together in a small educational project:

1. **Transport** — receive external events through a REST API;
2. **Decision** — classify intent and choose the appropriate tool;
3. **Data** — use relational persistence for structured entities and document storage for flexible interaction logs.

The project implements these three layers in a compact, commented codebase without external frameworks. Anyone with Python 3 installed can run it locally.

## Features

- **Complete REST API** with `GET` and `POST`, status codes and JSON responses;
- **Automation webhook** at `POST /api/mensagem`;
- **AI-agent loop** for intent classification, tool selection, execution and response logging;
- **Function-calling pattern** through the `FERRAMENTAS` catalog with five actions;
- **Relational SQLite database** for `clientes` and `pedidos`, including keys and `JOIN` queries;
- **JSON document store** for flexible interaction records;
- **Chat frontend** that consumes the same API and displays data in real time.

## Run locally

```bash
python app.py
```

Open `http://localhost:8000` in a browser. On the first run the application creates the local database and seeds sample data automatically. Stop it with `Ctrl+C`.

> Only Python 3 is required. No `pip install` is needed. By default, no external network request is made: `POST /api/mensagem` uses the local agent. An optional n8n integration can be enabled through `N8N_WEBHOOK_URL`; see `docs/04-operacao/variaveis-de-ambiente.md`.

## Code map

| File | Responsibility |
|---|---|
| `app.py` | HTTP server, REST routes and webhook |
| `agente.py` | Intent classification, tool catalog and agent loop |
| `banco.py` | Relational SQLite + JSON document persistence |
| `frontend/index.html` | Chat and data panel consuming the API |

**Suggested reading order:** `banco.py` → `agente.py` → `app.py` → `frontend/index.html`

## Endpoints

| Method | Route | Description |
|---|---|---|
| `GET` | `/` | Serves the frontend |
| `GET` | `/api/clientes` | Lists customers |
| `GET` | `/api/pedidos` | Lists orders using a JOIN |
| `GET` | `/api/conversas` | Lists conversations |
| `POST` | `/api/mensagem` | Receives a message and triggers the agent |
| `POST` | `/api/clientes` | Creates a customer |

## Agent tools

| Tool | Trigger |
|---|---|
| `consultar_cliente` | customer or phone queries |
| `criar_pedido` | order creation |
| `status_pedido` | order-status lookup |
| `listar_produtos` | products, plans and prices |
| `fallback` | any other message |

## Connecting a real LLM

The current agent uses rules so the project can run without cost. To connect a real model:

1. implement `chamar_llm_real()` in `agente.py`;
2. replace the body of `classificar()` with the LLM call;
3. keep the existing tool, loop and persistence boundaries.

## Current limits and production evolution

| Current limit | Production direction |
|---|---|
| No authentication/authorization | Add login and access control |
| Single-file SQLite | Move to Postgres/MySQL with connection pooling |
| Rule-based agent | Connect an LLM while preserving the tool boundary |
| `http.server` without HTTPS | Run behind a TLS proxy or managed PaaS |
| No robust rate limiting | Add stricter validation and throttling |
| No load testing | Run load tests before public exposure |

## Repository structure

```text
autoflow-ia/
├── app.py
├── agente.py
├── banco.py
├── frontend/
│   └── index.html
├── docs/
├── studio/
└── README.md
```

`dados.db` and `conversas.json` are generated automatically and ignored by `.gitignore`.

The `studio/` directory records the process used to plan and review the project; it is not part of the application runtime.
