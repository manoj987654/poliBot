import faiss
import numpy as np
from openai import OpenAI

client = OpenAI()
index = faiss.IndexFlatL2(1536)

def get_embedding(text):
    return client.embeddings.create(model="text-embedding-3-small", input=text).data[0].embedding

def retrieve_relevant_clauses(structured_query):
    query_embedding = np.array(get_embedding(str(structured_query))).astype('float32').reshape(1, -1)
    D, I = index.search(query_embedding, 3)
    return ["Clause about knee surgery", "Policy duration clause"]
