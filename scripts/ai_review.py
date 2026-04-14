"""Revisión automática con IA para práctica de EDA."""
import os
import json
import glob


def read_notebook():
    notebooks = glob.glob("notebook/*.ipynb")
    if not notebooks:
        return None
    with open(notebooks[0]) as f:
        nb = json.load(f)
    cells_text = []
    for i, cell in enumerate(nb["cells"]):
        source = "".join(cell.get("source", []))
        if source.strip():
            cells_text.append(f"[Celda {i + 1} ({cell['cell_type']})]:\n{source}")
    return "\n\n".join(cells_text)


def read_test_results():
    try:
        with open("test_output.txt") as f:
            return f.read()
    except FileNotFoundError:
        return "Sin resultados de tests"


def get_ai_feedback(notebook_content, test_results):
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        return "⚠️ No se configuró ANTHROPIC_API_KEY. Contacta al profesor."

    try:
        import anthropic
        client = anthropic.Anthropic(api_key=api_key)

        prompt = f"""Eres un profesor de Data Analytics revisando un EDA (Análisis Exploratorio
de Datos) de un alumno sobre un dataset de ecommerce.

El dataset tiene problemas de calidad intencionados:
- ~3% de nulos en shipping_region
- ~2% de order_ids duplicados
- Algunas cantidades negativas (errores)
- Outliers extremos en precios

Resultados de tests automáticos:
{test_results}

Contenido del notebook:
{notebook_content}

Evalúa (1-10 cada criterio):

1. **Detección de problemas de calidad** — ¿Encontró los nulos, duplicados, negativos y outliers?
2. **Visualizaciones** — ¿Son variadas, informativas y bien formateadas?
3. **Análisis bivariante** — ¿Exploró relaciones interesantes entre variables?
4. **Hallazgos** — ¿Son 5+? ¿Tienen evidencia y contexto de negocio?
5. **Resumen ejecutivo** — ¿Es claro, conciso y accionable?
6. **Calidad del código** — ¿Limpio, documentado, reproducible?

Feedback constructivo en español. Amable pero riguroso.
Termina con:
- **Nota global**: Suspenso / Aprobado / Notable / Sobresaliente
- **Consejo de mejora**: Una cosa concreta

Formato: Markdown."""

        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1500,
            messages=[{"role": "user", "content": prompt}],
        )
        return message.content[0].text
    except Exception as e:
        return f"⚠️ Error en revisión IA: {str(e)}"


def main():
    notebook_content = read_notebook()
    if not notebook_content:
        feedback = "⚠️ No se encontró el notebook."
    else:
        feedback = get_ai_feedback(notebook_content, read_test_results())

    with open("ai_feedback.md", "w") as f:
        f.write(feedback)
    print("AI feedback generated")


if __name__ == "__main__":
    main()
