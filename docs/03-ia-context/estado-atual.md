# Estado Atual — AutoFlow IA

> Última atualização: 2026-06-22

## Fase atual

- [x] MVP completo e funcional — pronto para apresentação

## O que está pronto

- [x] Servidor HTTP (`app.py`) com GET/POST e status codes corretos
- [x] Webhook `POST /api/mensagem`
- [x] API REST: GET /api/clientes, /api/pedidos, /api/conversas, POST /api/clientes
- [x] Agente (`agente.py`): classificação por regex, 5 ferramentas, loop completo
- [x] Esqueleto `chamar_llm_real()` com comentários para plugar LLM
- [x] Banco SQLite (`banco.py`): clientes + pedidos com FK + JOIN
- [x] Banco JSON (`banco.py`): conversas como documentos
- [x] Seed automático na primeira execução
- [x] Frontend chat estilo WhatsApp com botões de exemplo rápido
- [x] Painel de dados que consome a API REST em tempo real
- [x] README.md mapeando cada requisito da vaga ao código
- [x] Documentação fase-0 a 04 criada

## O que NÃO está feito (opcional, pós-apresentação)

- [ ] LLM real plugado (esqueleto existe — basta configurar chave)
- [ ] Ferramenta de cancelamento de pedido
- [ ] Deploy no GitHub/Render para ter URL pública
- [ ] Testes automatizados

## Preparação para a entrevista

**Pontos-chave para explicar:**
1. Por que stdlib only (ADR-001)
2. Loop do agente: classificar → ferramenta → executar → registrar
3. Por que dois bancos (ADR-002): schema fixo vs. documento flexível
4. Como plugar LLM real sem reescrever o código (`chamar_llm_real`)
