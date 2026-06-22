"""
banco.py — Camada de dados do AutoFlow IA.

Demonstra os DOIS tipos de modelagem que a vaga pede:

  • RELACIONAL (SQLite): tabelas 'clientes' e 'pedidos' com chave primária (PK)
    e chave estrangeira (FK). Bom para dados estruturados e com relações.

  • NÃO RELACIONAL (documento JSON): o arquivo 'conversas.json' guarda o
    histórico de mensagens como documentos flexíveis. Bom para dados que
    variam de formato (aqui, o log de cada interação do agente).

Tudo com a biblioteca padrão do Python (módulo sqlite3 já vem incluído).
"""
import sqlite3
import json
import os
import datetime

PASTA = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(PASTA, "dados.db")          # banco relacional
DOC = os.path.join(PASTA, "conversas.json")   # "banco" de documentos (NoSQL)


def conexao():
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row  # deixa acessar colunas por nome
    return con


def inicializar():
    """Cria as tabelas (se não existirem) e popula alguns dados de exemplo."""
    con = conexao()
    cur = con.cursor()

    # Tabela RELACIONAL 1: clientes  (id = chave primária)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            nome     TEXT NOT NULL,
            telefone TEXT UNIQUE
        )
    """)

    # Tabela RELACIONAL 2: pedidos  (cliente_id = chave estrangeira -> clientes.id)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS pedidos (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER NOT NULL,
            produto    TEXT NOT NULL,
            status     TEXT DEFAULT 'recebido',
            criado_em  TEXT,
            FOREIGN KEY (cliente_id) REFERENCES clientes(id)
        )
    """)
    con.commit()

    # Dados de exemplo (só na primeira vez)
    cur.execute("SELECT COUNT(*) FROM clientes")
    if cur.fetchone()[0] == 0:
        cur.executemany(
            "INSERT INTO clientes (nome, telefone) VALUES (?, ?)",
            [("Maria Silva", "5521999990001"), ("Joao Souza", "5521999990002")],
        )
        cur.execute(
            "INSERT INTO pedidos (cliente_id, produto, criado_em) VALUES (?, ?, ?)",
            (1, "Plano Basico", datetime.datetime.now().isoformat(timespec="seconds")),
        )
        con.commit()
    con.close()

    if not os.path.exists(DOC):
        _salvar_doc([])


# ----------------------------------------------------------------------
# OPERAÇÕES RELACIONAIS (SQL)
# ----------------------------------------------------------------------
def listar_clientes():
    con = conexao()
    rows = con.execute("SELECT * FROM clientes ORDER BY id").fetchall()
    con.close()
    return [dict(r) for r in rows]


def buscar_cliente(termo):
    """Busca por parte do nome OU telefone exato."""
    con = conexao()
    row = con.execute(
        "SELECT * FROM clientes WHERE nome LIKE ? OR telefone = ?",
        (f"%{termo}%", termo),
    ).fetchone()
    con.close()
    return dict(row) if row else None


def criar_cliente(nome, telefone):
    con = conexao()
    cur = con.execute(
        "INSERT INTO clientes (nome, telefone) VALUES (?, ?)", (nome, telefone)
    )
    con.commit()
    novo_id = cur.lastrowid
    con.close()
    return novo_id


def criar_pedido(cliente_id, produto):
    con = conexao()
    cur = con.execute(
        "INSERT INTO pedidos (cliente_id, produto, criado_em) VALUES (?, ?, ?)",
        (cliente_id, produto, datetime.datetime.now().isoformat(timespec="seconds")),
    )
    con.commit()
    novo_id = cur.lastrowid
    con.close()
    return novo_id


def listar_pedidos():
    """JOIN entre pedidos e clientes — mostra o poder do modelo relacional."""
    con = conexao()
    rows = con.execute(
        """
        SELECT p.id, c.nome AS cliente, p.produto, p.status, p.criado_em
        FROM pedidos p
        JOIN clientes c ON c.id = p.cliente_id
        ORDER BY p.id DESC
        """
    ).fetchall()
    con.close()
    return [dict(r) for r in rows]


def buscar_pedido(pedido_id):
    con = conexao()
    row = con.execute(
        """
        SELECT p.id, c.nome AS cliente, p.produto, p.status
        FROM pedidos p
        JOIN clientes c ON c.id = p.cliente_id
        WHERE p.id = ?
        """,
        (pedido_id,),
    ).fetchone()
    con.close()
    return dict(row) if row else None


# ----------------------------------------------------------------------
# OPERAÇÕES NÃO RELACIONAIS (documento JSON)
# ----------------------------------------------------------------------
def _ler_doc():
    with open(DOC, encoding="utf-8") as f:
        return json.load(f)


def _salvar_doc(dados):
    with open(DOC, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)


def registrar_conversa(canal, mensagem, resposta, ferramenta):
    """Cada interação vira um 'documento' flexível no arquivo JSON."""
    docs = _ler_doc()
    docs.append(
        {
            "canal": canal,
            "mensagem": mensagem,
            "resposta": resposta,
            "ferramenta_usada": ferramenta,
            "em": datetime.datetime.now().isoformat(timespec="seconds"),
        }
    )
    _salvar_doc(docs)


def listar_conversas():
    return _ler_doc()
