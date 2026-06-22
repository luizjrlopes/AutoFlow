# Visão Técnica — AutoFlow IA

## Stack

| Camada | Tecnologia | Justificativa |
|--------|-----------|---------------|
| Linguagem | Python 3.x | Exigência: somente stdlib — zero instalação |
| Servidor HTTP | `ThreadingHTTPServer` | Embutido, suporta múltiplas requisições |
| Banco relacional | SQLite (`sqlite3`) | Embutido no Python; demonstra FK e JOIN |
| Banco não relacional | JSON (`json`) | Arquivo de documentos flexíveis |
| Frontend | HTML/CSS/JS puro | Sem build step; servido pelo próprio servidor |

## Estrutura de pastas

```
03_Projeto_AutoFlow_IA/
├── app.py              # servidor HTTP + rotas REST + webhook
├── agente.py           # agente de IA (intenção + ferramentas + loop)
├── banco.py            # camada de dados (SQLite relacional + JSON documento)
├── frontend/
│   └── index.html      # chat + painel de dados
├── dados.db            # gerado automaticamente (SQLite)
├── conversas.json      # gerado automaticamente (JSON)
├── CLAUDE.md
├── README.md
└── docs/
```

## Diagrama de alto nível

```
[Browser - frontend/index.html]
          │
          │ POST /api/mensagem
          │ GET /api/clientes, /api/pedidos, /api/conversas
          ▼
[app.py - ThreadingHTTPServer :8000]
          │
          ├── GET /          → serve index.html
          ├── GET /api/*     → banco.py (SQLite + JSON)
          └── POST /api/mensagem → agente.py
                                        │
                                        ▼
                            [agente.py]
                            classificar(mensagem)
                                   │
                            FERRAMENTAS[nome](args)
                                   │
                            banco.registrar_conversa()
                                   │
                            retorna {resposta, ferramenta_usada, args}
```

## Loop do agente (ponto central da apresentação)

```
mensagem → classificar() → (ferramenta, args)
                                    ↓
                          FERRAMENTAS[ferramenta](args)
                                    ↓
                          banco.registrar_conversa()
                                    ↓
                          { resposta, ferramenta_usada, args }
```

## Como plugar LLM real (ponto de extensão)

A função `classificar()` em `agente.py` usa regras hoje. Para usar um LLM:
1. Implementar `chamar_llm_real(mensagem)` — esqueleto já existe no arquivo
2. Substituir o corpo de `classificar()` por uma chamada ao LLM
3. O resto do código (FERRAMENTAS, loop, banco) não muda

## Convenções de código

- **Nomes:** snake_case em Python
- **Idioma:** código em inglês exceto variáveis de negócio; comentários em português
- **Filosofia:** funções curtas, lógica explícita, sem "magic" — o código deve ser lido em 10 min
