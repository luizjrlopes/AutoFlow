# Fluxos Principais — AutoFlow IA

## Fluxo 1: Usuário envia mensagem via chat (fluxo principal)

**Ator:** Usuário no browser  
**Pré-condição:** `python app.py` rodando em http://localhost:8000

**Passos:**
1. Usuário digita mensagem no chat e clica Enviar
2. Frontend faz `POST /api/mensagem` com `{ "mensagem": "...", "canal": "whatsapp" }`
3. `app.py` valida que mensagem não está vazia
4. `app.py` chama `agente.responder(mensagem, canal)`
5. `agente.classificar(mensagem)` determina `(ferramenta, args)` via regex/keywords
6. `FERRAMENTAS[ferramenta](args)` executa a ação no banco
7. `banco.registrar_conversa(canal, mensagem, resposta, ferramenta)` salva no JSON
8. Agente retorna `{ "resposta": "...", "ferramenta_usada": "...", "args": {...} }`
9. `app.py` retorna 200 com esse JSON
10. Frontend exibe a resposta no chat com a ferramenta usada (etiqueta roxa)

**Pós-condição:** Conversa salva no JSON; dados atualizados no SQLite (se ferramenta criou/modificou algo)

---

## Fluxo 2: Criar pedido via agente

**Mensagem exemplo:** "Quero criar um pedido para Maria"

**Passos:**
1. `classificar()` detecta "pedido" + "quero" → `("criar_pedido", {"cliente": "Maria", "produto": "Plano Basico"})`
2. `tool_criar_pedido(args)` chama `banco.buscar_cliente("Maria")`
3. Encontra Maria Silva → `banco.criar_pedido(cliente_id=1, produto="Plano Basico")`
4. Retorna `"Pedido #3 criado para Maria Silva: Plano Basico. Status: recebido."`

---

## Fluxo 3: Criar cliente via API REST

**Ator:** Qualquer cliente HTTP (curl, frontend, Postman)

**Passos:**
1. `POST /api/clientes` com `{ "nome": "Carlos", "telefone": "5521999990003" }`
2. `app.py` valida campo `nome`
3. `banco.criar_cliente("Carlos", "5521999990003")`
4. Retorna `201 Created` com `{ "id": 3, "nome": "Carlos", "telefone": "..." }`

---

## Fluxo 4: Plugar LLM real (evolutivo)

**Quando quiser evoluir o projeto:**

1. Configurar `OPENAI_API_KEY` (ou equivalente) como variável de ambiente
2. Em `agente.py`, substituir `classificar(mensagem)` por chamada a `chamar_llm_real(mensagem)`
3. Descrever as FERRAMENTAS no formato de tools da API (OpenAI function calling)
4. O resto do código não muda — mesmo loop, mesmo banco

**Ponto central para a entrevista:** *"A estrutura foi pensada para receber um LLM real sem reescrever nada. Só troco o cérebro que decide a ferramenta."*
