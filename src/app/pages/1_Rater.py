import streamlit as st
import duckdb, json, os
from pathlib import Path

st.title("Rater")
st.write("Rate a generated sample against the rubric. (Stub UI)")

# Placeholder controls
col1, col2 = st.columns(2)
with col1:
    st.text_area("Task brief", "Two-column signup with OAuth buttons...")
with col2:
    st.text_area("Acceptance criteria", "Email+password inputs; Google+GitHub buttons; responsive.")

st.subheader("Rendered Output (placeholder)")
st.components.v1.html("""
<html><body><h3>Generated UI preview</h3><button>Create account</button></body></html>
""", height=200)

design = st.slider("Design quality (1–5)", 1, 5, 3)
func = st.slider("Functional behavior (1–5)", 1, 5, 3)
a11y = st.number_input("Accessibility issues (count)", 0, 100, 0)
notes = st.text_area("Notes")

if st.button("Submit rating"):
    st.success("Saved (stub). Wire to DuckDB or Postgres next.")
