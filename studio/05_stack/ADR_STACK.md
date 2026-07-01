# ADR-STACK — Decisão de Stack: AutoFlow IA

> Etapa: `05_STACK` | Status: APROVADO | Data: 2026-07-01

---

## Contexto

O projeto precisa demonstrar, num único codebase pequeno e legível, todos os padrões de um sistema de integração com IA: API REST, webhook, agente com function calling, banco relacional e banco de documentos. O código deve ser executável em qualquer máquina sem instalação de dependências, e ser lido em 10 minutos por um engenheiro que nunca viu o projeto.

---

## Decisão 1 — Python puro (stdlib only), sem framework

**Escolha:** `http.server.ThreadingHTTPServer` da stdlib Python

**Alternativas consideradas:**
- FastAPI — framework popular, mas introduz decorators e conceitos que obscurecem a mecânica do servidor
- Flask — mais simples, mas ainda é uma dependência externa que exige `pip install`
- Nenhum framework externo — exige `pip install` na máquina do entrevistador

**Razão:**
A demo é executada ao vivo na entrevista. Zero dependências elimina o risco de "não consigo instalar" e mantém o foco no código, não no setup. A stdlib Python é suficiente para demonstrar todos os padrões necessários.

**Consequência:**
O roteamento de endpoints é manual (`if path == "/api/clientes"`). Isso é intencional: torna explícito o que um framework normalmente abstrai, o que é didaticamente valioso.

---

## Decisão 2 — SQLite (stdlib) para banco relacional

**Escolha:** `sqlite3` da stdlib Python

**Alternativas consideradas:**
- PostgreSQL — produção real, mas exige servidor externo
- MySQL — mesma restrição
- SQLite via arquivo externo — identico, mas sqlite3 é stdlib

**Razão:**
SQLite é embutido no Python — sem servidor, sem configuração. Permite demonstrar SQL real (CREATE TABLE, FK, JOIN) com o mesmo código que rodaria em PostgreSQL, sem infra adicional.

**Consequência:**
`dados.db` é gerado automaticamente no primeiro run. Deve estar em `.gitignore` (já está).

---

## Decisão 3 — JSON para banco de documentos

**Escolha:** `json` da stdlib Python + arquivo `conversas.json`

**Alternativas consideradas:**
- MongoDB — paradigma NoSQL real, mas exige servidor externo
- TinyDB — biblioteca externa
- Redis — mais próximo de cache do que documento

**Razão:**
Demonstra o paradigma NoSQL (documento flexível, sem schema fixo) com a mesma restrição de zero dependências. O entrevistador vê, de forma explícita e lado a lado em `banco.py`, a diferença entre relacional (SQLite) e documento (JSON).

**Consequência:**
`conversas.json` é gerado automaticamente. Deve estar em `.gitignore` (já está). A "coleção" de conversas é um array JSON — leitura completa a cada query, aceitável para demo educacional.

---

## Decisão 4 — Agente rule-based, não LLM real

**Escolha:** dicionário `FERRAMENTAS` com regras de classificação por palavras-chave

**Alternativas consideradas:**
- Integrar OpenAI/Anthropic API diretamente
- Usar LangChain/LlamaIndex

**Razão:**
Um LLM real exigiria API key, custo por token e conexão de rede. A demo deve funcionar offline. O padrão de function calling (classificar → escolher ferramenta → executar → registrar) é idêntico ao que um LLM faria — a diferença é só o classificador. O esqueleto `chamar_llm_real()` deixa o caminho de extensão explícito.

**Consequência:**
O agente não tem raciocínio semântico — palavras não mapeadas vão para `fallback`. Documentado explicitamente no README.

---

## Resumo

| Decisão | Escolha | Trade-off aceito |
|---|---|---|
| Linguagem | Python 3 stdlib | Roteamento manual vs. simplicidade absoluta |
| Servidor | ThreadingHTTPServer | Sem features avançadas vs. zero deps |
| Banco relacional | SQLite | Single-file vs. escala |
| Banco documento | JSON | Performance vs. zero deps |
| Agente | Rule-based | Sem semântica vs. zero API key |

Todas as decisões sacrificam features de produção em favor de: zero dependências, execução instantânea, código didático.
