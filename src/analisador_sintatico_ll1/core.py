# Integrantes do grupo (ordem alfabetica):
# TODO - username1
# TODO - username2
# TODO - username3
# TODO - username4
#
# Nome do grupo no Canvas: TODO

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto
from pathlib import Path
from typing import Any


class TokenType(Enum):
    LPAREN = auto()
    RPAREN = auto()
    NUMBER = auto()
    IDENTIFIER = auto()
    KW_START = auto()
    KW_END = auto()
    KW_RES = auto()
    KW_SEQ = auto()
    KW_IF = auto()
    KW_IFELSE = auto()
    KW_WHILE = auto()
    OP_PLUS = auto()
    OP_MINUS = auto()
    OP_MULT = auto()
    OP_REAL_DIV = auto()
    OP_INT_DIV = auto()
    OP_MOD = auto()
    OP_POW = auto()
    OP_GT = auto()
    OP_LT = auto()
    OP_GTE = auto()
    OP_LTE = auto()
    OP_EQ = auto()
    OP_NEQ = auto()


@dataclass(slots=True)
class Token:
    token_type: TokenType
    lexeme: str
    line: int
    column: int
    numeric_value: float | None = None
    is_integer_literal: bool = False


@dataclass(slots=True)
class GrammarBundle:
    productions: dict[str, list[list[str]]]
    first: dict[str, set[str]]
    follow: dict[str, set[str]]
    parsing_table: dict[str, dict[str, list[str]]]


@dataclass(slots=True)
class ParseResult:
    derivation: list[str]
    syntax_tree_seed: Any


def lerTokens(arquivo: str | Path) -> list[list[Token]]:
    raise NotImplementedError("Etapa 2: leitura de tokens ainda nao implementada.")


def construirGramatica() -> GrammarBundle:
    raise NotImplementedError("Etapa 3: construcao da gramatica ainda nao implementada.")


def parsear(tokens: list[list[Token]], tabela_ll1: GrammarBundle) -> ParseResult:
    raise NotImplementedError("Etapa 4: parser ainda nao implementado.")


def gerarArvore(derivacao: ParseResult) -> dict[str, Any]:
    raise NotImplementedError("Etapa 5: geracao da arvore ainda nao implementada.")


def gerarAssembly(arvore: dict[str, Any]) -> str:
    raise NotImplementedError("Etapa 7: geracao de Assembly ainda nao implementada.")
