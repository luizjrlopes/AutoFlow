# 🤖 AutoFlow IA — Central de Automação e Integração

Mini-aplicação que **demonstra, num projeto só, cada requisito da vaga** de Especialista em Automação e Integração com IA (OTG). Serve para 3 coisas:

1. **Apresentar** na entrevista ("montei um projeto que cobre os pontos da vaga").
2. **Estudar** lendo o próprio código — tudo comentado em português.
3. **Evoluir** depois (plugar uma IA real, subir no GitHub como portfólio).

Feito **só com a biblioteca padrão do Python** — não precisa instalar nada.

---

## ▶️ Como rodar

1. Abra o terminal nesta pasta (`03_Projeto_AutoFlow_IA`).
2. Rode:

   ```bash
   python app.py
   ```

   *(no Windows pode ser `python app.py`; se não funcionar, tente `py app.py`)*
3. Abra no navegador: **http://localhost:8000**
4. No chat, toque nos botões de exemplo ou digite. Para parar: `Ctrl + C` no terminal.

> Na primeira execução, o app cria sozinho o banco `dados.db` e o `conversas.json` com dados de exemplo.

---

## 🧩 Como cada requisito da vaga aparece no código

| Requisito da vaga | Onde está | O que olhar |
|---|---|---|
| **Consumo / criação de APIs REST** | `app.py` | Métodos `do_GET`/`do_POST`, respostas em JSON, status codes (200/201/400/404) |
| **Automação (gatilho → ação)** | `app.py` → `POST /api/mensagem` | O "webhook" que recebe a mensagem e dispara o agente (mesma ideia do gatilho no n8n/Make) |
| **Criação de agentes com IA** | `agente.py` | Loop do agente: classifica intenção → escolhe ferramenta → executa → responde |
| **Ferramentas do agente (function calling)** | `agente.py` → dicionário `FERRAMENTAS` | Cada ferramenta é uma ação que o agente pode chamar |
| **Modelagem de dados — relacional** | `banco.py` | Tabelas `clientes` e `pedidos` com PK e FK; consulta com `JOIN` |
| **Modelagem de dados — não relacional** | `banco.py` | `conversas.json` guarda cada interação como documento flexível |
| **WhatsApp / Telegram** | `frontend/index.html` | Chat que simula o canal e chama o webhook; o campo `canal` identifica a origem |
| **Comunicação / homologação / implantação** | (conceito) | Veja a seção "Glossário" abaixo e o guia da entrevista |

### Sugestão de ordem de leitura para estudar
1. `banco.py` — como os dados são guardados (relacional + documento).
2. `agente.py` — como o agente decide o que fazer.
3. `app.py` — como tudo é exposto via API REST e como o webhook dispara o agente.
4. `frontend/index.html` — como um cliente consome a API.

---

## 🔌 Como plugar uma IA real (opcional, para depois)

Hoje o agente usa **regras** (em `agente.py`, função `classificar`) para o app rodar sem custo e sem chave. Para usar um LLM de verdade:

- Veja a função `chamar_llm_real` no fim de `agente.py` — há um esqueleto comentado usando `function calling`.
- A estrutura (ferramentas + loop) **continua igual**; só troca o "cérebro" que escolhe a ferramenta.

Isso é exatamente o ponto que você pode comentar na entrevista: *"deixei o agente pronto para receber um LLM via function calling"*.

---

## 📁 Estrutura

```
03_Projeto_AutoFlow_IA/
├── app.py              # servidor + API REST + webhook
├── agente.py           # o agente de IA (intenção, ferramentas, loop)
├── banco.py            # dados: SQLite (relacional) + JSON (documento)
├── frontend/
│   └── index.html      # chat estilo WhatsApp que consome a API
└── README.md           # este arquivo
```
*(`dados.db` e `conversas.json` são criados automaticamente ao rodar.)*

---

## 📖 Glossário rápido (para a entrevista)

- **Webhook**: URL que recebe um evento de fora e dispara um fluxo. Aqui: `POST /api/mensagem`.
- **Agente de IA**: LLM que decide passos e usa ferramentas para cumprir um objetivo (modelo + ferramentas + memória, em loop).
- **Function calling**: quando o modelo escolhe e chama uma ferramenta/ação.
- **PK / FK**: chave primária identifica a linha; chave estrangeira liga a outra tabela.
- **Relacional × NoSQL**: tabelas com relações × documentos flexíveis.
- **Levantamento / homologação / implantação**: entender o que fazer → validar → colocar em produção.

---

## 🚀 Subir no GitHub (vira item de portfólio)

```bash
git init
git add .
git commit -m "AutoFlow IA — automação com agente de IA, API REST e modelagem de dados"
# crie um repositório vazio no GitHub e então:
git remote add origin https://github.com/SEU_USUARIO/autoflow-ia.git
git push -u origin main
```

> Dica: adicione um `.gitignore` com `dados.db`, `conversas.json` e `__pycache__/` para não versionar dados gerados.
