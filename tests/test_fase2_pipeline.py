from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from analisador_sintatico_ll1 import construirGramatica
from analisador_sintatico_ll1 import gerarArvore
from analisador_sintatico_ll1 import gerarAssembly
from analisador_sintatico_ll1 import lerTokens
from analisador_sintatico_ll1 import parsear
from analisador_sintatico_ll1.errors import LexicalTokenError
from analisador_sintatico_ll1.errors import SyntaxAnalysisError


ROOT = Path(__file__).resolve().parents[1]


class Fase2PipelineTests(unittest.TestCase):
    def test_construir_gramatica_sem_conflitos(self) -> None:
        bundle = construirGramatica()

        self.assertEqual(bundle.start_symbol, "program")
        self.assertIn("stmt_inner", bundle.productions)
        self.assertEqual(bundle.first["program"], {"LPAREN"})
        self.assertEqual(bundle.parsing_table["stmt_inner"]["IDENTIFIER"], ["IDENTIFIER"])
        self.assertEqual(bundle.parsing_table["stmt_after_second"]["KW_IF"], ["KW_IF"])

    def test_ler_tokens_serializados_aceita_formato_da_fase_1(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            arquivo = Path(tmp_dir) / "tokens.txt"
            arquivo.write_text(
                "\n".join(
                    [
                        "[LINHA 1]",
                        "type=LPAREN;lexeme=(;line=1;column=1;is_integer_literal=False",
                        "type=KW_START;lexeme=START;line=1;column=2;is_integer_literal=False",
                        "type=RPAREN;lexeme=);line=1;column=7;is_integer_literal=False",
                        "",
                        "[LINHA 2]",
                        "type=LPAREN;lexeme=(;line=2;column=1;is_integer_literal=False",
                        "type=NUMBER;lexeme=10;line=2;column=2;value=10.0;is_integer_literal=True",
                        "type=IDENTIFIER;lexeme=X;line=2;column=5;is_integer_literal=False",
                        "type=RPAREN;lexeme=);line=2;column=6;is_integer_literal=False",
                        "",
                    ]
                ),
                encoding="utf-8",
            )

            tokens = lerTokens(arquivo)

        self.assertEqual(len(tokens), 2)
        self.assertEqual(
            [token.token_type.name for token in tokens[0]],
            ["LPAREN", "KW_START", "RPAREN"],
        )
        self.assertEqual(tokens[1][1].numeric_value, 10.0)

    def test_programas_validos_parseiam_e_geram_assembly(self) -> None:
        for nome_arquivo in ["teste1.txt", "teste2.txt", "teste3.txt"]:
            with self.subTest(programa=nome_arquivo):
                caminho = ROOT / "tests" / nome_arquivo
                tokens = lerTokens(caminho)
                bundle = construirGramatica()
                resultado = parsear(tokens, bundle)
                arvore = gerarArvore(resultado)
                assembly = gerarAssembly(arvore)

                self.assertGreaterEqual(arvore["program"]["statement_count"], 10)
                self.assertIn("Program", arvore["tree_text"])
                self.assertIn("_start:", assembly)
                self.assertIn("puts_jtag", assembly)

    def test_parser_detecta_erro_lexico(self) -> None:
        caminho = ROOT / "tests" / "invalidos" / "lexico_minusculo.txt"

        with self.assertRaises(LexicalTokenError):
            lerTokens(caminho)

    def test_parser_detecta_erro_sintatico(self) -> None:
        caminho = ROOT / "tests" / "invalidos" / "sintaxe_sem_end.txt"
        tokens = lerTokens(caminho)
        bundle = construirGramatica()

        with self.assertRaises(SyntaxAnalysisError):
            parsear(tokens, bundle)


if __name__ == "__main__":
    unittest.main()
