# Estratégia de Git — AutoFlow IA

## Como versionar

```bash
git init
git add app.py agente.py banco.py frontend/ README.md CLAUDE.md docs/
# NÃO adicionar: dados.db, conversas.json, __pycache__/
git commit -m "feat: AutoFlow IA — agente, API REST e modelagem de dados"
git remote add origin https://github.com/SEU_USUARIO/autoflow-ia.git
git push -u origin main
```

## .gitignore recomendado

```
dados.db
conversas.json
__pycache__/
*.pyc
.env
```

## Commits

Conventional Commits em português:
```
feat: adiciona ferramenta de cancelamento de pedido
fix: corrige busca de cliente com acentos
docs: atualiza README com instruções de entrevista
```
