import streamlit as st

st.set_page_config(page_title="UI Eval Harness", layout="wide")

st.title("UI Evaluation Harness — Figma-style UI Generation")
st.caption("Rater UI • Metrics • Admin")

st.markdown(
    """
**Welcome!** This app lets you:
1) Rate generated UIs against task specs (Design × Functionality).
2) View metrics (quality, latency, cost).
3) Administer tasks and prompts.
"""
)

st.subheader("Quick links")
st.page_link("pages/1_Rater.py", label="➡️ Rater")
st.page_link("pages/2_Metrics.py", label="📊 Metrics")
st.page_link("pages/3_Admin.py", label="🛠️ Admin")

st.info("Starter scaffold ready. Use `make setup` then `make rate` to launch.")
