# Roteiro de Defesa

Este roteiro organiza uma apresentacao objetiva da Fase 2 e considera que a defesa ocorrera nos dias `29/04/2026` e `30/04/2026`.

## Regra operacional

- Ate `24/04/2026 23:59`, o trabalho oficial segue em `Github`.
- Apos o prazo, a pasta `Github` fica congelada.
- Qualquer treino, teste adicional, alteracao de arquivos e ensaio da defesa deve ocorrer apenas em `Githubmirror`.

## Objetivo da apresentacao

Demonstrar que a solucao:

- le o programa da linguagem da Fase 2;
- faz a analise sintatica LL(1);
- gera arvore sintatica;
- detecta erros de entrada;
- emite Assembly ARMv7 coerente com a AST.

## Preparacao antes da defesa

1. Trabalhar apenas na pasta `Githubmirror`.
2. Abrir um terminal na raiz de `Githubmirror`.
3. Deixar prontos estes arquivos:
   - `tests/teste1.txt`
   - `tests/teste3.txt`
   - `tests/invalidos/lexico_minusculo.txt`
   - `tests/invalidos/sintaxe_sem_end.txt`
4. Deixar aberto o arquivo `generated/ultimo_assembly.s`.
5. Se for usar simulador, deixar o CPULATOR pronto.

## Sequencia sugerida da defesa

### 1. Abertura rapida

- Mostrar `README.md`.
- Apontar:
  - identificacao da disciplina;
  - funcoes principais;
  - organizacao de `docs/`, `tests/` e `generated/`.

### 2. Execucao valida principal

Comando sugerido:

```powershell
python AnalisadorSintatico.py tests/teste3.txt
```

Pontos para mostrar:

- a execucao termina sem erro;
- os artefatos sao atualizados;
- existe arvore em `docs/arvore_ultima_execucao.md`;
- existe Assembly em `generated/ultimo_assembly.s`.

### 3. Mostrar a arvore sintatica

- Abrir `docs/arvore_ultima_execucao.md`.
- Explicar rapidamente:
  - `Program`;
  - `Statement`;
  - `BinaryOp`;
  - `If` ou `IfElse`;
  - `While`.

### 4. Mostrar alteracao de resultado

Durante a defesa, editar uma copia de `tests/teste3.txt` dentro de `Githubmirror`.

Sugestoes de alteracao:

- trocar valores iniciais de memoria;
- trocar um operador, como `+` por `*`;
- trocar um limite de comparacao no `WHILE`.

Depois, rodar novamente:

```powershell
python AnalisadorSintatico.py tests/teste3.txt
```

O objetivo e mostrar que:

- a analise continua valida;
- a arvore muda de acordo com a entrada;
- o Assembly tambem muda de forma coerente.

### 5. Demonstracao de erro detectado

Opcao de erro lexico:

```powershell
python AnalisadorSintatico.py tests/invalidos/lexico_minusculo.txt
```

Opcao de erro sintatico:

```powershell
python AnalisadorSintatico.py tests/invalidos/sintaxe_sem_end.txt
```

O que destacar:

- o programa detecta o erro;
- a mensagem e clara;
- nao aparece traceback bruto.

### 6. Demonstracao do Assembly ARMv7

Abrir `generated/ultimo_assembly.s` e explicar por blocos:

- `_start` como ponto de entrada;
- `const_*` como constantes numericas;
- `mem_*` como memoria simbólica;
- operacoes aritmeticas:
  - `vadd.f64`
  - `vsub.f64`
  - `vmul.f64`
  - `vdiv.f64`
  - `pow_double_int`
  - `intdiv_double`
  - `mod_double`
- estruturas de controle com labels de comparacao, `if` e `while`.

### 7. Parte opcional no CPULATOR

Se houver tempo:

- carregar o Assembly no CPULATOR ARMv7;
- mostrar alguns trechos e comentar os calculos;
- focar em um bloco pequeno, nao no arquivo inteiro.

## Arquivos mais recomendados por papel

- `tests/teste1.txt`: demonstracao valida mais simples.
- `tests/teste3.txt`: demonstracao valida mais rica para AST e Assembly.
- `tests/invalidos/lexico_minusculo.txt`: erro lexico.
- `tests/invalidos/sintaxe_sem_end.txt`: erro sintatico.

## Fechamento da fala

Uma forma boa de encerrar:

- a entrada foi reconhecida por uma gramatica LL(1);
- a AST foi montada corretamente;
- erros invalidos sao detectados;
- o Assembly ARMv7 e gerado a partir da arvore sintatica;
- a pasta oficial da entrega permaneceu congelada apos o prazo, e os ensaios ocorreram em `Githubmirror`.
