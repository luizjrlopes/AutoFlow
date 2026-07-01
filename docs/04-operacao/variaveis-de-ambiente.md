# Variáveis de Ambiente — AutoFlow IA

## Projeto atual (nenhuma variável obrigatória)

O AutoFlow IA roda sem nenhuma variável de ambiente — o design intencional é zero configuração para o caminho padrão (100% local). Uma variável opcional existe para habilitar uma integração externa:

| Configuração | Onde | Valor padrão |
|-------------|------|-------------|
| Porta do servidor | `app.py` — `PORTA = 8000` | 8000 |
| Arquivo do banco SQLite | `banco.py` — `DB` | `dados.db` (mesmo diretório) |
| Arquivo JSON | `banco.py` — `DOC` | `conversas.json` (mesmo diretório) |
| `N8N_WEBHOOK_URL` (opcional) | `app.py` — `N8N_WEBHOOK` via `os.environ.get(...)` | vazio → `POST /api/mensagem` usa sempre o agente local |

Se `N8N_WEBHOOK_URL` estiver definida, `POST /api/mensagem` encaminha a mensagem para essa URL antes de tentar o agente local; se a chamada falhar (timeout, erro, URL fora do ar), cai automaticamente no agente local (`origem: "local"` na resposta). Sem a variável definida, o comportamento é sempre local — nenhuma chamada de rede é feita.

## Se plugar LLM real

| Variável | Exemplo | Descrição |
|----------|---------|-----------|
| `OPENAI_API_KEY` | `sk-...` | Chave de API para LLM (não commitar) |
| `LLM_MODEL` | `gpt-4o-mini` | Modelo a usar (opcional) |

Carregar via `os.environ.get("OPENAI_API_KEY")` em `agente.py` — nunca hardcoded no código.
