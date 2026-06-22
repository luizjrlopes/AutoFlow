# Regras de Negócio — AutoFlow IA

## Regras do webhook

**RN-001: Mensagem não pode ser vazia**
- **O que:** `POST /api/mensagem` com `mensagem` vazia ou ausente retorna 400
- **Por quê:** Agente não tem como classificar intenção de string vazia

**RN-002: Canal padrão é whatsapp**
- **O que:** Se o campo `canal` não for enviado, usa `"whatsapp"` como padrão
- **Por quê:** Compatibilidade — cliente pode omitir o campo

## Regras do agente

**RN-010: Toda intenção gera exatamente uma ferramenta**
- **O que:** `classificar()` sempre retorna um par `(ferramenta, args)` — nunca None
- **Por quê:** Em caso de intenção não reconhecida, cai no `fallback`

**RN-011: Toda interação é registrada no JSON**
- **O que:** `banco.registrar_conversa()` é chamado após toda resposta do agente
- **Por quê:** Demonstrar o paradigma não relacional (documento flexível por interação)

## Regras de dados

**RN-020: Pedido exige cliente válido**
- **O que:** `criar_pedido` verifica que o cliente existe antes de criar o pedido com FK
- **Por quê:** Integridade referencial — pedido sem cliente válido quebraria a FK

**RN-021: Nome do cliente é obrigatório**
- **O que:** `POST /api/clientes` sem `nome` retorna 400
- **Por quê:** Tabela `clientes` tem `nome TEXT NOT NULL`

**RN-022: Telefone é único por cliente**
- **O que:** Tabela `clientes` tem `telefone UNIQUE`
- **Por quê:** Evita duplicação de cliente pelo mesmo telefone
