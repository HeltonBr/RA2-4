from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

from analisador_sintatico_ll1 import construirGramatica
from analisador_sintatico_ll1 import lerTokens
from analisador_sintatico_ll1 import parsear
from analisador_sintatico_ll1.ast_nodes import BinaryOpNode
from analisador_sintatico_ll1.ast_nodes import IfNode
from analisador_sintatico_ll1.ast_nodes import MemoryReadNode
from analisador_sintatico_ll1.ast_nodes import MemoryWriteNode
from analisador_sintatico_ll1.ast_nodes import NumberNode
from analisador_sintatico_ll1.ast_nodes import ProgramNode
from analisador_sintatico_ll1.ast_nodes import RelationalOpNode
from analisador_sintatico_ll1.ast_nodes import ResultRefNode
from analisador_sintatico_ll1.ast_nodes import SequenceNode
from analisador_sintatico_ll1.ast_nodes import WhileNode
from analisador_sintatico_ll1.core import construirGramatica as construirGramaticaCore
from analisador_sintatico_ll1.core import gerarArvore
from analisador_sintatico_ll1.core import gerarAssembly
from analisador_sintatico_ll1.core import lerTokens as lerTokensCore
from analisador_sintatico_ll1.core import parsear as parsearCore


ROOT = Path(__file__).resolve().parents[1]
PROGRAMAS_VALIDOS = [ROOT / "tests" / nome for nome in ("teste1.txt", "teste2.txt", "teste3.txt")]
ARQUIVOS_OBRIGATORIOS = [
    ROOT / "README.md",
    ROOT / "AnalisadorSintatico.py",
    ROOT / "docs" / "gramatica.md",
    ROOT / "docs" / "first_follow.md",
    ROOT / "docs" / "tabela_ll1.md",
    ROOT / "docs" / "arvore_ultima_execucao.md",
    ROOT / "docs" / "auditoria-entrega.md",
    ROOT / "generated" / "tokens_ultima_execucao.txt",
    ROOT / "generated" / "arvore_ultima_execucao.json",
    ROOT / "generated" / "ultimo_assembly.s",
]


class AuditoriaEntregaTests(unittest.TestCase):
    def test_arquivos_obrigatorios_existentes_e_nao_vazios(self) -> None:
        for caminho in ARQUIVOS_OBRIGATORIOS:
            with self.subTest(arquivo=str(caminho.relative_to(ROOT))):
                self.assertTrue(caminho.exists(), f"Arquivo obrigatorio ausente: {caminho}")
                self.assertGreater(caminho.stat().st_size, 0, f"Arquivo vazio: {caminho}")

    def test_funcoes_exigidas_estao_expostas(self) -> None:
        self.assertTrue(callable(lerTokensCore))
        self.assertTrue(callable(construirGramaticaCore))
        self.assertTrue(callable(parsearCore))
        self.assertTrue(callable(gerarArvore))
        self.assertTrue(callable(gerarAssembly))

    def test_readme_cobre_itens_administrativos_minimos(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8").lower()

        self.assertIn("pontificia universidade catolica do parana", readme)
        self.assertIn("2026", readme)
        self.assertIn("linguagens formais e compiladores", readme)
        self.assertIn("frank coelho de alcantara", readme)
        self.assertIn("ra2-4", readme)
        self.assertIn("python analisadorsintatico.py", readme)
        self.assertIn("cpulator", readme)

    def test_cada_programa_valido_cobre_os_requisitos_minimos(self) -> None:
        for caminho in PROGRAMAS_VALIDOS:
            with self.subTest(programa=caminho.name):
                texto = caminho.read_text(encoding="utf-8")
                linhas_uteis = [linha for linha in texto.splitlines() if linha.strip()]
                self.assertGreaterEqual(len(linhas_uteis), 10)

                program = self._parse_program(caminho)
                inventario = self._inventariar_programa(program)

                self.assertTrue({"+", "-", "*", "|", "/", "%", "^"}.issubset(inventario["binary_ops"]))
                self.assertTrue(inventario["has_memory_read"])
                self.assertTrue(inventario["has_memory_write"])
                self.assertTrue(inventario["has_res"])
                self.assertTrue(inventario["has_if"])
                self.assertTrue(inventario["has_while"])
                self.assertTrue(inventario["has_integer_literal"])
                self.assertTrue(inventario["has_real_literal"])

    def test_cli_processa_programa_valido(self) -> None:
        resultado = subprocess.run(
            [sys.executable, "AnalisadorSintatico.py", str(PROGRAMAS_VALIDOS[0])],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )

        self.assertEqual(resultado.returncode, 0)
        self.assertIn("Analise concluida para:", resultado.stdout)
        self.assertIn("Artefatos atualizados em:", resultado.stdout)

    def test_import_publico_funciona_sem_py_path_externo(self) -> None:
        resultado = subprocess.run(
            [
                sys.executable,
                "-c",
                "import analisador_sintatico_ll1; print(','.join(analisador_sintatico_ll1.__all__))",
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )

        self.assertEqual(resultado.returncode, 0, resultado.stderr)
        self.assertIn("lerTokens", resultado.stdout)
        self.assertIn("gerarAssembly", resultado.stdout)

    def test_unittest_consegue_importar_sem_py_path_externo(self) -> None:
        resultado = subprocess.run(
            [
                sys.executable,
                "-m",
                "unittest",
                "tests.test_fase2_pipeline.Fase2PipelineTests.test_construir_gramatica_sem_conflitos",
                "-v",
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )

        self.assertEqual(resultado.returncode, 0, resultado.stderr)
        saida_combinada = f"{resultado.stdout}\n{resultado.stderr}".lower()
        self.assertIn("ok", saida_combinada)

    def _parse_program(self, caminho: Path) -> ProgramNode:
        tokens = lerTokens(caminho)
        bundle = construirGramatica()
        resultado = parsear(tokens, bundle)
        return resultado.syntax_tree_seed

    def _inventariar_programa(self, program: ProgramNode) -> dict[str, object]:
        inventario = {
            "binary_ops": set(),
            "has_memory_read": False,
            "has_memory_write": False,
            "has_res": False,
            "has_if": False,
            "has_while": False,
            "has_integer_literal": False,
            "has_real_literal": False,
        }
        for statement in program.statements:
            self._visitar(statement.node, inventario)
        return inventario

    def _visitar(self, node, inventario: dict[str, object]) -> None:
        if isinstance(node, NumberNode):
            if node.is_integer_literal:
                inventario["has_integer_literal"] = True
            else:
                inventario["has_real_literal"] = True
            return
        if isinstance(node, MemoryReadNode):
            inventario["has_memory_read"] = True
            return
        if isinstance(node, ResultRefNode):
            inventario["has_res"] = True
            return
        if isinstance(node, MemoryWriteNode):
            inventario["has_memory_write"] = True
            self._visitar(node.value, inventario)
            return
        if isinstance(node, BinaryOpNode):
            inventario["binary_ops"].add(node.operator)
            self._visitar(node.left, inventario)
            self._visitar(node.right, inventario)
            return
        if isinstance(node, RelationalOpNode):
            self._visitar(node.left, inventario)
            self._visitar(node.right, inventario)
            return
        if isinstance(node, SequenceNode):
            self._visitar(node.first, inventario)
            self._visitar(node.second, inventario)
            return
        if isinstance(node, IfNode):
            inventario["has_if"] = True
            self._visitar(node.condition, inventario)
            self._visitar(node.then_branch, inventario)
            if node.else_branch is not None:
                self._visitar(node.else_branch, inventario)
            return
        if isinstance(node, WhileNode):
            inventario["has_while"] = True
            self._visitar(node.condition, inventario)
            self._visitar(node.body, inventario)


if __name__ == "__main__":
    unittest.main()
