
import pdfplumber
from docx import Document
import extract_msg

def extract_text_from_pdf(path):
    with pdfplumber.open(path) as pdf:
        return "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())

def extract_text_from_docx(path):
    doc = Document(path)
    return "\n".join(p.text for p in doc.paragraphs if p.text.strip())

def extract_text_from_msg(path):
    msg = extract_msg.Message(path)
    return msg.body

def extract_text(path):
    if path.endswith(".pdf"):
        return extract_text_from_pdf(path)
    elif path.endswith(".docx"):
        return extract_text_from_docx(path)
    elif path.endswith(".msg"):
        return extract_text_from_msg(path)
    else:
        raise ValueError("Unsupported file type: " + path)
