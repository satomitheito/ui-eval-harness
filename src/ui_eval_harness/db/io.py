# Minimal DuckDB IO helpers (expand as needed)
from pathlib import Path
import duckdb
from typing import Any

def get_conn(db_path: Path = Path("data/duckdb/ui_eval.duckdb")):
    db_path.parent.mkdir(parents=True, exist_ok=True)
    return duckdb.connect(str(db_path))

def init_schema(conn: duckdb.DuckDBPyConnection):
    conn.execute("""    create table if not exists dim_models(
        model_id text primary key,
        family text,
        version text,
        provider text
    );
    create table if not exists dim_prompts(
        prompt_id text primary key,
        template_id text,
        category text,
        complexity int
    );
    create table if not exists fct_generation(
        gen_id text primary key,
        task_id text,
        model_id text,
        prompt_id text,
        started_at timestamp,
        duration_ms int,
        tokens_in int,
        tokens_out int,
        cost_usd double,
        output_path text
    );
    create table if not exists fct_evaluation(
        eval_id text primary key,
        gen_id text,
        rater_id text,
        design_score int,
        func_score int,
        a11y_issues int,
        failures text,
        notes text,
        created_at timestamp
    );
    """)
