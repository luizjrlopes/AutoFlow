# Glossário — AutoFlow IA

## Termos do domínio

| Termo | Definição |
|-------|-----------|
| Webhook | URL que recebe um evento externo e dispara um fluxo. Aqui: `POST /api/mensagem` |
| Agente de IA | Sistema que classifica uma intenção e escolhe/executa uma ferramenta para responder |
| Ferramenta (tool) | Função que o agente pode chamar — aqui: consultar_cliente, criar_pedido, etc. |
| Function calling | Padrão em que o "cérebro" (LLM ou regras) escolhe qual ferramenta chamar e com quais argumentos |
| Intenção | O que o usuário quer fazer — classificada pelo agente antes de escolher a ferramenta |
| Canal | Origem da mensagem — `whatsapp` ou `telegram` no campo da request |

## Termos técnicos

| Termo | Significado no código |
|-------|----------------------|
| `FERRAMENTAS` | Dicionário em `agente.py` que mapeia nome → função de ferramenta |
| `classificar()` | Função que analisa o texto e retorna `(nome_ferramenta, args)` |
| `responder()` | Loop principal do agente: classifica → executa → registra → retorna |
| `inicializar()` | Função em `banco.py` que cria tabelas e seed na primeira execução |
| `PK` | Chave primária — identifica unicamente uma linha (`id` nas tabelas) |
| `FK` | Chave estrangeira — liga `pedidos.cliente_id` → `clientes.id` |

## Requisitos da vaga × conceitos

| Requisito OTG | Conceito | Onde ver |
|---------------|---------|---------|
| Consumo/criação de APIs | REST com status codes | `app.py` |
| Automação (gatilho → ação) | Webhook → agente | `POST /api/mensagem` |
| Agente de IA | Loop de intenção + ferramenta | `agente.py` |
| Relacional | SQLite com FK | `banco.py` — `clientes` e `pedidos` |
| Não relacional | JSON como documento | `banco.py` — `conversas.json` |
| WhatsApp/Telegram | Campo `canal` no request | `agente.py` + `frontend` |
