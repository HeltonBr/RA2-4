# Integrantes do grupo (ordem alfabetica):
# Helton Tessari Brandao - HeltonBr
#
# Nome do grupo no Canvas: RA2-4

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from analisador_sintatico_ll1.ast_nodes import ProgramNode
from analisador_sintatico_ll1.ast_nodes import program_to_dict
from analisador_sintatico_ll1.ast_nodes import render_program_tree
from analisador_sintatico_ll1.codegen_arm import gerarAssembly
from analisador_sintatico_ll1.grammar import GrammarBundle
from analisador_sintatico_ll1.grammar import construirGramatica
from analisador_sintatico_ll1.parser_ll1 import ParseResult
from analisador_sintatico_ll1.parser_ll1 import parsear
from analisador_sintatico_ll1.tokens import Token
from analisador_sintatico_ll1.tokens import TokenType
from analisador_sintatico_ll1.tokens import lerTokens
from analisador_sintatico_ll1.tokens import salvar_tokens_em_arquivo


def gerarArvore(derivacao: ParseResult) -> dict[str, Any]:
    program = derivacao.syntax_tree_seed
    if not isinstance(program, ProgramNode):
        raise TypeError("ParseResult nao contem uma ProgramNode valida.")
    return {
        "program": program_to_dict(program),
        "tree_text": render_program_tree(program),
        "derivation": derivacao.derivation,
        "_ast": program,
    }


__all__ = [
    "GrammarBundle",
    "ParseResult",
    "Token",
    "TokenType",
    "construirGramatica",
    "gerarArvore",
    "gerarAssembly",
    "lerTokens",
    "parsear",
    "salvar_tokens_em_arquivo",
]
