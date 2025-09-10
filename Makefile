.PHONY: setup seed run rate build-dbt report test lint ci

setup:
	uv sync
	uv run playwright install
	uv run pre-commit install

seed:
	uv run python -m ui_eval_harness.runners.seed

run:
	uv run python -m ui_eval_harness.runners.experiment

rate:
	uv run streamlit run src/app/Home.py

build-dbt:
	export DBT_PROFILES_DIR=$(PWD)/dbt && uv run dbt build

report:
	uv run python -c "print('TODO: analysis pipeline -> docs/decision_memo.md')"

test:
	uv run pytest -q

lint:
	uv run ruff check .
	uv run black --check .

ci: lint test
