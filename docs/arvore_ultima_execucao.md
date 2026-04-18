# Arvore Sintatica da Ultima Execucao

```text
Program
  Statement[1] line=2
    MemoryWrite name=M
      Number value=8
  Statement[2] line=3
    MemoryWrite name=N
      Number value=5
  Statement[3] line=4
    MemoryWrite name=R
      Number value=2.25
  Statement[4] line=5
    BinaryOp operator=-
      MemoryRead name=M
      MemoryRead name=N
  Statement[5] line=6
    BinaryOp operator=+
      MemoryRead name=M
      MemoryRead name=N
  Statement[6] line=7
    BinaryOp operator=*
      MemoryRead name=M
      MemoryRead name=N
  Statement[7] line=8
    BinaryOp operator=/
      MemoryRead name=M
      MemoryRead name=N
  Statement[8] line=9
    BinaryOp operator=|
      MemoryRead name=M
      MemoryRead name=R
  Statement[9] line=10
    BinaryOp operator=%
      MemoryRead name=M
      MemoryRead name=N
  Statement[10] line=11
    BinaryOp operator=^
      MemoryRead name=N
      Number value=3
  Statement[11] line=12
    If
      Condition
        RelationalOp operator=!=
          ResultRef offset=1
          Number value=0
      Then
        IfElse
          Condition
            RelationalOp operator=>
              MemoryRead name=M
              MemoryRead name=N
          Then
            MemoryWrite name=M
              BinaryOp operator=-
                MemoryRead name=M
                Number value=1
          Else
            MemoryWrite name=N
              BinaryOp operator=-
                MemoryRead name=N
                Number value=1
  Statement[12] line=13
    Sequence
      While
        Condition
          RelationalOp operator=>
            MemoryRead name=M
            Number value=0
        Body
          MemoryWrite name=M
            BinaryOp operator=-
              MemoryRead name=M
              Number value=1
      Sequence
        MemoryWrite name=KEEP
          ResultRef offset=1
        MemoryWrite name=R
          BinaryOp operator=+
            MemoryRead name=R
            Number value=1.0
```
