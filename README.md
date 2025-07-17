
# InsureQueryAI - LLM-powered Insurance Decision System

This system uses OpenAI and LangChain to:
- Parse vague queries like "46M, knee surgery, 3-month policy"
- Retrieve relevant clauses from PDFs, Word Docs, or Emails using FAISS
- Make explainable approval/rejection decisions
- Log all decisions to SQLite for auditing

## How to Run
```
pip install -r requirements.txt
streamlit run frontend/streamlit_app.py
```

## Deployment
- Ready to deploy on Render using render.yaml and Dockerfile
