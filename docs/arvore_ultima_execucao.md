# Arvore Sintatica da Ultima Execucao

```text
Program
  Statement[1] line=2
    MemoryWrite name=X
      Number value=10
  Statement[2] line=3
    MemoryWrite name=Y
      Number value=3
  Statement[3] line=4
    BinaryOp operator=+
      MemoryRead name=X
      MemoryRead name=Y
  Statement[4] line=5
    BinaryOp operator=-
      MemoryRead name=X
      Number value=2
  Statement[5] line=6
    BinaryOp operator=*
      MemoryRead name=X
      Number value=2
  Statement[6] line=7
    BinaryOp operator=/
      Number value=9
      Number value=2
  Statement[7] line=8
    BinaryOp operator=|
      Number value=9.0
      Number value=2.0
  Statement[8] line=9
    BinaryOp operator=%
      Number value=9
      Number value=4
  Statement[9] line=10
    BinaryOp operator=^
      MemoryRead name=X
      Number value=2
  Statement[10] line=11
    If
      Condition
        ResultRef offset=1
      Then
        Sequence
          MemoryWrite name=Z
            Number value=5
          BinaryOp operator=+
            MemoryRead name=Z
            MemoryRead name=Y
  Statement[11] line=12
    Sequence
      While
        Condition
          RelationalOp operator=>
            MemoryRead name=X
            Number value=0
        Body
          MemoryWrite name=X
            BinaryOp operator=-
              MemoryRead name=X
              Number value=1
      MemoryWrite name=Y
        BinaryOp operator=+
          MemoryRead name=Y
          Number value=1
```
