# Deploy — AutoFlow IA

> Projeto de demo local. Deploy é opcional (portfólio).

## Opção 1: Render (mais simples)

1. Criar `requirements.txt` vazio (sem dependências)
2. Criar repo no GitHub e fazer push
3. Conectar repo no Render (Free tier)
4. Start Command: `python app.py`
5. Porta: `8000`

**Atenção:** Em produção, `dados.db` e `conversas.json` são recriados a cada deploy (ephemeral storage no Render free tier). Para persistência, migrar para SQLite em volume persistente ou PostgreSQL.

## Opção 2: Railway

Similar ao Render, com volume persistente disponível mesmo no free tier.

## Checklist pré-deploy

- [ ] Garantir que `.gitignore` exclui `dados.db`, `conversas.json` e `__pycache__/`
- [ ] Testar que `python app.py` funciona na porta `8000`
- [ ] Verificar que o seed cria dados de exemplo na primeira execução
