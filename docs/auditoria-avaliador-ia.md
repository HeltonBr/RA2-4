# Auditoria do Padrao de Avaliacao por IA

Este arquivo registra a leitura dos relatorios de avaliacao automatizada de RA2, RA3 e RA4 usados como referencia para endurecer a entrega atual da Fase 2.

## Fontes analisadas

- `AVALIACAO_RA2-grupo-12.md`
- `avaliacao_RA3_Grupo_4.md`
- `avaliacao-RA4_Grupo_2.md`

## Padroes observados na avaliacao

- A avaliacao procura arquivos obrigatorios de forma literal, especialmente `README.md`, documentacao em markdown, artefatos gerados e arquivos de teste.
- A ausencia de FIRST/FOLLOW, tabela LL(1), gramatica formal ou arvore persistida gera penalizacao severa, mesmo quando o codigo aparenta funcionar.
- As funcoes pedidas no enunciado sao procuradas pelo nome, como `lerTokens`, `construirGramatica`, `parsear`, `gerarArvore` e `gerarAssembly`.
- Os tres arquivos principais de teste sao analisados individualmente; cada um precisa demonstrar operacoes, memoria, `RES`, decisao, laco, inteiros e reais.
- A ferramenta verifica execucao por linha de comando e valoriza mensagens de erro sem traceback.
- A avaliacao separa funcionalidade, organizacao, robustez e artefatos. Um projeto funcional pode perder muitos pontos se a documentacao ou os arquivos de saida estiverem incompletos.
- A ausencia de historico Git incremental foi apontada como risco recorrente nos relatorios antigos.
- Para Assembly, a avaliacao procura nao apenas geracao textual, mas tambem evidencia de execucao correta no simulador indicado.

## Medidas aplicadas nesta entrega

- `README.md` completo com instituicao, ano, disciplina, professor, integrante, grupo, execucao, depuracao e Cpulator.
- Funcoes exigidas expostas pelo pacote publico:
  - `lerTokens`
  - `construirGramatica`
  - `parsear`
  - `gerarArvore`
  - `gerarAssembly`
- Documentacao formal persistida:
  - `docs/gramatica.md`
  - `docs/first_follow.md`
  - `docs/tabela_ll1.md`
  - `docs/arvore_ultima_execucao.md`
- Artefatos finais persistidos:
  - `generated/tokens_ultima_execucao.txt`
  - `generated/arvore_ultima_execucao.json`
  - `generated/ultimo_assembly.s`
- Auditoria automatizada local em `tests/test_auditoria_entrega.py`.
- Testes principais validando que `teste1.txt`, `teste2.txt` e `teste3.txt` cobrem todos os requisitos minimos do enunciado.
- Testes adicionais em `tests/variacoes/` para validar espacos extras, tabs, comentarios, linhas em branco, aninhamento e `SEQ` com varias operacoes na mesma linha.
- Casos invalidos adicionais para erro lexico, expressao vazia e duas declaracoes de topo na mesma linha.
- Runtime ARMv7 corrigido e testado para saida legivel no `JTAG UART` do CPulator.
- Linha do tempo em `docs/linha-do-tempo.md` com checkpoints pequenos e commits objetivos.

## Riscos residuais assumidos

- O enunciado menciona pull requests de outros integrantes, mas esta entrega foi conduzida individualmente com autoria de Helton Tessari Brandao, conforme registrado no README e nos cabecalhos.
- A linguagem formal adotada usa leitura de memoria como `(MEM)` para preservar previsibilidade LL(1). Essa decisao esta documentada no README e na gramatica.
- Duas declaracoes completas no mesmo nivel e na mesma linha sao rejeitadas. A forma suportada para varias operacoes na mesma linha e o encadeamento por `SEQ`, mantendo uma declaracao de topo por linha, como o enunciado orienta.
