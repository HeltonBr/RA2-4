# Integrantes do grupo (ordem alfabetica):
# Helton Tessari Brandao - HeltonBr
#
# Nome do grupo no Canvas: RA2-4

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from analisador_sintatico_ll1.core import construirGramatica
from analisador_sintatico_ll1.core import gerarArvore
from analisador_sintatico_ll1.core import gerarAssembly
from analisador_sintatico_ll1.core import lerTokens
from analisador_sintatico_ll1.core import parsear
from analisador_sintatico_ll1.core import salvar_tokens_em_arquivo
from analisador_sintatico_ll1.errors import AnalisadorSintaticoError
from analisador_sintatico_ll1.grammar import salvar_documentacao_gramatica


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Analisador sintatico LL(1) para a linguagem RPN da Fase 2."
    )
    parser.add_argument("arquivo", type=Path, help="Arquivo de programa ou de tokens.")
    return parser


def executar_pipeline(arquivo: Path) -> Path:
    repo_root = Path(__file__).resolve().parents[2]
    generated_dir = repo_root / "generated"
    docs_dir = repo_root / "docs"

    tokens = lerTokens(arquivo)
    gramatica = construirGramatica()
    derivacao = parsear(tokens, gramatica)
    arvore = gerarArvore(derivacao)
    assembly = gerarAssembly(arvore)

    generated_dir.mkdir(parents=True, exist_ok=True)
    salvar_tokens_em_arquivo(tokens, generated_dir / "tokens_ultima_execucao.txt")
    (generated_dir / "arvore_ultima_execucao.json").write_text(
        json.dumps(arvore["program"], ensure_ascii=True, indent=2) + "\n",
        encoding="utf-8",
    )
    (generated_dir / "ultimo_assembly.s").write_text(assembly, encoding="utf-8")
    (docs_dir / "arvore_ultima_execucao.md").write_text(
        "# Arvore Sintatica da Ultima Execucao\n\n```text\n"
        + arvore["tree_text"].rstrip()
        + "\n```\n",
        encoding="utf-8",
    )
    salvar_documentacao_gramatica(gramatica, docs_dir)
    return generated_dir


def main() -> int:
    args = build_parser().parse_args()
    try:
        generated_dir = executar_pipeline(args.arquivo)
        print(f"Analise concluida para: {args.arquivo}")
        print(f"Artefatos atualizados em: {generated_dir}")
        return 0
    except AnalisadorSintaticoError as exc:
        print(f"Erro: {exc}", file=sys.stderr)
        return 1
    except Exception as exc:  # pragma: no cover - ultima barreira defensiva
        print(f"Erro inesperado: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
