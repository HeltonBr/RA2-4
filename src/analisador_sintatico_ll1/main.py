from __future__ import annotations

import argparse
from pathlib import Path

from analisador_sintatico_ll1.core import construirGramatica
from analisador_sintatico_ll1.core import gerarArvore
from analisador_sintatico_ll1.core import lerTokens
from analisador_sintatico_ll1.core import parsear


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Analisador sintatico LL(1) para a linguagem RPN da Fase 2."
    )
    parser.add_argument("arquivo", type=Path, help="Arquivo de programa ou de tokens.")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    tokens = lerTokens(args.arquivo)
    gramatica = construirGramatica()
    derivacao = parsear(tokens, gramatica)
    gerarArvore(derivacao)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
