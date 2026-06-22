# Sessão de Discovery — AutoFlow IA

**Data:** 2026-06-22 (reconstituída a partir do código)  
**Contexto:** Projeto criado para demonstrar requisitos da vaga OTG — Especialista em Automação e Integração com IA

---

## O que o produto faz

Mini-aplicação Python que simula uma central de automação com IA. Recebe mensagens via webhook (simulando WhatsApp/Telegram), processa com um agente que classifica a intenção e escolhe a ferramenta adequada, executa ações no banco de dados (SQLite relacional + JSON não relacional) e retorna respostas estruturadas.

## Para quem é

O candidato (Luiz Júnior) — para apresentação na entrevista da vaga OTG de Especialista em Automação e Integração com IA.

## Problema principal resolvido

Demonstrar, num único projeto executável sem instalação de dependências externas, todos os requisitos técnicos listados na vaga: API REST, automação por webhook, agente de IA com function calling pattern, modelagem relacional + não relacional, e integração com canais de mensagem.

## Stack decidida

- Python stdlib apenas (sem pip install) — roda em qualquer máquina com Python 3
- SQLite (embutido no Python) para dados relacionais
- JSON para dados não relacionais (documentos)
- ThreadingHTTPServer para o servidor HTTP
- HTML/CSS/JS puro para o frontend

## Componentes identificados

1. **app.py** — servidor HTTP com rotas REST (GET + POST), webhook central
2. **agente.py** — agente com catálogo de ferramentas, classificação de intenção, loop de execução
3. **banco.py** — camada de dados: SQLite (clientes + pedidos) + JSON (conversas)
4. **frontend/index.html** — chat estilo WhatsApp que consome a API

## Requisitos da vaga mapeados no código

| Requisito | Implementado em |
|-----------|----------------|
| Consumo/criação de APIs REST | `app.py` — GET/POST com JSON e status codes |
| Automação (gatilho → ação) | `POST /api/mensagem` — webhook que dispara o agente |
| Agente de IA com function calling | `agente.py` — FERRAMENTAS + loop classificar→executar |
| Modelagem relacional | `banco.py` — SQLite com clientes, pedidos, FK |
| Modelagem não relacional | `banco.py` — conversas.json como documentos |
| WhatsApp/Telegram | `frontend/index.html` — chat com campo `canal` |
| Homologação/implantação | `python app.py` — sem instalação, zero config |
