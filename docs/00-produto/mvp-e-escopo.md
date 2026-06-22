# MVP e Escopo — AutoFlow IA

## O que está implementado (MVP completo)

| Feature | Arquivo | Status |
|---------|---------|--------|
| Servidor HTTP com GET/POST | `app.py` | ✅ |
| Webhook `POST /api/mensagem` | `app.py` | ✅ |
| API REST: clientes, pedidos, conversas | `app.py` | ✅ |
| Agente: classificação de intenção | `agente.py` | ✅ |
| 5 ferramentas (consulta, criação, status, produtos, fallback) | `agente.py` | ✅ |
| Esqueleto para LLM real (`chamar_llm_real`) | `agente.py` | ✅ |
| Banco relacional SQLite (clientes + pedidos com FK) | `banco.py` | ✅ |
| Banco não relacional JSON (conversas como documentos) | `banco.py` | ✅ |
| Frontend chat estilo WhatsApp | `frontend/index.html` | ✅ |
| Painel de dados que consome a API | `frontend/index.html` | ✅ |
| Seed automático na primeira execução | `banco.py` | ✅ |

## O que está FORA do MVP

- [ ] LLM real plugado (esqueleto existe em `agente.py` — basta configurar chave)
- [ ] Autenticação
- [ ] Deploy em cloud
- [ ] Multi-canal real (hoje é simulado via campo `canal`)
- [ ] Persistência de conversas além do JSON local

## Critério de sucesso do MVP

- [x] Roda com `python app.py` sem instalar nada além do Python 3
- [x] Cobre todos os requisitos da vaga listados no README
- [x] Código comentado em português para leitura durante a entrevista
