# Padrões de Prompt — AutoFlow IA

## Para adicionar uma nova ferramenta ao agente

```
No AutoFlow IA (agente.py), adicione a ferramenta [nome] que [o que faz].
Regras:
- A ferramenta deve ser adicionada ao dicionário FERRAMENTAS
- A função recebe um dict de args e retorna uma string de resposta
- A classificação de intenção deve detectar [palavras-chave] e mapear para essa ferramenta
Pronto quando: mensagem "[exemplo]" no chat retorna a resposta esperada.
```

## Para adicionar uma rota REST

```
No AutoFlow IA (app.py), adicione o endpoint [MÉTODO] /api/[rota] que [o que faz].
Deve: validar [campos], chamar banco.[função](), retornar JSON com status [código].
Pronto quando: curl [MÉTODO] http://localhost:8000/api/[rota] retorna [resposta esperada].
```

## Para estender o banco

```
No banco.py do AutoFlow IA, adicione [função] que [o que faz] na tabela [nome].
Siga o padrão existente: conexao() → execute() → commit() → close().
Pronto quando: a função é chamada e [critério verificável].
```
