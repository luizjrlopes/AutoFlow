# RELATÓRIO DE SEGURANÇA — AutoFlow IA

> Etapa: `11_SEGURANCA` | Status: APROVADO | Data: 2026-07-01

---

## Checklist de segurança

### Secrets e dados sensíveis no código

| Item | Verificação | Status |
|---|---|---|
| API keys ou tokens no código | `grep -r "sk-\|Bearer\|api_key" *.py` → vazio | ✅ Nenhum |
| URLs externas hardcoded no código | Nenhuma — `app.py` lê `N8N_WEBHOOK_URL` via `os.environ.get(...)`, valor padrão vazio | ✅ Nenhuma |
| Integração opcional com n8n | `POST /api/mensagem` só encaminha externamente se `N8N_WEBHOOK_URL` estiver definida; sem a variável, é sempre o agente local. Em caso de falha de rede, cai automaticamente para o agente local (fallback) | ✅ Opt-in, com fallback |
| Senha hardcoded | Sem autenticação no MVP — nenhuma senha | ✅ N/A |
| `chamar_llm_real()` | Função é esqueleto comentado — sem key real | ✅ Seguro |

> Nota de correção (2026-07-01): uma versão anterior deste relatório afirmava "nenhuma URL de produção no código", mas havia uma URL real do n8n hardcoded em `app.py`. Isso foi corrigido movendo a URL para a variável de ambiente opcional `N8N_WEBHOOK_URL` antes da publicação.

### Arquivos gerados em runtime

| Arquivo | .gitignore | Risco |
|---|---|---|
| `dados.db` | ✅ coberto | Contém dados de seed fictícios — baixo risco |
| `conversas.json` | ✅ coberto | Contém conversas de teste — baixo risco |
| `__pycache__/` | ✅ coberto | Bytecode Python — sem dado sensível |

### Estrutura do .gitignore

```
dados.db          # banco SQLite gerado em runtime
conversas.json    # histórico de conversas gerado em runtime
__pycache__/      # cache Python
*.pyc
.env              # não existe, mas coberto preventivamente
```

Resultado: todos os arquivos gerados em runtime estão bloqueados.

### Verificação de histórico git

| Item | Status |
|---|---|
| `git ls-files \| grep "dados.db"` → vazio | ✅ |
| `git ls-files \| grep "conversas.json"` → vazio | ✅ |
| Nenhum commit com secret no histórico | ✅ |

---

## Exposição de dados no README

| Item | Avaliação |
|---|---|
| Credenciais de acesso | Não aplicável — sem autenticação |
| URLs de produção | `http://localhost:8000` por padrão. `N8N_WEBHOOK_URL` é opcional, não vem definida por padrão e não aparece hardcoded no código |
| Dados de usuário real | Seed são dados fictícios (cliente1, cliente2...) |
| Promessa de integração real que não existe | README declara explicitamente que o padrão é local; a integração com n8n é opcional e documentada em `docs/04-operacao/variaveis-de-ambiente.md` |

---

## Avaliação de risco de publicação

| Dimensão | Risco | Justificativa |
|---|---|---|
| Vazamento de credencial | Nenhum | Sem API key, sem senha real |
| Exposição de dado pessoal | Nenhum | Apenas dados de seed fictícios |
| Código malicioso ou inseguro | Nenhum | Stdlib Python — sem deps externas de pacote |
| Comprometimento de infraestrutura | Nenhum | Deploy local apenas; integração com n8n é opt-in via env var, nunca commitada no código |

---

## Conclusão

**Aprovado para publicação no GitHub público.**

Nenhum bloqueio identificado, após a correção do item de URL hardcoded (ver nota acima). `legado/` e `prototipo/` ficam fora do repositório público via `.gitignore`; `studio/` é publicado como registro do processo de construção do projeto.
