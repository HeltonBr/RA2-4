# Checklist Final de Entrega

Este arquivo consolida o fechamento da Fase 2 como pacote de entrega e ajuda a revisar rapidamente o que a IA avaliadora tende a procurar.

## Identificacao e repositorio

- Repositorio da entrega: `RA2-4`
- Integrante autoral documentado: Helton Tessari Brandao - `HeltonBr`
- Disciplina, ano, instituicao, professor e grupo: registrados em `README.md`
- Ponto de entrada principal: `AnalisadorSintatico.py`

## Funcoes exigidas

- `lerTokens(arquivo)`: exposta em `analisador_sintatico_ll1/__init__.py`
- `construirGramatica()`: exposta em `analisador_sintatico_ll1/__init__.py`
- `parsear(tokens, tabela_ll1)`: exposta em `analisador_sintatico_ll1/__init__.py`
- `gerarArvore(derivacao)`: exposta em `analisador_sintatico_ll1/__init__.py`
- `gerarAssembly(arvore)`: exposta em `analisador_sintatico_ll1/__init__.py`

## Documentacao tecnica

- Gramatica formal: `docs/gramatica.md`
- FIRST e FOLLOW: `docs/first_follow.md`
- Tabela LL(1): `docs/tabela_ll1.md`
- Arvore da ultima execucao em markdown: `docs/arvore_ultima_execucao.md`
- Linha do tempo dos checkpoints: `docs/linha-do-tempo.md`
- Auditoria automatizada local: `docs/auditoria-entrega.md`
- Roteiro de envio e congelamento: `docs/roteiro-envio.md`

## Artefatos persistidos

- Tokens da ultima execucao: `generated/tokens_ultima_execucao.txt`
- Arvore sintatica em JSON: `generated/arvore_ultima_execucao.json`
- Ultimo Assembly ARMv7 gerado: `generated/ultimo_assembly.s`

## Arquivos de teste

- Programas validos: `tests/teste1.txt`, `tests/teste2.txt`, `tests/teste3.txt`
- Casos invalidos: `tests/invalidos/`
- Suite automatizada principal:
  - `tests/test_fase2_pipeline.py`
  - `tests/test_auditoria_entrega.py`

## Comandos de validacao

- Execucao principal:
  - `python AnalisadorSintatico.py tests/teste1.txt`
- Execucao como modulo:
  - `python -m analisador_sintatico_ll1 tests/teste1.txt`
- Suite automatizada:
  - `python -m unittest discover -s tests -p "test_*.py" -v`

## Fechamento manual antes de enviar

- Confirmar que o repositorio publicado no GitHub esta atualizado com os commits locais.
- Confirmar que `README.md` continua com instrucoes de execucao e depuracao.
- Confirmar que os arquivos em `generated/` correspondem a uma execucao valida recente.
- Confirmar que `docs/` contem os markdowns tecnicos exigidos.
- Confirmar que a suite automatizada continua verde a partir da raiz do repositorio.
- Interromper qualquer alteracao local apos `24/04/2026 23:59` no fuso `America/Sao_Paulo`.
