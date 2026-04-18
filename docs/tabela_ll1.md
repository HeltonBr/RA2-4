# Tabela LL(1)

| Nao-terminal | `EOF` | `EOL` | `IDENTIFIER` | `KW_END` | `KW_IF` | `KW_IFELSE` | `KW_RES` | `KW_SEQ` | `KW_START` | `KW_WHILE` | `LPAREN` | `NUMBER` | `OP_EQ` | `OP_GT` | `OP_GTE` | `OP_INT_DIV` | `OP_LT` | `OP_LTE` | `OP_MINUS` | `OP_MOD` | `OP_MULT` | `OP_NEQ` | `OP_PLUS` | `OP_POW` | `OP_REAL_DIV` | `RPAREN` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `program` |  |  |  |  |  |  |  |  |  |  | `start_line program_body` |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `start_line` |  |  |  |  |  |  |  |  |  |  | `LPAREN KW_START RPAREN EOL` |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `program_body` |  |  |  |  |  |  |  |  |  |  | `LPAREN program_body_after_lparen` |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `program_body_after_lparen` |  |  | `stmt_inner RPAREN EOL program_body` | `KW_END RPAREN EOL EOF` |  |  |  |  |  |  | `stmt_inner RPAREN EOL program_body` | `stmt_inner RPAREN EOL program_body` |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `stmt` |  |  |  |  |  |  |  |  |  |  | `LPAREN stmt_inner RPAREN` |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `stmt_inner` |  |  | `IDENTIFIER` |  |  |  |  |  |  |  | `item stmt_after_first` | `item stmt_after_first` |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `item` |  |  |  |  |  |  |  |  |  |  | `stmt` | `NUMBER` |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `stmt_after_first` |  |  | `IDENTIFIER` |  |  |  | `KW_RES` |  |  |  | `item stmt_after_second` | `item stmt_after_second` |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `stmt_after_second` |  |  |  |  | `KW_IF` |  |  | `KW_SEQ` |  | `KW_WHILE` | `item KW_IFELSE` | `item KW_IFELSE` | `relational_op` | `relational_op` | `relational_op` | `binary_op` | `relational_op` | `relational_op` | `binary_op` | `binary_op` | `binary_op` | `relational_op` | `binary_op` | `binary_op` | `binary_op` |  |
| `binary_op` |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | `OP_INT_DIV` |  |  | `OP_MINUS` | `OP_MOD` | `OP_MULT` |  | `OP_PLUS` | `OP_POW` | `OP_REAL_DIV` |  |
| `relational_op` |  |  |  |  |  |  |  |  |  |  |  |  | `OP_EQ` | `OP_GT` | `OP_GTE` |  | `OP_LT` | `OP_LTE` |  |  |  | `OP_NEQ` |  |  |  |  |
