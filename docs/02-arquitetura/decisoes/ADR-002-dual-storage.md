# ADR-002: Dois paradigmas de banco — SQLite (relacional) + JSON (documento)

**Data:** 2026-06-22  
**Status:** Aceita

## Contexto

A vaga exige demonstrar conhecimento tanto de modelagem relacional quanto não relacional. Usar só um paradigma não cobre o requisito.

## Decisão

**SQLite para dados estruturados com relações** (clientes, pedidos com FK) e **JSON para documentos flexíveis** (conversas, onde cada interação pode ter campos variados).

A divisão não é arbitrária: segue o critério de adequação dos dados ao modelo. Clientes e pedidos têm schema fixo e relação FK — ideal para relacional. Conversas variam por ferramenta usada (cada uma pode ter campos diferentes no JSON) — ideal para documento.

## Consequências

**Positivas:** Demonstra os dois paradigmas; justificativa técnica real, não apenas acadêmica  
**Negativas:** Dois mecanismos de persistência para manter  
**Ponto de apresentação:** "Não escolhi JSON por capricho — escolhi porque conversa é documento flexível que varia por contexto."
