import streamlit as st
import pandas as pd

st.title("Metrics")
st.write("Quality vs Latency vs Cost (placeholder)")
df = pd.DataFrame({
    "model": ["ollama/llama3.1", "openai/gpt-4o-mini"],
    "template": ["A", "B"],
    "overall_mean": [3.4, 3.9],
    "latency_p50_ms": [2200, 1800],
    "cost_usd": [0.00, 0.03],
})
st.dataframe(df)
st.write("Add Pareto frontier plot once real data is flowing.")
