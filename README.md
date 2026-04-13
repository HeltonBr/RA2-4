# Analisador Sintatico LL(1) - Fase 2

Projeto em desenvolvimento para a disciplina de Linguagens Formais e Compiladores da PUC-PR.

Esta fase amplia a Fase 1 para construir um analisador sintatico LL(1), gerar a arvore sintatica e preparar a geracao de Assembly ARMv7 a partir da AST.

## Situacao atual

- Etapa 1 concluida: analise integral do enunciado, definicao de arquitetura base e planejamento de evolucao.
- Compatibilidade alvo: formato de tokens serializados em `generated/tokens_ultima_execucao.txt` usado no repositorio publico `HeltonBr/RA1-4-RA1`.
- Linguagem escolhida: Python 3.13.

## Estrutura inicial

- `src/analisador_sintatico_ll1/`: codigo-fonte principal.
- `tests/`: testes automatizados e fixtures.
- `docs/`: requisitos, estrategia de implementacao e documentacao tecnica.

## Funcoes-alvo da atividade

O projeto sera organizado em torno das funcoes solicitadas no enunciado:

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

## Proximos marcos

O roteiro detalhado de 8 evolucoes planejadas esta em `docs/plano-evolucao.md`.

O mapeamento completo dos requisitos do enunciado esta em `docs/analise-requisitos.md`.
