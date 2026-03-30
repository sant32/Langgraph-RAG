# services/ingestion.py

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.service.vector import vector_store



def process_pdf(path: str):
    docs = PyPDFLoader(path).load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=2100,
        chunk_overlap=500
    )

    chunks = splitter.split_documents(docs)

    clean_chunks = [
        d for d in chunks
        if d.page_content and d.page_content.strip()
    ]

    vector_store.add_documents(clean_chunks)

    return len(clean_chunks)