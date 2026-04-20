# Roteiro de Envio e Congelamento

Este roteiro organiza os ultimos passos de envio da Fase 2 e fixa o ponto a partir do qual nenhuma alteracao adicional deve ser feita no repositorio local.

## Prazo de congelamento

- Data limite da entrega: `24/04/2026`
- Horario limite da entrega: `23:59`
- Fuso considerado: `America/Sao_Paulo`

Regra de congelamento: apos `24/04/2026 23:59`, fica proibido realizar qualquer alteracao na pasta de trabalho, gerar novos artefatos, criar novos commits ou executar qualquer acao que produza modificacao local relacionada a esta entrega.

## Roteiro antes do prazo

1. Rodar `python -m unittest discover -s tests -p "test_*.py" -v`.
2. Rodar `python AnalisadorSintatico.py tests/teste3.txt`.
3. Conferir os artefatos em `generated/` e `docs/arvore_ultima_execucao.md`.
4. Conferir se `git status --short` esta limpo.
5. Garantir que o branch `main` publicado no GitHub esteja atualizado antes do prazo.
6. Abrir o repositorio publicado e revisar rapidamente README, `docs/` e `generated/`.

## O que nao fazer apos o prazo

- Nao editar codigo, documentacao, testes ou artefatos.
- Nao rodar comandos que reescrevam `generated/` ou `docs/arvore_ultima_execucao.md`.
- Nao criar commits adicionais.
- Nao reabrir ciclos de ajuste local para esta atividade.

## Acoes permitidas sem alterar a entrega

- Consultar o repositorio ja publicado.
- Ler os arquivos locais sem regravacao.
- Conferir historico de commits ja existente.
