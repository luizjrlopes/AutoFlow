# Mapa de Telas — AutoFlow IA

## Interface única

O AutoFlow IA tem uma única página (`frontend/index.html`) com layout em duas colunas.

## Estrutura da página

```
http://localhost:8000
├── Coluna esquerda: Chat estilo WhatsApp
│   ├── Header: "Atendimento AutoFlow · WhatsApp"
│   ├── Área de mensagens (bot + usuário)
│   ├── Botões de exemplo rápido
│   └── Input + botão Enviar
│
└── Coluna direita: Painel de dados (consome API REST)
    ├── Endpoints REST listados
    ├── Tabela de Pedidos (modelo relacional)
    └── Log de Conversas (documento/NoSQL)
```

## Endpoints REST (mapa de rotas)

| Método | Rota | O que faz |
|--------|------|-----------|
| GET | `/` | Serve o frontend (index.html) |
| GET | `/api/clientes` | Lista todos os clientes (SQLite) |
| GET | `/api/pedidos` | Lista pedidos com JOIN cliente (SQLite) |
| GET | `/api/conversas` | Lista conversas (JSON) |
| POST | `/api/mensagem` | **Webhook principal** — recebe mensagem e dispara agente |
| POST | `/api/clientes` | Cria novo cliente via API REST |

## Ferramentas do agente

| Ferramenta | Gatilho | O que faz |
|-----------|---------|-----------|
| `consultar_cliente` | "cliente", "telefone" | Busca cliente por nome/telefone no SQLite |
| `criar_pedido` | "pedido" + "criar/quero/comprar" | Cria pedido com FK ao cliente |
| `status_pedido` | "status" + número | Busca status do pedido via JOIN |
| `listar_produtos` | "produto", "plano", "preço" | Retorna lista de produtos disponíveis |
| `fallback` | qualquer outra | Orienta o usuário sobre as opções disponíveis |
