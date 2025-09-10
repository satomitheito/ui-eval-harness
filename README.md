# UI Evaluation Harness (Figma‑style UI Generation)

A compact, hiring‑ready project that evaluates how well different model+prompt strategies convert natural‑language UI specs into working UIs. Includes:
- Streamlit rater UI (human‑in‑the‑loop)
- Auto‑checks (responsiveness, a11y) with Playwright
- DuckDB + dbt models (clean marts for analysis)
- Experiment runner with data contracts
- CI (ruff/black/tests)

## Quickstart

```bash
# 1) Install uv (if not already): https://docs.astral.sh/uv/
# 2) Sync deps
uv sync

# 3) Install Playwright browsers
uv run playwright install

# 4) Initialize pre-commit
uv run pre-commit install

# 5) Launch the rater/dashboard app
uv run streamlit run src/app/Home.py
```

Run dbt (DuckDB):
```bash
# set profiles dir for dbt to use the repo profile
export DBT_PROFILES_DIR=$(pwd)/dbt
uv run dbt debug
uv run dbt build
```

Run tests & linters:
```bash
uv run ruff check .
uv run black --check .
uv run pytest -q
```

## Project structure
See the repo tree in this README and within source files for detailed comments.
