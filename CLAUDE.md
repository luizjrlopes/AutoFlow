# CLAUDE.md — Contexto para o AI

> Este arquivo é lido automaticamente pelo Claude em cada sessão. Mantenha-o sempre atualizado.

## O que é este projeto

**Produto:** AutoFlow IA — Mini-aplicação Python que demonstra, num único projeto, todos os requisitos da vaga de Especialista em Automação e Integração com IA (OTG): API REST, automação via webhook, agente de IA com function calling, modelagem relacional + não relacional, e integração com canais de mensagem (WhatsApp/Telegram).  
**Público:** Uso pessoal do candidato — apresentação em entrevista e portfólio  
**Stack:** Python 3.x (stdlib apenas) + SQLite + JSON

## Estado atual

**Fase:** MVP completo — pronto para apresentação  
**Último trabalho:** Implementação completa: servidor HTTP (ThreadingHTTPServer), API REST com GET/POST, agente com ferramentas (FERRAMENTAS dict), banco relacional (SQLite) + não relacional (JSON), frontend chat estilo WhatsApp  
**Próximo passo:** Opcional — plugar LLM real via `chamar_llm_real()` em `agente.py`

## Regras que o AI não pode violar

- [ ] Sem dependências externas — somente biblioteca padrão Python
- [ ] A estrutura do agente (classificar → escolher ferramenta → executar → registrar) deve ser mantida — é o ponto central da apresentação
- [ ] O dicionário `FERRAMENTAS` em `agente.py` é o catálogo de tools — não mover lógica para fora dele
- [ ] `banco.py` deve manter os dois paradigmas: SQLite (relacional) e JSON (documento) — é um requisito da vaga
- [ ] `conversas.json` e `dados.db` são criados automaticamente — não commitar no git
- [ ] O endpoint `POST /api/mensagem` é o "webhook" central — não renomear

## Arquitetura em uma linha

```
[frontend/index.html (chat)] → [POST /api/mensagem (webhook)] → [agente.py] → [banco.py (SQLite + JSON)]
```

## Padrões de código

- Linguagem: Python 3 (stdlib only)
- Idioma dos comentários: Português (código é educacional)
- Todo módulo tem docstring explicando o "por quê" educacional
- Funções simples e curtas — o código deve ser lido em 10 minutos

## Onde estão as coisas

| O que | Onde |
|-------|------|
| Servidor HTTP + rotas REST | `app.py` |
| Agente (intenção + ferramentas) | `agente.py` |
| Banco de dados (SQLite + JSON) | `banco.py` |
| Frontend chat | `frontend/index.html` |
| Dados gerados automaticamente | `dados.db`, `conversas.json` |

## Contexto de negócio

Projeto criado especificamente para a vaga de Especialista em Automação e Integração com IA na OTG. Cada linha de código mapeia diretamente a um requisito da vaga: consumo/criação de APIs REST, automação (gatilho → ação), agente de IA com function calling, modelagem relacional e não relacional, e canais de mensagem (WhatsApp/Telegram simulados).
