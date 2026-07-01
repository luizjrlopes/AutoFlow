# SPEC — Agente de IA (AutoFlow IA)

> Etapa: `06_SPECS` | Status: IMPLEMENTADO | Data: 2026-07-01

---

## Responsabilidade

O agente é o núcleo de decisão do sistema. Recebe uma mensagem de texto, determina a intenção do usuário e executa a ferramenta correspondente. É o equivalente prático do padrão de function calling usado por LLMs.

---

## Interface

**Entrada:** `string` — mensagem de texto livre do usuário
**Saída:** `string` — resposta gerada após execução da ferramenta

**Arquivo:** `agente.py`

---

## Loop do agente

```
mensagem_recebida
    → classificar(mensagem) → intenção : str
    → FERRAMENTAS[intenção](mensagem) → resposta : str
    → registrar_conversa(mensagem, resposta) → banco.py
    → retornar resposta
```

---

## Catálogo de ferramentas (FERRAMENTAS)

| Chave | Ferramenta | Acionamento | Ação |
|---|---|---|---|
| `consultar_cliente` | Consultar cliente | "cliente", "telefone", "quem é" | Busca cliente por nome no SQLite |
| `criar_pedido` | Criar pedido | "pedido" + "quero/criar/comprar" | Insere pedido no SQLite |
| `status_pedido` | Status do pedido | "status" + número | Busca pedido por ID |
| `listar_produtos` | Listar produtos/planos | "produto", "plano", "preço", "catálogo" | Retorna lista hardcoded de produtos |
| `fallback` | Fallback | qualquer outra entrada | Resposta genérica orientando o usuário |

---

## Regras de classificação

A classificação é determinística por palavras-chave (não probabilística):

```python
def classificar(mensagem: str) -> str:
    msg = mensagem.lower()
    if "cliente" in msg or "telefone" in msg:
        return "consultar_cliente"
    if "pedido" in msg and any(v in msg for v in ["quero", "criar", "comprar"]):
        return "criar_pedido"
    if "status" in msg:
        return "status_pedido"
    if any(p in msg for p in ["produto", "plano", "preço", "catálogo"]):
        return "listar_produtos"
    return "fallback"
```

---

## Extensão para LLM real

O esqueleto `chamar_llm_real(mensagem, ferramentas)` está comentado em `agente.py`. Para plugar um LLM real:

1. Implementar `chamar_llm_real()` com `urllib.request` (stdlib) chamando a API do modelo
2. Substituir o corpo de `classificar()` pela chamada ao LLM com `tool_use`
3. O catálogo `FERRAMENTAS`, o loop de execução e o registro em banco **não mudam**

---

## Critérios de aceite (retroativos)

- [x] Toda mensagem recebida pelo webhook resulta em uma resposta
- [x] A resposta correta é retornada para cada intenção mapeada
- [x] Mensagens não mapeadas retornam fallback (sem erro 500)
- [x] Toda interação é registrada em `conversas.json`
- [x] O catálogo `FERRAMENTAS` é o ponto único de adição de novas ações
