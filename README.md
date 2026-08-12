# Data4CVLab

Data4CVLab is a learning and research workspace for data-centric computer vision, with a focus on object detection.

Repo-level agent instructions are defined in `AGENTS.md`. Read that file before changing project structure, learning materials, or code.

The working philosophy is:

```text
Problem -> Data -> Experiment -> Evaluation -> Explanation -> Iteration
```

## Repository Layout

```text
data/         Local datasets and derived data artifacts.
notebooks/    Exploratory learning, visualization, and analysis notebooks.
src/          Reusable Python package code.
scripts/      Repeatable command-line workflows.
configs/      Dataset, training, and evaluation configuration files.
experiments/  Per-experiment outputs, notes, and metrics.
reports/      Dataset reports, experiment reports, and error analysis.
docs/         Ontology, annotation policy, and curriculum notes.
tests/        Unit tests for reusable code.
```

## Working Rule

Use notebooks to explore and explain. Move stable logic into `src/data4cvlab/`, then call it from scripts or notebooks.

```text
Explore in notebook.
Stabilize into src/.
Run with scripts/.
Report in reports/.
```

## Environment

Recommended setup:

```bash
uv venv
uv pip install -e ".[dev]"
```

Alternative with standard Python:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```
