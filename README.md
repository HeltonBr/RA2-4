# Analisador Sintatico LL(1) - Fase 2

Projeto da disciplina de Linguagens Formais e Compiladores da PUC-PR.

Esta fase amplia a Fase 1 para construir um analisador sintatico LL(1), gerar a arvore sintatica e emitir Assembly ARMv7 diretamente a partir da AST.

## Informacoes institucionais

- Instituicao: Pontificia Universidade Catolica do Parana (PUC-PR)
- Ano: 2026
- Disciplina: Linguagens Formais e Compiladores
- Integrante: Helton Tessari Brandao - `HeltonBr`
- Grupo no Canvas: `RA2-4`

## Situacao atual

- Nucleo do analisador implementado: leitura de tokens, gramatica LL(1), parser descendente recursivo, AST e geracao inicial de Assembly.
- Tres arquivos de teste validos e dois cenarios invalidos ja foram adicionados em `tests/`.
- A linha do tempo das etapas concluida/testada fica em `docs/linha-do-tempo.md`.
- Compatibilidade mantida com o formato serializado de tokens da Fase 1.
- Ambiente local validado com Python 3.9.

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
$env:PYTHONPATH='src'
python -m analisador_sintatico_ll1.main tests/teste1.txt
```

## Testes

Para rodar a suite automatizada:

```powershell
$env:PYTHONPATH='src'
python -m unittest discover -s tests -p "test_*.py" -v
```

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

Observacao importante: o uso de memoria como operando sera documentado na forma canonica `(MEM)` para preservar a previsibilidade da gramatica LL(1). Compatibilidades adicionais com a Fase 1 poderao ser avaliadas depois, mas nao sao a base formal da gramatica.

## Documentacao e artefatos

- Requisitos analisados: `docs/analise-requisitos.md`
- Planejamento incremental: `docs/plano-evolucao.md`
- Linha do tempo das tarefas: `docs/linha-do-tempo.md`
- Sintaxe de controle: `docs/sintaxe_controle.md`
- Gramatica, FIRST/FOLLOW e tabela LL(1): gerados em `docs/`
- Ultima arvore sintatica em markdown: `docs/arvore_ultima_execucao.md`
- Ultimos artefatos persistidos: `generated/`

## Proximos marcos

- Refinar mensagens de erro e recuperacao basica.
- Revisar a documentacao final da entrega com os artefatos gerados.
- Consolidar novos commits pequenos e rastreaveis ao longo das proximas etapas.
