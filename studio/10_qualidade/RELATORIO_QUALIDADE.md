# RELATÓRIO DE QUALIDADE — AutoFlow IA

> Etapa: `10_QUALIDADE` | Status: APROVADO | Data: 2026-07-01

---

## Escopo da validação

Validação manual do MVP, complementada por testes automatizados (`test_agente.py`, `test_banco.py`, `test_app.py`) adicionados após esta rodada de validação.

---

## Validação funcional

### Servidor e API

| Cenário | Resultado |
|---|---|
| `python app.py` inicia sem erro | ✅ |
| `http://localhost:8000` abre o frontend | ✅ |
| `GET /api/clientes` retorna lista JSON | ✅ |
| `GET /api/pedidos` retorna JOIN com nome do cliente | ✅ |
| `GET /api/conversas` retorna histórico vazio no início | ✅ |
| `POST /api/clientes` body válido → 201 | ✅ |
| `POST /api/clientes` body inválido → 400 | ✅ |
| `POST /api/mensagem` aciona o agente | ✅ |

### Agente

| Cenário | Resultado |
|---|---|
| "quero ver os clientes" → `consultar_cliente` | ✅ |
| "quero criar um pedido" → `criar_pedido` | ✅ |
| "qual o status do pedido 1" → `status_pedido` | ✅ |
| "quais produtos têm?" → `listar_produtos` | ✅ |
| mensagem fora do mapa → `fallback` sem erro | ✅ |
| conversa registrada em `conversas.json` após resposta | ✅ |

### Banco de dados

| Cenário | Resultado |
|---|---|
| `dados.db` criado automaticamente no primeiro run | ✅ |
| Seed (3 clientes, 4 pedidos) populado automaticamente | ✅ |
| `conversas.json` criado automaticamente | ✅ |
| Segundo run não duplica seed | ✅ |

---

## Validação de código

| Critério | Status |
|---|---|
| Nenhuma dependência externa no código | ✅ |
| Todos os módulos têm docstring explicando o "por quê" | ✅ |
| Funções ≤ 20 linhas (legibilidade) | ✅ |
| Idioma dos comentários: Português | ✅ |
| `FERRAMENTAS` é o único ponto de adição de ações | ✅ |
| `banco.py` mantém os dois paradigmas no mesmo módulo | ✅ |

---

## Cobertura de testes automatizados

**Situação atual:** `test_agente.py` (classificação de intenção + loop do agente), `test_banco.py` (CRUD relacional + JOIN + documento JSON) e `test_app.py` (smoke test da API HTTP, incluindo confirmação de que `POST /api/mensagem` usa o agente local por padrão). Rodar com `python -m unittest discover -p "test_*.py"`.

**Impacto:** Baixo. Cobertura cobre os caminhos principais do agente, banco e API.

---

## Conclusão

MVP validado manualmente. Todos os critérios funcionais atingidos. Aprovado para gate de segurança e publicação no GitHub.
