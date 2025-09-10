import streamlit as st
from pathlib import Path

st.title("Admin")
st.write("Seed tasks, manage prompts/models. (Placeholder controls)")

if st.button("Seed example tasks & goldens"):
    st.success("Seeded (stub). Run `make seed` for real seeding via Python module.")
