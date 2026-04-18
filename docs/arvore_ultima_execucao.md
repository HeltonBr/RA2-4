# Arvore Sintatica da Ultima Execucao

```text
Program
  Statement[1] line=2
    MemoryWrite name=A
      Number value=4
  Statement[2] line=3
    MemoryWrite name=B
      Number value=2
  Statement[3] line=4
    MemoryWrite name=C
      Number value=1.5
  Statement[4] line=5
    BinaryOp operator=+
      MemoryRead name=A
      MemoryRead name=B
  Statement[5] line=6
    MemoryWrite name=D
      BinaryOp operator=+
        MemoryRead name=A
        MemoryRead name=B
  Statement[6] line=7
    BinaryOp operator=^
      MemoryRead name=A
      Number value=2
  Statement[7] line=8
    BinaryOp operator=*
      MemoryRead name=A
      MemoryRead name=B
  Statement[8] line=9
    BinaryOp operator=/
      MemoryRead name=A
      MemoryRead name=B
  Statement[9] line=10
    BinaryOp operator=|
      MemoryRead name=A
      MemoryRead name=C
  Statement[10] line=11
    BinaryOp operator=%
      MemoryRead name=A
      MemoryRead name=B
  Statement[11] line=12
    Sequence
      IfElse
        Condition
          RelationalOp operator=<
            MemoryRead name=A
            MemoryRead name=B
        Then
          MemoryWrite name=A
            BinaryOp operator=+
              MemoryRead name=A
              Number value=1
        Else
          MemoryWrite name=B
            BinaryOp operator=+
              MemoryRead name=B
              Number value=1
      MemoryWrite name=OUT
        ResultRef offset=2
  Statement[12] line=13
    Sequence
      While
        Condition
          RelationalOp operator=>
            MemoryRead name=A
            Number value=0
        Body
          MemoryWrite name=A
            BinaryOp operator=-
              MemoryRead name=A
              Number value=1
      MemoryWrite name=OUT
        BinaryOp operator=+
          MemoryRead name=OUT
          MemoryRead name=B
```
