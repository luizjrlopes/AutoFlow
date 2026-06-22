# Modelos de Dados — AutoFlow IA

> Fonte de verdade: `banco.py` — função `inicializar()`

## Banco Relacional (SQLite)

### clientes

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `id` | INTEGER | Sim | PK (AUTOINCREMENT) |
| `nome` | TEXT | Sim | Nome do cliente |
| `telefone` | TEXT | Não | Telefone — UNIQUE |

**Dados de exemplo (seed):** Maria Silva (5521999990001), Joao Souza (5521999990002)

---

### pedidos

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `id` | INTEGER | Sim | PK (AUTOINCREMENT) |
| `cliente_id` | INTEGER | Sim | FK → clientes.id |
| `produto` | TEXT | Sim | Nome do produto |
| `status` | TEXT | Sim | Default: `'recebido'` |
| `criado_em` | TEXT | Não | ISO 8601 timestamp |

**Relacionamento:** `pedidos.cliente_id` → `clientes.id` (FOREIGN KEY)

**Query de join (em `listar_pedidos()`):**
```sql
SELECT p.id, c.nome AS cliente, p.produto, p.status, p.criado_em
FROM pedidos p
JOIN clientes c ON c.id = p.cliente_id
ORDER BY p.id DESC
```

---

## Banco Não Relacional (JSON)

### conversas.json — array de documentos

Cada documento (interação) tem estrutura flexível:

```json
{
  "canal": "whatsapp",
  "mensagem": "Quero criar um pedido para Maria",
  "resposta": "Pedido #3 criado para Maria Silva: Plano Basico. Status: recebido.",
  "ferramenta_usada": "criar_pedido",
  "em": "2026-06-22T10:30:00"
}
```

**Por que JSON (não relacional):**
- Cada conversa pode ter campos diferentes dependendo da ferramenta usada
- Demonstra o paradigma NoSQL de documentos flexíveis sem schema fixo
- Contrasta com a rigidez do SQLite (schema fixo com FK)

---

## Diagrama de relacionamentos

```
clientes 1 ──── N pedidos   (via cliente_id FK)
```
