# AutoFlow IA — Central de Automação e Integração com Agentes

Central de automação construída em Python puro que demonstra os padrões centrais de sistemas de integração com IA: **API REST**, **webhook como gatilho de automação**, **agente com function calling**, e **modelagem de dados relacional + não relacional** — tudo rodando com zero dependências externas.

## Por que este projeto

Automações modernas com IA combinam três camadas que raramente aparecem juntas num único projeto didático:

1. **Transporte** — receber eventos de canais externos (WhatsApp, Telegram, webhooks) via API REST
2. **Decisão** — um agente que classifica a intenção e escolhe a ferramenta certa (o padrão de function calling)
3. **Dados** — persistência dual: relacional para estruturas fixas com FK, documento para logs flexíveis

Este projeto implementa as três camadas num codebase pequeno e comentado, sem frameworks externos — qualquer pessoa com Python 3 instalado consegue rodar em 10 segundos.

---

## Funcionalidades

- **API REST completa** — `GET` e `POST` com status codes corretos (200/201/400/404), respostas em JSON
- **Webhook de automação** — `POST /api/mensagem` simula a chegada de uma mensagem e dispara o agente automaticamente
- **Agente de IA** — loop: classifica intenção → escolhe ferramenta → executa → registra resposta
- **Function calling pattern** — dicionário `FERRAMENTAS` com 5 ações que o agente pode invocar; pronto para substituir as regras por um LLM real
- **Banco relacional** (SQLite) — tabelas `clientes` e `pedidos` com chave primária, chave estrangeira e `JOIN`
- **Banco de documentos** (JSON) — cada interação salva como documento flexível, demonstrando o paradigma NoSQL
- **Frontend chat** — interface estilo WhatsApp que consome a própria API, com painel de dados em tempo real

---

## Como rodar

```bash
python app.py
```

Abra `http://localhost:8000` no navegador. Na primeira execução o app cria automaticamente o banco e popula dados de exemplo. Para parar: `Ctrl+C`.

> Requer apenas Python 3 — nenhum pacote externo (`pip install` não é necessário). Por padrão, nenhuma chamada de rede é feita: o webhook `POST /api/mensagem` sempre usa o agente local. Uma integração opcional com n8n pode ser ativada via variável de ambiente `N8N_WEBHOOK_URL` — veja `docs/04-operacao/variaveis-de-ambiente.md`.

---

## Mapa do código

| Arquivo | Responsabilidade |
|---------|-----------------|
| `app.py` | Servidor HTTP, rotas REST e webhook (`POST /api/mensagem`) |
| `agente.py` | Classificação de intenção, catálogo de ferramentas e loop do agente |
| `banco.py` | Camada de dados: SQLite (relacional) + JSON (documento) |
| `frontend/index.html` | Chat + painel de dados consumindo a API |

**Ordem de leitura sugerida:** `banco.py` → `agente.py` → `app.py` → `frontend/index.html`

---

## Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| `GET` | `/` | Serve o frontend |
| `GET` | `/api/clientes` | Lista clientes (SQLite) |
| `GET` | `/api/pedidos` | Lista pedidos com JOIN (SQLite) |
| `GET` | `/api/conversas` | Lista conversas (JSON) |
| `POST` | `/api/mensagem` | **Webhook** — recebe mensagem e dispara o agente |
| `POST` | `/api/clientes` | Cria novo cliente |

---

## Ferramentas do agente

| Ferramenta | Quando é acionada |
|-----------|------------------|
| `consultar_cliente` | "cliente", "telefone" |
| `criar_pedido` | "pedido" + "criar/quero/comprar" |
| `status_pedido` | "status" + número do pedido |
| `listar_produtos` | "produto", "plano", "preço" |
| `fallback` | qualquer outra mensagem |

---

## Como plugar um LLM real

O agente usa regras hoje para rodar sem custo. Para usar um modelo real:

1. Implemente `chamar_llm_real()` em `agente.py` — há um esqueleto comentado com o padrão de function calling via `urllib.request`
2. Substitua o corpo de `classificar()` pela chamada ao LLM
3. O resto do código (ferramentas, loop, banco) não muda

---

## Limites do projeto e como levaria para produção

Este é um projeto didático/portfólio, não uma aplicação pronta para produção. Limitações conhecidas e o que mudaria:

| Limite atual | Em produção |
|---|---|
| Sem autenticação/autorização | Adicionar login e controle de acesso por canal/cliente |
| SQLite em arquivo único, sem controle de concorrência real | Migrar para Postgres/MySQL com pool de conexões |
| Agente por regras (`re`), sem LLM real | Plugar um LLM via `chamar_llm_real()` (esqueleto já existe em `agente.py`) |
| Servidor `http.server` da stdlib, sem HTTPS | Deploy atrás de um proxy (nginx/Caddy) com TLS, ou PaaS gerenciado |
| Sem rate limiting nem validação de input mais robusta | Adicionar limites de tamanho/formato e throttling por IP/canal |
| Sem testes de carga | Rodar testes de carga antes de expor a um canal real (WhatsApp/Telegram) |

## Estrutura de arquivos

```
autoflow-ia/
├── app.py
├── agente.py
├── banco.py
├── frontend/
│   └── index.html
├── docs/
├── studio/        # memória de processo — como o projeto foi construído (gates, specs, handoffs)
└── README.md
```

`dados.db` e `conversas.json` são gerados automaticamente e ignorados pelo `.gitignore`.

A pasta `studio/` registra o pipeline usado para planejar e revisar este projeto (contexto, especificações, checklist de qualidade e segurança) — não faz parte do runtime da aplicação, é material de processo.
