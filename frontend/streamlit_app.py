
import streamlit as st
import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.query_parser import parse_query
from app.retriever import retrieve_relevant_clauses
from app.decision_engine import make_decision
from app.document_loader import extract_text_from_pdf

st.set_page_config(page_title="Insurance LLM Query Engine", layout="centered")
st.title("📄 Insurance LLM Query Engine")

st.sidebar.header("Upload Insurance Document")
uploaded_file = st.sidebar.file_uploader("Upload a policy PDF", type=["pdf"])
if uploaded_file:
    file_path = f"data/policies/{uploaded_file.name}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.sidebar.success(f"Uploaded: {uploaded_file.name}")

st.markdown("### 🔍 Enter a Natural Language Query")
query = st.text_input("Example: 46-year-old male, knee surgery in Pune, 3-month-old policy")

if query:
    parsed = parse_query(query)
    clauses = retrieve_relevant_clauses(query)
    decision = make_decision(parsed, clauses)
    st.markdown("### ✅ Structured Decision Output")
    st.json(decision)
