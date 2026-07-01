# SPEC — Camada de Dados (AutoFlow IA)

> Etapa: `06_SPECS` | Status: IMPLEMENTADO | Data: 2026-07-01

---

## Responsabilidade

Camada única de persistência que implementa dois paradigmas de banco de dados no mesmo módulo, demonstrando de forma explícita a diferença entre relacional e documento.

**Arquivo:** `banco.py`

---

## Paradigma 1 — Banco Relacional (SQLite)

### Schema

```sql
CREATE TABLE IF NOT EXISTS clientes (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    nome    TEXT NOT NULL,
    email   TEXT NOT NULL,
    telefone TEXT
);

CREATE TABLE IF NOT EXISTS pedidos (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id  INTEGER NOT NULL REFERENCES clientes(id),
    produto     TEXT NOT NULL,
    valor       REAL NOT NULL,
    status      TEXT DEFAULT 'pendente'
);
```

### Operações expostas

| Função | SQL | Retorno |
|---|---|---|
| `listar_clientes()` | `SELECT * FROM clientes` | `list[dict]` |
| `buscar_cliente(nome)` | `SELECT * WHERE nome LIKE ?` | `dict \| None` |
| `criar_cliente(nome, email, tel)` | `INSERT INTO clientes` | `int` (id) |
| `listar_pedidos()` | `SELECT … JOIN clientes` | `list[dict]` |
| `buscar_pedido(id)` | `SELECT * WHERE id = ?` | `dict \| None` |
| `criar_pedido(cliente_id, produto, valor)` | `INSERT INTO pedidos` | `int` (id) |

### Arquivo gerado
`dados.db` — criado automaticamente no primeiro run. Em `.gitignore`.

---

## Paradigma 2 — Banco de Documentos (JSON)

### Estrutura do documento

```json
{
  "timestamp": "2026-07-01T16:00:00",
  "mensagem": "quero criar um pedido",
  "resposta": "Pedido criado com sucesso. ID: 3",
  "intencao": "criar_pedido"
}
```

Cada interação do agente gera um documento. Não há schema fixo — campos podem variar por intenção.

### Operações expostas

| Função | Ação | Retorno |
|---|---|---|
| `registrar_conversa(msg, resp, intencao)` | Append ao array JSON | `None` |
| `listar_conversas()` | Lê arquivo completo | `list[dict]` |

### Arquivo gerado
`conversas.json` — criado automaticamente. Em `.gitignore`.

---

## Inicialização

`banco.py` executa `inicializar_banco()` na importação:
- Cria `dados.db` se não existir
- Cria tabelas se não existirem
- Popula dados de seed (3 clientes, 4 pedidos) se banco estiver vazio
- Cria `conversas.json` vazio se não existir

---

## Critérios de aceite (retroativos)

- [x] Banco SQLite criado automaticamente no primeiro run
- [x] Tabelas com FK entre `pedidos.cliente_id` e `clientes.id`
- [x] JOIN retorna nome do cliente junto com pedido
- [x] JSON inicializado automaticamente, sem erro se arquivo não existir
- [x] Ambos os paradigmas vivem em `banco.py` — ponto único de acesso a dados
- [x] `dados.db` e `conversas.json` em `.gitignore`
