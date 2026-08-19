# AutoFlow IA — Central de Automação e Integração com Agentes

[English](README.md) | [Português](README.pt-BR.md)

Central de automação construída em Python puro que demonstra os padrões centrais de sistemas de integração com IA: **API REST**, **webhook como gatilho de automação**, **agente com function calling** e **modelagem de dados relacional + não relacional** — tudo rodando com zero dependências externas.

## Por que este projeto

Automações modernas com IA combinam três camadas que raramente aparecem juntas num único projeto didático:

1. **Transporte** — receber eventos de canais externos via API REST;
2. **Decisão** — um agente que classifica a intenção e escolhe a ferramenta certa;
3. **Dados** — persistência dual: relacional para estruturas fixas e documento para logs flexíveis.

O projeto implementa essas três camadas em um codebase pequeno e comentado, sem frameworks externos. Qualquer pessoa com Python 3 instalado consegue executá-lo localmente.

## Funcionalidades

- **API REST completa** com `GET` e `POST`, status codes e respostas JSON;
- **Webhook de automação** em `POST /api/mensagem`;
- **Agente de IA** com classificação de intenção, seleção de ferramenta e registro da resposta;
- **Function calling pattern** com catálogo `FERRAMENTAS` e cinco ações;
- **Banco relacional SQLite** com `clientes`, `pedidos`, chaves e `JOIN`;
- **Banco de documentos JSON** para registro flexível das interações;
- **Frontend de chat** que consome a própria API e exibe dados em tempo real.

## Como rodar

```bash
python app.py
```

Abra `http://localhost:8000` no navegador. Na primeira execução o app cria automaticamente o banco e popula dados de exemplo. Para parar: `Ctrl+C`.

> Requer apenas Python 3. Nenhum `pip install` é necessário. Por padrão, nenhuma chamada de rede é feita: o webhook `POST /api/mensagem` usa o agente local. Uma integração opcional com n8n pode ser ativada por `N8N_WEBHOOK_URL`; veja `docs/04-operacao/variaveis-de-ambiente.md`.

## Mapa do código

| Arquivo | Responsabilidade |
|---|---|
| `app.py` | Servidor HTTP, rotas REST e webhook |
| `agente.py` | Classificação de intenção, catálogo de ferramentas e loop do agente |
| `banco.py` | SQLite relacional + JSON documental |
| `frontend/index.html` | Chat e painel de dados consumindo a API |

**Ordem de leitura sugerida:** `banco.py` → `agente.py` → `app.py` → `frontend/index.html`

## Endpoints

| Método | Rota | Descrição |
|---|---|---|
| `GET` | `/` | Serve o frontend |
| `GET` | `/api/clientes` | Lista clientes |
| `GET` | `/api/pedidos` | Lista pedidos com JOIN |
| `GET` | `/api/conversas` | Lista conversas |
| `POST` | `/api/mensagem` | Webhook que recebe mensagem e dispara o agente |
| `POST` | `/api/clientes` | Cria novo cliente |

## Ferramentas do agente

| Ferramenta | Quando é acionada |
|---|---|
| `consultar_cliente` | consultas sobre cliente ou telefone |
| `criar_pedido` | criação de pedido |
| `status_pedido` | consulta de status por número do pedido |
| `listar_produtos` | produtos, planos e preços |
| `fallback` | qualquer outra mensagem |

## Como plugar um LLM real

O agente usa regras hoje para rodar sem custo. Para usar um modelo real:

1. implemente `chamar_llm_real()` em `agente.py`;
2. substitua o corpo de `classificar()` pela chamada ao LLM;
3. mantenha o restante do fluxo de ferramentas, loop e persistência.

## Limites do projeto e evolução para produção

| Limite atual | Em produção |
|---|---|
| Sem autenticação/autorização | Adicionar login e controle de acesso |
| SQLite em arquivo único | Migrar para Postgres/MySQL com pool de conexões |
| Agente por regras | Conectar um LLM real mantendo a fronteira de ferramentas |
| `http.server` sem HTTPS | Executar atrás de proxy com TLS ou PaaS gerenciado |
| Sem rate limiting robusto | Adicionar validação e throttling |
| Sem testes de carga | Executar testes antes de exposição pública |

## Estrutura de arquivos

```text
autoflow-ia/
├── app.py
├── agente.py
├── banco.py
├── frontend/
│   └── index.html
├── docs/
├── studio/
└── README.md
```

`dados.db` e `conversas.json` são gerados automaticamente e ignorados pelo `.gitignore`.

A pasta `studio/` registra o processo usado para planejar e revisar o projeto; não faz parte do runtime da aplicação.
