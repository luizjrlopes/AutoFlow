# ADR-001: Somente biblioteca padrão Python

**Data:** 2026-06-22  
**Status:** Aceita

## Contexto

O projeto precisa rodar no computador do entrevistador sem nenhum passo de instalação. A demo deve funcionar com apenas `python app.py`.

## Opções consideradas

### Opção A: Flask/FastAPI + pip install
- **Prós:** APIs mais elegantes, auto-documentação (Swagger)
- **Contras:** Requer pip, venv, ou Docker — fricção na entrevista

### Opção B: Somente stdlib (http.server, sqlite3, json)
- **Prós:** Zero fricção; roda em qualquer máquina com Python 3; demonstra conhecimento profundo da stdlib
- **Contras:** Código de servidor mais verboso que Flask

## Decisão

**Opção B.** O custo de verbosidade no `app.py` é compensado pela eliminação total de fricção de instalação — e demonstrar conhecimento da stdlib é, por si só, um diferencial técnico.

## Consequências

**Positivas:** Demo sem falhas por problema de ambiente  
**Negativas:** `app.py` com mais código boilerplate de HTTP do que Flask precisaria
