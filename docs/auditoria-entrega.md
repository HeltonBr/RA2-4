# Auditoria Automatizada da Entrega

Este arquivo resume as checagens automatizadas adicionadas para aproximar a validacao local do comportamento esperado de uma correcao por IA.

## O que a auditoria verifica

- Existencia e nao-vazio dos arquivos obrigatorios de entrega.
- Presenca das funcoes exigidas no enunciado:
  - `lerTokens`
  - `construirGramatica`
  - `parsear`
  - `gerarArvore`
  - `gerarAssembly`
- Presenca do ponto de entrada `AnalisadorSintatico.py`.
- Importacao do pacote principal e execucao de teste unitario sem depender de `PYTHONPATH` manual.
- Compatibilidade de import a partir da raiz do repositorio por meio do pacote `analisador_sintatico_ll1/`.
- Cobertura administrativa minima do `README.md`:
  - instituicao;
  - ano;
  - disciplina;
  - professor;
  - grupo;
  - instrucoes de execucao;
  - instrucoes de depuracao.
- Cobertura estrutural dos 3 arquivos de teste validos, analisada sobre a AST:
  - pelo menos 10 linhas uteis;
  - operadores `+ - * | / % ^`;
  - leitura e escrita de memoria;
  - uso de `RES`;
  - pelo menos uma decisao;
  - pelo menos um laço;
  - literais inteiros e reais.
- Funcionamento do CLI em caso valido e retorno limpo em casos de erro.

## Suite responsavel

As checagens ficam principalmente em:

- `tests/test_fase2_pipeline.py`
- `tests/test_auditoria_entrega.py`

## Comando de execucao

```powershell
python -m unittest discover -s tests -p "test_*.py" -v
```
