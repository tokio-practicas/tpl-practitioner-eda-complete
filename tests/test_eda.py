"""Tests automáticos para la práctica de EDA."""
import pytest
import subprocess
import json
import os

ROOT = os.path.dirname(os.path.dirname(__file__))


def run_notebook():
    return subprocess.run(
        [
            "jupyter", "nbconvert",
            "--to", "notebook", "--execute",
            "--ExecutePreprocessor.timeout=180",
            os.path.join(ROOT, "notebook", "practica_eda.ipynb"),
            "--output", "executed.ipynb",
        ],
        capture_output=True, text=True, cwd=ROOT,
    )


def get_notebook():
    with open(os.path.join(ROOT, "notebook", "executed.ipynb")) as f:
        return json.load(f)


def all_code(nb):
    return "\n".join("".join(c["source"]) for c in nb["cells"] if c["cell_type"] == "code")


def all_markdown(nb):
    return "\n".join("".join(c["source"]) for c in nb["cells"] if c["cell_type"] == "markdown")


class TestEDA:
    @pytest.fixture(autouse=True, scope="class")
    def execute(self):
        result = run_notebook()
        assert result.returncode == 0, f"Notebook no ejecuta: {result.stderr[:500]}"

    def test_no_errors(self):
        for cell in get_notebook()["cells"]:
            if cell["cell_type"] == "code":
                for out in cell.get("outputs", []):
                    assert out.get("output_type") != "error"

    def test_data_loaded(self):
        src = all_code(get_notebook())
        assert "ecommerce_transactions" in src or "read_csv" in src

    def test_null_analysis(self):
        src = all_code(get_notebook())
        assert "isnull" in src or "isna" in src or "info()" in src, (
            "No se analizaron valores nulos"
        )

    def test_duplicates_checked(self):
        src = all_code(get_notebook())
        assert "duplicated" in src or "drop_duplicates" in src, (
            "No se comprobaron duplicados"
        )

    def test_visualizations_present(self):
        src = all_code(get_notebook()).lower()
        viz = ["plot", "hist", "scatter", "boxplot", "heatmap", "bar", "countplot"]
        assert any(k in src for k in viz), "No se encontraron visualizaciones"

    def test_five_findings(self):
        md = all_markdown(get_notebook()).lower()
        count = md.count("hallazgo")
        assert count >= 5, f"Solo {count} hallazgos documentados, se necesitan 5+"

    def test_executive_summary_written(self):
        md = all_markdown(get_notebook())
        assert "resumen ejecutivo" in md.lower()
        # Check student replaced the placeholder
        assert "Escribe tu resumen" not in md, (
            "El resumen ejecutivo no se completó (placeholder sin reemplazar)"
        )
