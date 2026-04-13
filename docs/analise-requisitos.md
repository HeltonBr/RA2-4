# Analise detalhada dos requisitos

## 1. Requisitos funcionais obrigatorios

### Entrada e pipeline

- O programa precisa processar um programa completo delimitado por `(START)` e `(END)`.
- O parser deve consumir um vetor ou string de tokens gerado a partir da Fase 1.
- O executavel deve receber um arquivo como argumento de linha de comando, sem menu interativo.
- O projeto precisa manter compatibilidade pratica com o formato de tokens serializado pelo repositorio de referencia da Fase 1.

### Linguagem

- Suportar operacoes `+`, `-`, `*`, `|`, `/`, `%`, `^`.
- Suportar inteiros e reais.
- Suportar aninhamento arbitrario.
- Suportar os comandos especiais `(N RES)`, `(<expr> MEM)` e `(MEM)`.
- Definir sintaxe documentada para decisao e repeticao respeitando parenteses e padrao pos-fixado.

### Analise sintatica

- A gramatica deve ser LL(1).
- Precisamos documentar as producoes completas da linguagem.
- Precisamos calcular e documentar FIRST e FOLLOW para cada nao-terminal.
- Precisamos construir a tabela LL(1).
- O parser deve ser descendente recursivo, com buffer de entrada, pilha de analise e funcoes por nao-terminal.
- O parser deve gerar a arvore sintatica durante o parsing ou a derivacao necessaria para `gerarArvore`.

### Saidas e artefatos

- Gerar e persistir a arvore sintatica em texto ou JSON.
- Gerar Assembly ARMv7 para Cpulator.
- Manter os ultimos resultados da execucao no repositorio.
- Entregar um markdown com gramatica, FIRST/FOLLOW, tabela LL(1) e arvore sintatica da ultima execucao.

### Testes

- Minimo de 3 arquivos de teste.
- Cada arquivo com pelo menos 10 linhas.
- Cada arquivo deve cobrir todos os operadores.
- Cada arquivo deve conter todos os comandos especiais.
- Cada arquivo deve conter pelo menos um laco e uma decisao.
- Incluir inteiros, reais e memorias.
- Incluir erros lexicos e sintaticos.

## 2. Requisitos administrativos e de repositorio

- Repositorio publico no GitHub.
- Nome do repositorio deve seguir o nome do grupo no Canvas.
- Commits claros e organizados.
- Contribuicoes dos integrantes registradas com pull requests.
- Uso de issues e recomendado.
- Somente um integrante com escrita direta no repositorio.

## 3. Requisitos de documentacao

- README com instituicao, ano, disciplina, professor.
- Integrantes em ordem alfabetica.
- Instrucoes de compilacao, execucao e depuracao.
- Sintaxe das estruturas de controle.
- Exemplos de uso.

## 4. Decisoes tecnicas tomadas nesta etapa

### Linguagem e arquitetura

- Python foi escolhido por compatibilidade direta com a Fase 1 de referencia.
- O projeto sera modularizado em leitura de tokens, gramatica, parser, AST, Assembly e CLI.

### Compatibilidade com a Fase 1

- O formato de token tomado como base e o arquivo `generated/tokens_ultima_execucao.txt` do repositorio `HeltonBr/RA1-4-RA1`.
- O leitor de tokens precisara reconhecer blocos `[LINHA N]` e entradas `chave=valor` separadas por `;`.

### Sintaxe proposta para estruturas novas

- Sequenciamento: `(<stmt> <stmt> SEQ)`
- Decisao simples: `(<expr> <stmt> IF)`
- Decisao com senao: `(<expr> <stmt> <stmt> IFELSE)`
- Laco: `(<expr> <stmt> WHILE)`
- Relacionais previstos: `>`, `<`, `>=`, `<=`, `==`, `!=`

Essas escolhas mantem o estilo pos-fixado e permitem documentar uma gramatica canonica LL(1).

## 5. Riscos identificados

- O enunciado exige simultaneamente compatibilidade com a Fase 1 e uma gramatica LL(1) estrita. Alguns atalhos permissivos da Fase 1, como memoria nua como operando, podem gerar ambiguidades formais. A estrategia adotada e manter uma sintaxe canonica rigorosa e tratar compatibilidades extras como opcional.
- A parte de Assembly para `IF`, `IFELSE` e `WHILE` exige convencao clara de verdade booleana e controle de labels.
- O nome final do repositorio no GitHub depende do nome oficial do grupo no Canvas, que ainda precisa ser confirmado antes da publicacao.
- Os nomes completos de todos os integrantes ainda nao foram preenchidos nas cabecalhos obrigatorios do codigo.

## 6. Checklist de aceite final

- [ ] `lerTokens()` implementada e testada com arquivo de tokens serializados.
- [ ] `construirGramatica()` implementada com EBNF, FIRST, FOLLOW e tabela LL(1).
- [ ] `parsear()` implementada com mensagens de erro por linha e coluna.
- [ ] `gerarArvore()` implementada e persistindo JSON/texto.
- [ ] `gerarAssembly()` gerando saida ARMv7 coerente com a AST.
- [ ] `main()` executando por linha de comando.
- [ ] 3 arquivos de teste completos.
- [ ] Casos invalidos cobrindo erros lexicos e sintaticos.
- [ ] README completo.
- [ ] Markdown tecnico com gramatica, FIRST/FOLLOW, tabela LL(1) e ultima arvore.
- [ ] Ultima execucao documentada no repositorio.
- [ ] Historico de commits limpo e evolutivo.
