# Analisador Sintatico LL(1) - Fase 2

Projeto da disciplina de Linguagens Formais e Compiladores da PUC-PR.

Esta fase amplia a Fase 1 para construir um analisador sintatico LL(1), gerar a arvore sintatica e emitir Assembly ARMv7 diretamente a partir da AST.

## Informacoes institucionais

- Instituicao: Pontificia Universidade Catolica do Parana (PUC-PR)
- Ano: 2026
- Disciplina: Linguagens Formais e Compiladores
- Professor: Frank Coelho de Alcantara
- Integrante: Helton Tessari Brandao - `HeltonBr`
- Grupo no Canvas: `RA2-4`

## Situacao atual

- Entrega publicada e validada no repositorio publico `HeltonBr/RA2-4`.
- Pipeline completo implementado: leitura de tokens, gramatica LL(1), parser descendente recursivo, AST e geracao de Assembly ARMv7.
- Tres arquivos de teste validos, cenarios invalidos, auditoria automatizada e checklist final estao presentes no repositorio.
- Testes adicionais de variacao de formato cobrem espacos extras, tabs, linhas em branco, comentarios e estruturas `SEQ` longas em uma mesma linha.
- A linha do tempo das etapas concluida/testada fica em `docs/linha-do-tempo.md`.
- Compatibilidade mantida com o formato serializado de tokens da Fase 1.
- Ambiente local validado com Python 3.9 a partir da raiz do repositorio.
- Validacao final registrada com `python -m unittest discover -s tests -p "test_*.py" -v` e 30 testes aprovados.

## Estrutura do repositorio

- `AnalisadorSintatico.py`: ponto de entrada principal do projeto.
- `src/analisador_sintatico_ll1/`: codigo-fonte principal.
- `tests/`: arquivos de teste validos, invalidos e suite automatizada.
- `docs/`: requisitos, estrategia, linha do tempo e documentacao tecnica gerada.
- `generated/`: tokens da ultima execucao, AST em JSON e ultimo Assembly gerado.

## Execucao

Para processar um arquivo de teste:

```powershell
python AnalisadorSintatico.py tests/teste1.txt
```

Se preferir executar como modulo:

```powershell
python -m analisador_sintatico_ll1 tests/teste1.txt
```

Ao final da execucao, o projeto atualiza:

- `generated/tokens_ultima_execucao.txt`
- `generated/arvore_ultima_execucao.json`
- `generated/ultimo_assembly.s`
- `docs/arvore_ultima_execucao.md`
- `docs/gramatica.md`
- `docs/first_follow.md`
- `docs/tabela_ll1.md`

## Testes

Para rodar a suite automatizada:

```powershell
python -m unittest discover -s tests -p "test_*.py" -v
```

Observacao: o repositorio inclui um pacote-raiz compativel em `analisador_sintatico_ll1/`, entao os comandos acima funcionam no diretorio raiz sem precisar configurar `PYTHONPATH` manualmente.

Os arquivos em `tests/variacoes/` reforcam a validacao de generalizacao do parser. Eles incluem espacos extras, tabs, linhas em branco, comentarios e operacoes encadeadas por `SEQ` em uma mesma declaracao.

## Depuracao e validacao

Fluxo sugerido para depurar a ultima execucao:

1. Rodar `python AnalisadorSintatico.py tests/teste1.txt`.
2. Conferir se os arquivos em `generated/` foram atualizados.
3. Abrir `docs/arvore_ultima_execucao.md` para validar a estrutura da AST.
4. Inspecionar `generated/ultimo_assembly.s`.
5. Validar o Assembly no CPULATOR ARMv7 DE1-SoC.

Referencia do simulador:

- https://cpulator.01xz.net/?sys=arm-de1soc

## Funcoes principais

- `lerTokens(arquivo)`
- `construirGramatica()`
- `parsear(tokens, tabela_ll1)`
- `gerarArvore(derivacao)`
- `gerarAssembly(arvore)`

## Sintaxe canonica proposta

Para manter a linguagem estritamente LL(1), a sintaxe canonica em documentacao e testes seguira estas formas:

- Inicio do programa: `(START)`
- Fim do programa: `(END)`
- Operacao aritmetica: `(<expr> <expr> OP)`
- Consulta a resultado anterior: `(<expr> RES)`
- Gravacao em memoria: `(<expr> MEM)`
- Leitura de memoria: `(MEM)`
- Operacao relacional: `(<expr> <expr> REL)`
- Sequencia de comandos: `(<stmt> <stmt> SEQ)`
- Decisao simples: `(<expr> <stmt> IF)`
- Decisao com senao: `(<expr> <stmt> <stmt> IFELSE)`
- Laco: `(<expr> <stmt> WHILE)`

Observacao importante: o uso de memoria como operando e documentado na forma canonica `(MEM)` para preservar a previsibilidade da gramatica LL(1). Compatibilidades adicionais com a Fase 1 nao fazem parte da especificacao formal desta entrega.

## Documentacao e artefatos

- Requisitos analisados: `docs/analise-requisitos.md`
- Planejamento incremental: `docs/plano-evolucao.md`
- Linha do tempo das tarefas: `docs/linha-do-tempo.md`
- Auditoria automatizada da entrega: `docs/auditoria-entrega.md`
- Auditoria do padrao de avaliacao por IA: `docs/auditoria-avaliador-ia.md`
- Checklist final de entrega: `docs/checklist-entrega.md`
- Roteiro de envio e congelamento: `docs/roteiro-envio.md`
- Roteiro de defesa: `docs/roteiro-defesa.md`
- Kit de demonstracao da defesa: `defesa/`
- Sintaxe de controle: `docs/sintaxe_controle.md`
- Gramatica, FIRST/FOLLOW e tabela LL(1): gerados em `docs/`
- Ultima arvore sintatica em markdown: `docs/arvore_ultima_execucao.md`
- Ultimos artefatos persistidos: `generated/`

## Espelho de defesa

Para manter uma copia separada da pasta oficial antes do prazo:

```powershell
.\sincronizar_para_githubmirror.ps1
```

Esse comando cria ou atualiza a pasta irma `Githubmirror`. A ideia e usar `Github` como pasta oficial ate o prazo e, depois do congelamento, continuar treinando e demonstrando apenas em `Githubmirror`.
O espelho copia tambem o historico Git da pasta oficial, para manter `Githubmirror` como copia fiel no momento da sincronizacao.

## Exemplo rapido

Exemplo de estrutura valida da linguagem:

```text
(START)
(10 X)
((X) 2 +)
(((X) 0 >) (((X) 1 -) X) WHILE)
(END)
```

## Estado de entrega

- Implementacao, documentacao tecnica, testes e artefatos obrigatorios estao organizados no repositorio.
- A validacao local pode ser refeita integralmente a partir da raiz com os comandos documentados neste README.
- A pasta `generated/` guarda os artefatos da ultima execucao canonica com `tests/teste3.txt`.
- A pasta `defesa/` e a pasta espelho `Githubmirror` sao apoios de demonstracao/treino; a entrega oficial permanece neste repositorio.
- Apos `24/04/2026 23:59` no fuso `America/Sao_Paulo`, a pasta oficial deve permanecer congelada.
