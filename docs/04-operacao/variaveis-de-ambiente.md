# Variáveis de Ambiente — AutoFlow IA

## Projeto atual (sem variáveis obrigatórias)

O AutoFlow IA não usa variáveis de ambiente — o design intencional é zero configuração. Tudo é definido no próprio código:

| Configuração | Onde | Valor padrão |
|-------------|------|-------------|
| Porta do servidor | `app.py` — `PORTA = 8000` | 8000 |
| Arquivo do banco SQLite | `banco.py` — `DB` | `dados.db` (mesmo diretório) |
| Arquivo JSON | `banco.py` — `DOC` | `conversas.json` (mesmo diretório) |

## Se plugar LLM real

| Variável | Exemplo | Descrição |
|----------|---------|-----------|
| `OPENAI_API_KEY` | `sk-...` | Chave de API para LLM (não commitar) |
| `LLM_MODEL` | `gpt-4o-mini` | Modelo a usar (opcional) |

Carregar via `os.environ.get("OPENAI_API_KEY")` em `agente.py` — nunca hardcoded no código.
