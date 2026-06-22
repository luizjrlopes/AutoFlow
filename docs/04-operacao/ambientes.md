# Ambientes — AutoFlow IA

## Único ambiente: local

| Etapa | Comando | Resultado |
|-------|---------|-----------|
| Rodar | `python app.py` | Servidor em http://localhost:8000 |
| Parar | `Ctrl+C` no terminal | |
| Resetar dados | Apagar `dados.db` e `conversas.json` | Recriados com seed na próxima execução |

## Como rodar

```bash
# Na pasta do projeto
python app.py
# ou no Windows:
py app.py

# Abrir no navegador
http://localhost:8000
```

## Verificação rápida

```bash
# Testar webhook via curl
curl -X POST http://localhost:8000/api/mensagem \
  -H "Content-Type: application/json" \
  -d '{"mensagem": "listar produtos", "canal": "whatsapp"}'

# Listar clientes
curl http://localhost:8000/api/clientes
```
