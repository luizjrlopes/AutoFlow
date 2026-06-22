# Restrições Técnicas — AutoFlow IA

## Stack (não mudar sem decisão documentada)

| Camada | Tecnologia | Restrição |
|--------|-----------|-----------|
| Linguagem | Python 3.x | Somente stdlib — sem pip install |
| Banco relacional | SQLite (módulo `sqlite3`) | Embutido no Python |
| Banco não relacional | JSON (módulo `json`) | Arquivo local `conversas.json` |
| Servidor HTTP | `http.server.ThreadingHTTPServer` | Embutido no Python |
| Frontend | HTML/CSS/JS puro | Sem framework externo |

## Por que sem dependências externas

Decisão fundamental do projeto: o candidato deve poder rodar `python app.py` em qualquer máquina com Python 3 instalado, sem `pip install`, sem venv, sem Docker. Isso garante que a demo funciona no computador do entrevistador sem fricção.

## Restrições de extensão

**Para plugar um LLM real** (evolutivo, não proibido):
- Usar `urllib.request` (stdlib) para chamar OpenAI/Anthropic — sem `requests`
- Ou configurar a chave e usar SDK externo apenas num branch separado
- A estrutura FERRAMENTAS + loop não muda — só a função `classificar()` é substituída por `chamar_llm_real()`

## O que o AI NÃO deve fazer sem perguntar

- [ ] Adicionar imports de bibliotecas externas (`requests`, `flask`, `fastapi`, etc.)
- [ ] Separar o servidor em múltiplos arquivos — a simplicidade é intencional
- [ ] Remover os comentários educacionais — são parte do propósito do projeto
