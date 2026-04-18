# Integrantes do grupo (ordem alfabetica):
# Helton Tessari Brandao - HeltonBr
#
# Nome do grupo no Canvas: RA2-4

from __future__ import annotations

from dataclasses import dataclass

from analisador_sintatico_ll1.ast_nodes import AstNode
from analisador_sintatico_ll1.ast_nodes import BinaryOpNode
from analisador_sintatico_ll1.ast_nodes import IfNode
from analisador_sintatico_ll1.ast_nodes import MemoryReadNode
from analisador_sintatico_ll1.ast_nodes import MemoryWriteNode
from analisador_sintatico_ll1.ast_nodes import NumberNode
from analisador_sintatico_ll1.ast_nodes import ProgramNode
from analisador_sintatico_ll1.ast_nodes import RelationalOpNode
from analisador_sintatico_ll1.ast_nodes import ResultRefNode
from analisador_sintatico_ll1.ast_nodes import SequenceNode
from analisador_sintatico_ll1.ast_nodes import StatementEntry
from analisador_sintatico_ll1.ast_nodes import WhileNode
from analisador_sintatico_ll1.ast_nodes import is_expression_node
from analisador_sintatico_ll1.ast_nodes import is_statement_node
from analisador_sintatico_ll1.grammar import GrammarBundle
from analisador_sintatico_ll1.tokens import Token
from analisador_sintatico_ll1.tokens import TokenType
from analisador_sintatico_ll1.tokens import flatten_token_lines
from analisador_sintatico_ll1.errors import SyntaxAnalysisError


@dataclass
class ParseResult:
    derivation: list[str]
    syntax_tree_seed: ProgramNode
    analysis_trace: list[str]


class TokenStream:
    def __init__(self, tokens: list[Token]) -> None:
        self.tokens = tokens
        self.index = 0

    def peek(self, offset: int = 0) -> Token:
        pos = min(self.index + offset, len(self.tokens) - 1)
        return self.tokens[pos]

    def advance(self) -> Token:
        token = self.peek()
        if self.index < len(self.tokens) - 1:
            self.index += 1
        return token

    def check(self, token_type: TokenType) -> bool:
        return self.peek().token_type == token_type

    def expect(self, token_type: TokenType, message: str) -> Token:
        token = self.peek()
        if token.token_type != token_type:
            raise SyntaxAnalysisError(
                f"{message} Encontrado {format_token_for_error(token)} na linha {token.line}, coluna {token.column}."
            )
        return self.advance()


class RecursiveDescentLL1Parser:
    def __init__(self, tokens: list[Token], grammar: GrammarBundle) -> None:
        self.stream = TokenStream(tokens)
        self.grammar = grammar
        self.derivation: list[str] = []
        self.analysis_trace: list[str] = []
        self.analysis_stack: list[str] = []
        self.statement_ordinal = 1

    def parse_program(self) -> ProgramNode:
        self._push("program")
        self._choose("program")
        self._parse_start_line()
        statements = self._parse_program_body()
        self._pop()
        return ProgramNode(statements=statements)

    def _parse_start_line(self) -> None:
        self._push("start_line")
        self._choose("start_line")
        self.stream.expect(TokenType.LPAREN, "Era esperado '(' para iniciar a linha START.")
        self.stream.expect(TokenType.KW_START, "Era esperado START.")
        self.stream.expect(TokenType.RPAREN, "Era esperado ')' apos START.")
        self.stream.expect(TokenType.EOL, "Era esperado fim de linha apos (START).")
        self._pop()

    def _parse_program_body(self) -> list[StatementEntry]:
        self._push("program_body")
        self._choose("program_body")
        opening = self.stream.expect(TokenType.LPAREN, "Era esperado '(' para iniciar uma linha do programa.")
        statements = self._parse_program_body_after_lparen(opening)
        self._pop()
        return statements

    def _parse_program_body_after_lparen(self, opening: Token) -> list[StatementEntry]:
        self._push("program_body_after_lparen")
        lookahead = self.stream.peek()
        if lookahead.token_type == TokenType.KW_END:
            self._choose("program_body_after_lparen")
            self.stream.advance()
            self.stream.expect(TokenType.RPAREN, "Era esperado ')' apos END.")
            self.stream.expect(TokenType.EOL, "Era esperado fim de linha apos (END).")
            self.stream.expect(TokenType.EOF, "Era esperado fim de arquivo apos (END).")
            self._pop()
            return []

        self._choose("program_body_after_lparen")
        node = self._parse_stmt_inner()
        self.stream.expect(TokenType.RPAREN, "Era esperado ')' para fechar a declaracao.")
        self.stream.expect(TokenType.EOL, "Era esperado fim de linha apos a declaracao.")
        entry = StatementEntry(
            ordinal=self.statement_ordinal,
            source_line=opening.line,
            node=node,
        )
        self.statement_ordinal += 1
        tail = self._parse_program_body()
        self._pop()
        return [entry, *tail]

    def _parse_stmt(self) -> AstNode:
        self._push("stmt")
        self._choose("stmt")
        opening = self.stream.expect(TokenType.LPAREN, "Era esperado '(' para iniciar a estrutura.")
        node = self._parse_stmt_inner()
        self.stream.expect(TokenType.RPAREN, "Era esperado ')' para fechar a estrutura.")
        self._pop()
        return self._with_fallback_position(node, opening)

    def _parse_stmt_inner(self) -> AstNode:
        self._push("stmt_inner")
        producao = self._choose("stmt_inner")
        if producao == ["IDENTIFIER"]:
            token = self.stream.expect(
                TokenType.IDENTIFIER,
                "Era esperado um identificador de memoria na forma canonica (MEM).",
            )
            node = MemoryReadNode(name=token.lexeme, line=token.line, column=token.column)
            self._pop()
            return node

        first = self._parse_item()
        node = self._parse_stmt_after_first(first)
        self._pop()
        return node

    def _parse_item(self) -> AstNode:
        self._push("item")
        producao = self._choose("item")
        if producao == ["NUMBER"]:
            token = self.stream.expect(TokenType.NUMBER, "Era esperado um numero.")
            assert token.numeric_value is not None
            node = NumberNode(
                value=token.numeric_value,
                lexeme=token.lexeme,
                line=token.line,
                column=token.column,
                is_integer_literal=token.is_integer_literal,
            )
            self._pop()
            return node

        node = self._parse_stmt()
        self._pop()
        return node

    def _parse_stmt_after_first(self, first: AstNode) -> AstNode:
        self._push("stmt_after_first")
        producao = self._choose("stmt_after_first")
        if producao == ["KW_RES"]:
            kw_token = self.stream.expect(TokenType.KW_RES, "Era esperado RES.")
            if not isinstance(first, NumberNode) or not first.is_integer_literal or first.value < 0:
                raise SyntaxAnalysisError(
                    f"RES exige um literal inteiro nao negativo na linha {kw_token.line}, coluna {kw_token.column}."
                )
            node = ResultRefNode(offset=int(first.value), line=kw_token.line, column=kw_token.column)
            self._pop()
            return node

        if producao == ["IDENTIFIER"]:
            id_token = self.stream.expect(
                TokenType.IDENTIFIER,
                "Era esperado o nome da memoria de destino para o armazenamento.",
            )
            self._ensure_expression(first, id_token, "armazenamento em memoria")
            node = MemoryWriteNode(name=id_token.lexeme, value=first, line=id_token.line, column=id_token.column)
            self._pop()
            return node

        second = self._parse_item()
        node = self._parse_stmt_after_second(first, second)
        self._pop()
        return node

    def _parse_stmt_after_second(self, first: AstNode, second: AstNode) -> AstNode:
        self._push("stmt_after_second")
        producao = self._choose("stmt_after_second")

        if producao == ["binary_op"]:
            operator = self._parse_binary_op()
            self._ensure_expression(first, operator, "operacao aritmetica")
            self._ensure_expression(second, operator, "operacao aritmetica")
            node = BinaryOpNode(
                operator=operator.lexeme,
                left=first,
                right=second,
                line=operator.line,
                column=operator.column,
            )
            self._pop()
            return node

        if producao == ["relational_op"]:
            operator = self._parse_relational_op()
            self._ensure_expression(first, operator, "operacao relacional")
            self._ensure_expression(second, operator, "operacao relacional")
            node = RelationalOpNode(
                operator=operator.lexeme,
                left=first,
                right=second,
                line=operator.line,
                column=operator.column,
            )
            self._pop()
            return node

        if producao == ["KW_IF"]:
            operator = self.stream.expect(TokenType.KW_IF, "Era esperado IF.")
            self._ensure_expression(first, operator, "condicao do IF")
            self._ensure_statement(second, operator, "ramo do IF")
            node = IfNode(
                condition=first,
                then_branch=second,
                else_branch=None,
                line=operator.line,
                column=operator.column,
            )
            self._pop()
            return node

        if producao == ["KW_WHILE"]:
            operator = self.stream.expect(TokenType.KW_WHILE, "Era esperado WHILE.")
            self._ensure_expression(first, operator, "condicao do WHILE")
            self._ensure_statement(second, operator, "corpo do WHILE")
            node = WhileNode(condition=first, body=second, line=operator.line, column=operator.column)
            self._pop()
            return node

        if producao == ["KW_SEQ"]:
            operator = self.stream.expect(TokenType.KW_SEQ, "Era esperado SEQ.")
            self._ensure_statement(first, operator, "primeiro elemento do SEQ")
            self._ensure_statement(second, operator, "segundo elemento do SEQ")
            node = SequenceNode(first=first, second=second, line=operator.line, column=operator.column)
            self._pop()
            return node

        third = self._parse_item()
        operator = self.stream.expect(TokenType.KW_IFELSE, "Era esperado IFELSE.")
        self._ensure_expression(first, operator, "condicao do IFELSE")
        self._ensure_statement(second, operator, "ramo THEN do IFELSE")
        self._ensure_statement(third, operator, "ramo ELSE do IFELSE")
        node = IfNode(
            condition=first,
            then_branch=second,
            else_branch=third,
            line=operator.line,
            column=operator.column,
        )
        self._pop()
        return node

    def _parse_binary_op(self) -> Token:
        self._push("binary_op")
        self._choose("binary_op")
        token = self.stream.advance()
        if token.token_type not in {
            TokenType.OP_PLUS,
            TokenType.OP_MINUS,
            TokenType.OP_MULT,
            TokenType.OP_REAL_DIV,
            TokenType.OP_INT_DIV,
            TokenType.OP_MOD,
            TokenType.OP_POW,
        }:
            raise SyntaxAnalysisError(
                f"Operador aritmetico invalido '{token.lexeme}' na linha {token.line}, coluna {token.column}."
            )
        self._pop()
        return token

    def _parse_relational_op(self) -> Token:
        self._push("relational_op")
        self._choose("relational_op")
        token = self.stream.advance()
        if token.token_type not in {
            TokenType.OP_GT,
            TokenType.OP_LT,
            TokenType.OP_GTE,
            TokenType.OP_LTE,
            TokenType.OP_EQ,
            TokenType.OP_NEQ,
        }:
            raise SyntaxAnalysisError(
                f"Operador relacional invalido '{token.lexeme}' na linha {token.line}, coluna {token.column}."
            )
        self._pop()
        return token

    def _choose(self, nonterminal: str) -> list[str]:
        lookahead = self.stream.peek().token_type.name
        producao = self.grammar.parsing_table.get(nonterminal, {}).get(lookahead)
        if producao is None:
            token = self.stream.peek()
            raise SyntaxAnalysisError(self._build_prediction_error(nonterminal, token))
        self.derivation.append(f"{nonterminal} -> {' '.join(producao)}")
        self.analysis_trace.append(f"pilha={self.analysis_stack!r} lookahead={lookahead} producao={producao}")
        return producao

    def _push(self, symbol: str) -> None:
        self.analysis_stack.append(symbol)

    def _pop(self) -> None:
        self.analysis_stack.pop()

    def _ensure_expression(self, node: AstNode, token: Token, contexto: str) -> None:
        if not is_expression_node(node):
            raise SyntaxAnalysisError(
                f"A estrutura usada em {contexto} nao produz valor na linha {token.line}, coluna {token.column}."
            )

    def _ensure_statement(self, node: AstNode, token: Token, contexto: str) -> None:
        if not is_statement_node(node):
            raise SyntaxAnalysisError(
                f"O item usado em {contexto} precisa ser uma estrutura parentetizada na linha "
                f"{token.line}, coluna {token.column}."
            )

    def _with_fallback_position(self, node: AstNode, opening: Token) -> AstNode:
        if getattr(node, "line", None):
            return node
        setattr(node, "line", opening.line)
        setattr(node, "column", opening.column)
        return node

    def _build_prediction_error(self, nonterminal: str, token: Token) -> str:
        esperados = sorted(self.grammar.parsing_table.get(nonterminal, {}))
        esperado_legivel = ", ".join(esperados)

        if nonterminal == "program_body" and token.token_type == TokenType.EOF:
            return "Programa incompleto: faltou a linha final (END)."
        if token.token_type == TokenType.EOF:
            return (
                f"Fim inesperado de arquivo enquanto analisava {nonterminal}. "
                f"Esperado: {esperado_legivel}."
            )
        if nonterminal == "stmt_after_second":
            return (
                "Estrutura pos-fixada incompleta: apos dois itens era esperado um operador aritmetico, "
                "um operador relacional ou uma keyword de controle (IF, IFELSE, WHILE, SEQ). "
                f"Encontrado {format_token_for_error(token)} na linha {token.line}, coluna {token.column}."
            )
        if nonterminal == "stmt_after_first":
            return (
                "Estrutura pos-fixada incompleta: apos o primeiro item era esperado RES, um identificador "
                "de memoria de destino ou outro item para continuar a estrutura. "
                f"Encontrado {format_token_for_error(token)} na linha {token.line}, coluna {token.column}."
            )
        return (
            f"Nao ha producao LL(1) para {nonterminal} com lookahead {token.token_type.name} "
            f"na linha {token.line}, coluna {token.column}. Esperado: {esperado_legivel}."
        )


def parsear(tokens: list[list[Token]], tabela_ll1: GrammarBundle) -> ParseResult:
    fluxo = flatten_token_lines(tokens)
    parser = RecursiveDescentLL1Parser(fluxo, tabela_ll1)
    program = parser.parse_program()
    return ParseResult(
        derivation=parser.derivation,
        syntax_tree_seed=program,
        analysis_trace=parser.analysis_trace,
    )


def format_token_for_error(token: Token) -> str:
    if token.token_type == TokenType.EOF:
        return "fim de arquivo"
    if token.token_type == TokenType.EOL:
        return "fim de linha"
    return f"'{token.lexeme}'"
