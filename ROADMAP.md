# Roadmap — AutoFlow IA

Estado atual e próximos passos do projeto.

---

## Estado atual — v1.0.0 ✅

MVP completo. Todos os padrões de integração com IA demonstráveis:

- [x] API REST (GET + POST, status codes corretos)
- [x] Webhook de automação (`POST /api/mensagem` → agente)
- [x] Agente com function calling (classificar → ferramenta → executar → registrar)
- [x] Banco relacional (SQLite — FK, JOIN)
- [x] Banco de documentos (JSON — paradigma NoSQL)
- [x] Frontend chat consumindo a própria API

---

## Próximos passos

### Qualidade (prioridade média)

- [x] Testes automatizados com `unittest` (stdlib)
  - `test_agente.py`, `test_banco.py`, `test_app.py` — classificação de intenção, operações de banco, smoke test da API
- [ ] Validação de input mais robusta (tamanho de campo, caracteres inválidos)

### Integração (prioridade baixa)

- [ ] Plugar LLM real via `chamar_llm_real()` em `agente.py`
  - Implementação com `urllib.request` — mantém zero deps externas
  - Candidatos: Anthropic Claude (function calling nativo), OpenAI
- [ ] Webhook externo real (WhatsApp via Meta API ou Telegram Bot API)
  - Pré-requisito: deploy em servidor com HTTPS

### Infraestrutura (prioridade baixa)

- [ ] Deploy em servidor mínimo (Railway, Render, ou VPS simples)
  - Bloqueia: webhook externo real
  - Decisão pendente: vale o custo para demo educacional?

---

## Fora do escopo

- Autenticação/autorização — projeto educacional, sem usuários externos
- Múltiplos usuários simultâneos — escopo de demo, não produção
- Banco de dados externo (PostgreSQL, MongoDB) — stdlib é suficiente para o objetivo
- Interface administrativa — fora do escopo do MVP
