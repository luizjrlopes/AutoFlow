# Histórico de Decisões — AutoFlow IA

### 2026-06-22 — Fase 0 — Somente biblioteca padrão Python
**Contexto:** Demo precisa rodar sem instalação no computador do entrevistador  
**Decisão:** `http.server`, `sqlite3`, `json` — zero dependências externas  
**Por quê:** Elimina 100% da fricção de demo; demonstra conhecimento da stdlib  
**Onde também registrar:** ADR-001

---

### 2026-06-22 — Fase 0 — SQLite + JSON como dois paradigmas de banco
**Contexto:** Vaga exige modelagem relacional E não relacional  
**Decisão:** SQLite para clientes/pedidos (schema fixo, FK), JSON para conversas (documento flexível)  
**Por quê:** Cada paradigma é adequado ao tipo de dado — não é divisão arbitrária  
**Onde também registrar:** ADR-002

---

### 2026-06-22 — Fase 0 — Dicionário FERRAMENTAS como catálogo de tools
**Contexto:** Precisava de um padrão análogo ao function calling de LLMs reais  
**Decisão:** `FERRAMENTAS = { "nome": função }` — o agente indexa por nome, igual ao function calling  
**Por quê:** Demonstra o padrão real; quando LLM for plugado, só muda quem escolhe o nome — o resto é igual

---

### 2026-06-22 — Fase 0 — Comentários em português no código
**Contexto:** Código educacional que será lido ao vivo na entrevista  
**Decisão:** Docstrings e comentários em português  
**Por quê:** Entrevistador lê mais rápido e sem atrito — o foco é no conceito, não na tradução
