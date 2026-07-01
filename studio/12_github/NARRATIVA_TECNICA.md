# NARRATIVA TÉCNICA — AutoFlow IA

> Etapa: `12_GITHUB` | Status: APROVADO | Data: 2026-07-01

---

## O projeto em uma frase

AutoFlow IA demonstra, num único codebase de ~400 linhas sem nenhuma dependência externa, os cinco padrões fundamentais de um sistema de integração com IA: API REST, webhook de automação, agente com function calling, banco relacional e banco de documentos.

---

## Por que este projeto existe

Foi construído para uma entrevista técnica para a vaga de Especialista em Automação e Integração com IA (OTG). Cada linha de código mapeia diretamente a um requisito da vaga.

O projeto responde à pergunta prática que toda entrevista técnica de IA faz: "você consegue integrar uma API, criar um agente que toma decisões e persistir dados em dois paradigmas diferentes?" — com código que qualquer engenheiro pode ler e rodar em 10 segundos.

---

## Decisões técnicas que valem mencionar

**Por que Python puro?**
A dependência zero é intencional. O foco da demo é nos padrões (webhook → agente → banco), não no setup. `pip install` é um atrito desnecessário numa entrevista ao vivo.

**Por que o agente não usa LLM real?**
Porque o LLM substitui apenas o classificador — o resto do código (ferramentas, loop, banco) é idêntico. `chamar_llm_real()` em `agente.py` é o esqueleto documentado que mostra onde plugar um modelo real.

**Por que SQLite e JSON no mesmo módulo?**
Para tornar explícita a diferença entre os paradigmas. `banco.py` tem as duas implementações lado a lado — o entrevistador lê um arquivo e entende os dois modelos.

---

## Estrutura da narrativa no README

O README público já cobre:
- Por que o projeto existe (mapeamento vaga → código)
- Funcionalidades com o pattern de cada uma
- Como rodar (um comando)
- Mapa do código (qual arquivo faz o quê)
- Endpoints documentados
- Ferramentas do agente
- Como plugar LLM real

---

## O que NÃO dizer no README

- Não mencionar que foi construído para uma vaga específica da OTG (README já não menciona)
- Não prometer integração com WhatsApp/Telegram real que não existe
- Não usar linguagem de produto — é educacional/portfólio

---

## Commits para publicação inicial

```
feat: AutoFlow IA — agente com function calling, API REST e modelagem dual
docs: README com mapeamento de padrões e instruções de uso
chore: .gitignore para dados gerados em runtime
```
