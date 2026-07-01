# Status do Projeto - AutoFlow IA

## Identificacao

- Nome: AutoFlow IA
- Tipo: projeto de portfolio / automacao com IA
- Prioridade: principal agora
- Pasta: `01_Projeto_AutoFlow_IA`
- Status publico/privado: candidato a GitHub publico apos revisao

## Objetivo

Demonstrar um MVP didatico em que uma mensagem entra por API, aciona um agente, executa ferramentas locais e registra dados em SQLite/JSON.

## Problema que resolve

Simula automacao conversacional com entrada por mensagem, decisao de ferramenta, execucao e registro.

## Usuario principal

Avaliador tecnico, recrutador ou entrevistador da OTG.

## Estado atual

Projeto ja tem codigo ativo e README. Precisa de revisao de seguranca, demo local e narrativa tecnica.

## O que ja existe

- `app.py`
- `agente.py`
- `banco.py`
- `frontend/`
- `README.md`
- `legado/artefatos_gerados/`

## O que falta

- Confirmar demo local sem dependencia critica de webhook externo.
- Revisar README.
- Revisar seguranca.
- Decidir se precisa de prototipo navegavel separado.

## Fonte principal atual

Codigo ativo + README.

## Existe prototipo?

Nao aprovado.

## Existe legado?

Sim. Apenas artefatos gerados em `legado/artefatos_gerados/`.

## Existe codigo?

Sim.

## Existe risco de segredo?

Possivel. Revisar URLs externas e qualquer arquivo local antes de publicacao.

## Gate atual

`01_CONTEXTO` pendente.

## Proxima acao recomendada

Criar Context Pack e rodar checklist de seguranca/publicacao.
