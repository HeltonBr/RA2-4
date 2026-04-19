# Linha do Tempo do Projeto

## 2026-04-18 - Checkpoint 1

### Objetivo do checkpoint

Transformar o bootstrap inicial em um nucleo executavel do analisador sintatico LL(1), com funcoes reais no lugar dos `NotImplementedError`.

### Tarefas executadas

- Estrutura do pacote separada em `tokens.py`, `grammar.py`, `parser_ll1.py`, `ast_nodes.py`, `codegen_arm.py` e `errors.py`.
- Implementacao de `lerTokens()` com dois modos de entrada:
  - leitura direta de codigo-fonte da Fase 2;
  - leitura de tokens serializados no formato herdado da Fase 1.
- Definicao da gramatica canonica LL(1) para:
  - programa com `(START)` e `(END)`;
  - expressoes aritmeticas;
  - `RES`;
  - leitura e escrita de memoria;
  - `SEQ`, `IF`, `IFELSE` e `WHILE`;
  - operadores relacionais.
- Implementacao de `construirGramatica()` com calculo de `FIRST`, `FOLLOW` e tabela LL(1).
- Implementacao de `parsear(tokens, tabela_ll1)` com parser descendente recursivo guiado pela tabela.
- Implementacao de `gerarArvore()` com serializacao para dicionario e representacao textual.
- Implementacao inicial de `gerarAssembly(arvore)` com suporte a expressoes, relacionais e estruturas de controle.
- Ajuste de compatibilidade para o Python 3.9 presente no ambiente local.

### Validacoes realizadas neste checkpoint

- Compilacao do pacote com `python -m compileall src`.
- Construcao da gramatica LL(1) sem conflitos.
- Parsing ponta a ponta de um programa minimo com:
  - atribuicao em memoria;
  - leitura de memoria;
  - comparacao relacional;
  - laço `WHILE`.
- Suite automatizada executada com `python -m unittest discover -s tests -p "test_*.py" -v`.
- Geracao validada de Assembly para `tests/teste1.txt`, `tests/teste2.txt` e `tests/teste3.txt`.
- Atualizacao dos artefatos de entrega em `generated/` e `docs/` a partir de `tests/teste1.txt`.

### Arquivos principais impactados

- `src/analisador_sintatico_ll1/tokens.py`
- `src/analisador_sintatico_ll1/grammar.py`
- `src/analisador_sintatico_ll1/parser_ll1.py`
- `src/analisador_sintatico_ll1/ast_nodes.py`
- `src/analisador_sintatico_ll1/codegen_arm.py`
- `src/analisador_sintatico_ll1/core.py`
- `src/analisador_sintatico_ll1/main.py`

### Riscos ou pontos a observar

- A sintaxe canonica adotada para leitura de memoria e `(MEM)`, nao `MEM` solto.
- A validacao semantica ainda e basica; neste momento o foco esta em forma sintatica e geracao estrutural.
- Ainda vale reforcar a recuperacao de erros e revisar os detalhes finais da entrega.

### Proximas tarefas do pipeline

- Revisar mensagens de erro para casos mais profundos de aninhamento e estruturas de controle.
- Auditar a documentacao final com foco no que o professor avaliara automaticamente.
- Continuar a linha do tempo com novos checkpoints pequenos e commits rastreaveis.

## 2026-04-18 - Checkpoint 2

### Objetivo do checkpoint

Eliminar traceback bruto na interface de linha de comando, melhorar mensagens sintaticas mais provaveis e reforcar a cobertura automatizada do fluxo de erro.

### Tarefas executadas

- Inclusao de tratamento centralizado de excecoes em `main.py`.
- Impressao limpa de erros de dominio como `Erro: ...`, com retorno diferente de zero.
- Melhoria da mensagem de fim de arquivo inesperado para o caso classico de programa sem `(END)`.
- Melhoria das mensagens de predicao para estruturas pos-fixadas incompletas.
- Inclusao dos cabecalhos obrigatorios nas primeiras linhas de `__init__.py` e `main.py`.
- Expansao da suite automatizada para cobrir:
  - erro lexico no CLI sem traceback;
  - erro sintatico no CLI sem traceback;
  - mensagem clara para `END` ausente.

### Validacoes realizadas neste checkpoint

- Suite automatizada executada com `python -m unittest discover -s tests -p "test_*.py" -v`:
  - 7 testes passando.
- Execucao manual do CLI com:
  - `tests/invalidos/lexico_minusculo.txt`;
  - `tests/invalidos/sintaxe_sem_end.txt`;
  - `tests/teste2.txt`.
- Atualizacao dos artefatos da ultima execucao em `generated/` e `docs/` com base em `tests/teste2.txt`.

### Arquivos principais impactados

- `src/analisador_sintatico_ll1/main.py`
- `src/analisador_sintatico_ll1/parser_ll1.py`
- `src/analisador_sintatico_ll1/__init__.py`
- `tests/test_fase2_pipeline.py`

### Riscos ou pontos a observar

- Ainda nao ha recuperacao sintatica multiponto; o comportamento segue fail-fast, mas agora com mensagem clara.
- Falta uma auditoria final focada no checklist do professor para confirmar se nada administrativo/documental ficou para tras.

### Proximas tarefas do pipeline

- Auditar README, markdowns tecnicos e estrutura do repositorio contra o enunciado final.
- Revisar se os nomes e as assinaturas esperadas pelo professor estao todos visiveis e consistentes.
- Fechar o proximo commit com foco em documentacao final e acabamento de entrega.

## 2026-04-18 - Checkpoint 3

### Objetivo do checkpoint

Adicionar uma auditoria automatizada do proprio repositorio para validar os entregaveis como se estivessemos do lado da IA avaliadora.

### Tarefas executadas

- Criacao de `docs/auditoria-entrega.md` explicando o escopo da verificacao automatizada.
- Criacao de `tests/test_auditoria_entrega.py` com checagens para:
  - existencia e nao-vazio dos arquivos obrigatorios;
  - exposicao das funcoes exigidas;
  - cobertura administrativa minima do README;
  - cobertura estrutural dos 3 programas validos com base na AST;
  - funcionamento do CLI em caso valido.
- Atualizacao do README para apontar explicitamente para a auditoria de entrega.

### Validacoes realizadas neste checkpoint

- Suite automatizada completa executada com `python -m unittest discover -s tests -p "test_*.py" -v`:
  - 12 testes passando.
- Execucao manual do CLI com `tests/teste3.txt`.
- Atualizacao dos artefatos da ultima execucao em `generated/` e `docs/` com base em `tests/teste3.txt`.

### Arquivos principais impactados

- `tests/test_auditoria_entrega.py`
- `docs/auditoria-entrega.md`
- `README.md`

### Riscos ou pontos a observar

- A auditoria reduz muito o risco de falhas administrativas/estruturais, mas ainda nao substitui uma ultima revisao manual do repositorio publicado no GitHub.
- Ainda vale conferir visualmente se a organizacao do repositório e os nomes vistos no GitHub batem com o esperado pelo professor.

### Proximas tarefas do pipeline

- Fazer a revisao final olhando o repositorio como artefato publicado no GitHub.
- Verificar se ainda existe alguma exigencia administrativa externa ao codigo local.
- Fechar o proximo commit como checkpoint de endurecimento final da entrega.

## 2026-04-18 - Checkpoint 4

### Objetivo do checkpoint

Eliminar a dependencia manual de `PYTHONPATH` para que a execucao local e a suite automatizada fiquem mais robustas perante uma correcao por IA.

### Tarefas executadas

- Criacao de um pacote-raiz compativel em `analisador_sintatico_ll1/` para expor o codigo de `src/` sem exigir `PYTHONPATH`.
- Atualizacao do README para documentar comandos de execucao e teste sem configuracao manual de ambiente.
- Expansao de `tests/test_auditoria_entrega.py` para checar:
  - importacao do pacote principal sem `PYTHONPATH`;
  - execucao de um teste unitario via `python -m unittest` sem `PYTHONPATH`.
- Atualizacao de `docs/auditoria-entrega.md` para refletir o novo endurecimento do ambiente.

### Validacoes realizadas neste checkpoint

- Suite automatizada completa executada com `python -m unittest discover -s tests -p "test_*.py" -v`:
  - 14 testes passando.
- Importacao publica validada com `python -c "import analisador_sintatico_ll1"`.
- Execucao como modulo validada com `python -m analisador_sintatico_ll1 tests/teste1.txt`.
- Atualizacao dos artefatos da ultima execucao em `generated/` e `docs/` com base em `tests/teste3.txt`.

### Arquivos principais impactados

- `analisador_sintatico_ll1/__init__.py`
- `analisador_sintatico_ll1/__main__.py`
- `tests/test_auditoria_entrega.py`
- `README.md`
- `docs/auditoria-entrega.md`

### Riscos ou pontos a observar

- O endurecimento assume execucao a partir da raiz do repositorio, que e justamente o fluxo esperado para a entrega local.
- Ainda vale uma ultima revisao humana do repositorio publicado antes do envio final.

### Proximas tarefas do pipeline

- Fazer uma auditoria final de acabamento olhando nomes, artefatos e documentacao como pacote de entrega.
- Decidir o ultimo checkpoint de encerramento, focado em revisao final e publicacao.

## 2026-04-19 - Checkpoint 5

### Objetivo do checkpoint

Consolidar um checklist final de entrega para deixar o repositorio mais autoexplicativo e facilitar uma revisao final humana ou automatizada.

### Tarefas executadas

- Criacao de `docs/checklist-entrega.md` com o mapeamento entre exigencias, arquivos e comandos de validacao.
- Atualizacao do README para apontar explicitamente para o checklist final.
- Atualizacao de `docs/plano-evolucao.md` para registrar o checklist como parte do fechamento.
- Expansao de `tests/test_auditoria_entrega.py` para verificar:
  - existencia do checklist final;
  - presenca do checklist no README;
  - cobertura minima do checklist sobre funcoes, docs, artefatos e comandos.

### Validacoes realizadas neste checkpoint

- Suite automatizada completa executada com `python -m unittest discover -s tests -p "test_*.py" -v`.
- Revisao do pacote de entrega a partir da raiz do repositorio, sem alterar o nucleo do analisador.

### Arquivos principais impactados

- `docs/checklist-entrega.md`
- `README.md`
- `docs/plano-evolucao.md`
- `tests/test_auditoria_entrega.py`

### Riscos ou pontos a observar

- O checklist melhora a rastreabilidade da entrega, mas ainda depende de os arquivos publicados no GitHub refletirem exatamente o estado local.

### Proximas tarefas do pipeline

- Fazer o ultimo checkpoint de encerramento com revisao final do repositorio publicado e orientacao de envio.
