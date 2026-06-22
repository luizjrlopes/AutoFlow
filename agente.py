"""
agente.py — O agente de IA do AutoFlow.

Mostra o PADRÃO de um agente de IA, mesmo sem um LLM real plugado:

    1. recebe uma mensagem (ex.: do WhatsApp)
    2. CLASSIFICA a intenção do usuário
    3. ESCOLHE uma ferramenta (tool) adequada
    4. EXECUTA a ferramenta (que consulta/altera o banco)
    5. COMPÕE e devolve a resposta, registrando tudo

Num agente "de verdade", os passos 2 e 3 são feitos por um LLM usando
'function calling' (o modelo decide qual ferramenta chamar e com quais
argumentos). Aqui usamos regras simples para o app rodar sem custo e sem
chave — mas deixamos o ponto EXATO para plugar um LLM real (ver o fim do
arquivo, em 'chamar_llm_real').
"""
import re
import banco


# ----------------------------------------------------------------------
# CATÁLOGO DE FERRAMENTAS (tools) que o agente pode usar
# Cada ferramenta recebe um dicionário de argumentos e devolve um texto.
# ----------------------------------------------------------------------
def tool_consultar_cliente(args):
    cliente = banco.buscar_cliente(args.get("termo", ""))
    if cliente:
        return f"Cliente encontrado: {cliente['nome']} (tel {cliente['telefone']})."
    return "Não encontrei esse cliente na base."


def tool_criar_pedido(args):
    cliente = banco.buscar_cliente(args.get("cliente", ""))
    if not cliente:
        return "Para criar um pedido preciso de um cliente válido. Qual o nome?"
    produto = args.get("produto", "Plano Basico")
    pedido_id = banco.criar_pedido(cliente["id"], produto)
    return (
        f"Pedido #{pedido_id} criado para {cliente['nome']}: {produto}. "
        f"Status: recebido."
    )


def tool_status_pedido(args):
    pedido = banco.buscar_pedido(args.get("id"))
    if pedido:
        return (
            f"Pedido #{pedido['id']} ({pedido['produto']}) de {pedido['cliente']} "
            f"— status: {pedido['status']}."
        )
    return "Não achei esse pedido. Confere o número?"


def tool_listar_produtos(args):
    return "Produtos disponíveis: Plano Basico, Plano Pro e Consultoria."


def tool_fallback(args):
    return (
        "Posso ajudar com: consultar cliente, criar pedido, status de pedido "
        "ou listar produtos. O que você precisa?"
    )


# Registro das ferramentas — é isto que um LLM "enxergaria" para escolher.
FERRAMENTAS = {
    "consultar_cliente": tool_consultar_cliente,
    "criar_pedido": tool_criar_pedido,
    "status_pedido": tool_status_pedido,
    "listar_produtos": tool_listar_produtos,
    "fallback": tool_fallback,
}


# ----------------------------------------------------------------------
# CLASSIFICAÇÃO DA INTENÇÃO  (o "cérebro" que escolhe a ferramenta)
# ----------------------------------------------------------------------
def _extrair(padrao, texto):
    m = re.search(padrao, texto, re.IGNORECASE)
    return m.group(1).strip() if m else None


def classificar(mensagem):
    """
    Decide QUAL ferramenta usar e extrai os argumentos.

    >>> É AQUI que entraria um LLM real (OpenAI/Azure) com function calling. <<<
    Veja 'chamar_llm_real' no fim do arquivo para entender como trocar.
    """
    m = mensagem.lower()
    numero = re.search(r"pedido\s*#?\s*(\d+)", m)

    # 1) status de um pedido (tem a palavra 'status' e um número)
    if "status" in m and numero:
        return "status_pedido", {"id": int(numero.group(1))}

    # 2) criar pedido
    if "pedido" in m and any(p in m for p in ("criar", "quero", "comprar", "novo")):
        cliente = _extrair(r"para ([A-Za-zÀ-ÿ]+)", mensagem)
        produto = _extrair(r"\bde (.+)$", mensagem) or "Plano Basico"
        return "criar_pedido", {"cliente": cliente or "", "produto": produto}

    # 3) consultar cliente
    if "cliente" in m or "telefone" in m:
        termo = _extrair(r"cliente ([A-Za-zÀ-ÿ]+)", mensagem) or ""
        return "consultar_cliente", {"termo": termo}

    # 4) listar produtos / planos / preços
    if any(p in m for p in ("produto", "plano", "preço", "preco", "valor")):
        return "listar_produtos", {}

    # 5) nada reconhecido
    return "fallback", {}


# ----------------------------------------------------------------------
# LOOP DO AGENTE  (junta tudo)
# ----------------------------------------------------------------------
def responder(mensagem, canal="whatsapp"):
    ferramenta, args = classificar(mensagem)      # 1+2+3: decide a ação
    resposta = FERRAMENTAS[ferramenta](args)       # 4: executa a ferramenta
    banco.registrar_conversa(canal, mensagem, resposta, ferramenta)  # 5: registra
    return {"resposta": resposta, "ferramenta_usada": ferramenta, "args": args}


# ----------------------------------------------------------------------
# PONTO PARA PLUGAR UM LLM REAL  (opcional — não precisa para apresentar)
# ----------------------------------------------------------------------
def chamar_llm_real(mensagem):
    """
    Para usar uma IA de verdade, troque a função 'classificar' por uma chamada
    a um LLM com function calling. Esqueleto usando só a biblioteca padrão:

        import os, json, urllib.request

        chave = os.environ.get("OPENAI_API_KEY")
        corpo = {
            "model": "gpt-4o-mini",
            "messages": [
                {"role": "system", "content": "Você decide qual ferramenta usar."},
                {"role": "user", "content": mensagem},
            ],
            "tools": [...],   # descreva as FERRAMENTAS acima no formato da API
        }
        req = urllib.request.Request(
            "https://api.openai.com/v1/chat/completions",
            data=json.dumps(corpo).encode(),
            headers={"Authorization": f"Bearer {chave}",
                     "Content-Type": "application/json"},
        )
        resposta = json.load(urllib.request.urlopen(req))
        # ... ler qual ferramenta o modelo escolheu e chamar FERRAMENTAS[...]

    A estrutura do resto do código (ferramentas + loop) continua igual.
    """
    raise NotImplementedError("Configure uma chave de LLM para ativar a IA real.")
