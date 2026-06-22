# Próximo Passo — AutoFlow IA

## Situação atual

MVP completo e pronto para apresentação. Nenhuma tarefa crítica pendente.

## Se quiser plugar um LLM real (pós-entrevista)

1. Obter chave de API (OpenAI, Anthropic, etc.)
2. Em `agente.py`, implementar `chamar_llm_real(mensagem)`:
   - Usar `urllib.request` (stdlib) para chamar a API
   - Descrever as FERRAMENTAS no formato de tools da API
   - Substituir o corpo de `classificar()` pela chamada ao LLM
3. Testar com `python app.py`

**Prompt sugerido:**
```
No AutoFlow IA (agente.py), implemente chamar_llm_real() usando urllib.request.
Leia docs/02-arquitetura/visao-tecnica.md (seção "Como plugar LLM real").
Use o dicionário FERRAMENTAS existente para descrever as tools no formato da API.
Pronto quando: mensagem "status do pedido 1" é respondida pelo LLM usando a ferramenta correta.
```

## Se quiser publicar como portfólio

```bash
git init
echo "dados.db
conversas.json
__pycache__/
*.pyc" > .gitignore
git add .
git commit -m "feat: AutoFlow IA — agente, API REST e modelagem de dados"
# criar repo no GitHub e push
```

## Prompt de início sugerido

```
Estou retomando o AutoFlow IA.
Leia CLAUDE.md e docs/03-ia-context/estado-atual.md.
A tarefa de hoje é: [descreva aqui]
```
