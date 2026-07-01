# CONTEXT PACK — AutoFlow IA

> Etapa: `02_CONTEXTO` | Status: APROVADO | Data: 2026-07-01

---

## Produto

**AutoFlow IA** — Mini-aplicação Python que demonstra, num único projeto, os padrões centrais de sistemas de integração com IA: API REST, automação via webhook, agente com function calling, modelagem relacional + não relacional, e integração com canais de mensagem.

**Origem:** Construído para demonstrar os 5 requisitos da vaga de Especialista em Automação e Integração com IA (OTG) em entrevista técnica de 01/07/2026.

**Público:** Uso pessoal do candidato — portfólio e apresentação em entrevista.

---

## Fonte principal

Código ativo em `app.py`, `agente.py`, `banco.py`, `frontend/index.html`.

Fontes secundárias (consulta pontual):
- `docs/` — produto, regras, arquitetura, contexto IA
- `CLAUDE.md` — contexto para sessões de IA
- `ESTRATEGIA-GIT.md` — convenção de commits e git

Legado: `legado/` — histórico de versões anteriores. Não é fonte primária.

---

## Stack

| Camada | Tecnologia | Justificativa |
|---|---|---|
| Linguagem | Python 3.x (stdlib only) | Zero dependências — qualquer máquina com Python 3 roda sem instalação |
| Servidor HTTP | `http.server.ThreadingHTTPServer` | Suficiente para demonstração local; evita framework que esconde a lógica |
| Banco relacional | SQLite (`sqlite3`) | Embutido no Python; demonstra SQL, FK, JOIN sem banco externo |
| Banco documento | JSON (`json`) | Arquivo simples; demonstra paradigma NoSQL sem MongoDB |
| Frontend | HTML/CSS/JS puro | Sem build step; abre no navegador diretamente |

Ver decisão formal: `studio/05_stack/ADR_STACK.md`

---

## Arquitetura

```
[frontend/index.html]
        |
        | POST /api/mensagem  (webhook de automação)
        ↓
[app.py — ThreadingHTTPServer]
  GET  /api/clientes    → banco.py → SQLite
  GET  /api/pedidos     → banco.py → SQLite (JOIN)
  GET  /api/conversas   → banco.py → JSON
  POST /api/mensagem    → agente.py
  POST /api/clientes    → banco.py → SQLite
        |
        ↓
[agente.py]
  classificar(mensagem) → intenção
  FERRAMENTAS[intenção](args) → execução
  registrar_conversa() → banco.py → JSON
        |
        ↓
[banco.py]
  SQLite: tabelas clientes, pedidos (FK, JOIN)
  JSON:   conversas.json (documento flexível)
```

---

## Mapeamento de requisitos da vaga → código

| Requisito OTG | Implementação |
|---|---|
| Consumo/criação de APIs REST | `app.py` — 6 endpoints GET/POST com status codes corretos |
| Automação (gatilho → ação) | `POST /api/mensagem` → aciona agente automaticamente |
| Agente de IA com function calling | `agente.py` — `FERRAMENTAS` dict + loop classificar→executar |
| Modelagem relacional | `banco.py` — SQLite com FK e JOIN |
| Modelagem não relacional | `banco.py` — JSON como documento NoSQL |

---

## Estado do MVP

- **Implementação:** Completa — todos os módulos funcionais
- **Agente:** Rule-based (não usa LLM real). `chamar_llm_real()` em `agente.py` é esqueleto documentado
- **Frontend:** Interface chat estilo WhatsApp consumindo a própria API
- **Banco:** SQLite criado e populado automaticamente no primeiro `python app.py`
- **Deploy:** Apenas local — `python app.py` → `http://localhost:8000`
- **GitHub:** `https://github.com/luizjrlopes/AutoFlow`

---

## Lacunas registradas

| Lacuna | Impacto | Decisão |
|---|---|---|
| `chamar_llm_real()` não implementado | Demo usa regras, não LLM | Intencional — extensão documentada, não requisito |
| Webhook externo (WhatsApp/Telegram real) | Não conectado | Intencional — demo local, não produção |
| `prototipo/` na raiz | Versão anterior | Histórico — não publicar junto |
| Sem testes automatizados | Risco de regressão | Roadmap — fora do escopo do MVP |

---

## Anti-contexto

- O legado em `legado/` não representa o estado atual
- `dados.db` e `conversas.json` são gerados em runtime — nunca commitar
- O projeto não tem autenticação — não é requisito da demo
