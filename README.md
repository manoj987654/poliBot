# LLM Document Processing System

This project uses Large Language Models (LLMs) to process natural language queries and retrieve relevant information from unstructured documents (PDF, DOCX, EML).

## Features
- Parse free-text queries into structured data
- Load and process multiple document formats
- Semantic search using OpenAI embeddings + FAISS
- Decision-making with justification citing specific clauses

## Installation
```bash
git clone https://github.com/<your-username>/llm-document-processing.git
cd llm-document-processing
pip install -r requirements.txt
```
Set your OpenAI API key:
```bash
export OPENAI_API_KEY="your-key-here"
```

## Run
```bash
uvicorn app.main:app --reload
```
Open `http://127.0.0.1:8000/docs` to test API.
