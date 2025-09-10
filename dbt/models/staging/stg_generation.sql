{{ config(materialized='view') }}

-- Expose generation events (created by our Python init step)
select
  gen_id,
  task_id,
  model_id,
  prompt_id,
  started_at,
  duration_ms,
  tokens_in,
  tokens_out,
  cost_usd,
  output_path
from fct_generation