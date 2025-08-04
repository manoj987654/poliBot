from fastapi import FastAPI, UploadFile
from app.query_parser import parse_query
from app.doc_loader import load_and_index_docs
from app.embeddings_store import retrieve_relevant_clauses
from app.decision_maker import make_decision

app = FastAPI()

@app.post("/process_query/")
async def process_query(query: str, files: list[UploadFile] = None):
    structured_query = parse_query(query)
    if files:
        docs = [await f.read() for f in files]
        load_and_index_docs(docs)
    clauses = retrieve_relevant_clauses(structured_query)
    decision = make_decision(structured_query, clauses)
    return {"structured_query": structured_query, "decision": decision}
