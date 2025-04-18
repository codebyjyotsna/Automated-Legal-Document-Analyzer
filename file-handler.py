import os
from docx import Document
from PyPDF2 import PdfReader

def handle_uploaded_file(file):
    filename = file.filename.lower()

    if filename.endswith('.docx'):
        return extract_text_from_docx(file)
    elif filename.endswith('.pdf'):
        return extract_text_from_pdf(file)
    else:
        raise ValueError("Unsupported file type. Please upload a .docx or .pdf file.")

def extract_text_from_docx(file):
    doc = Document(file)
    return "\n".join([paragraph.text for paragraph in doc.paragraphs])

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    return "\n".join([page.extract_text() for page in reader.pages])
