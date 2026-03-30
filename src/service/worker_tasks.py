from src.service.ingestion import process_pdf
from dotenv import load_dotenv

load_dotenv()

def process_pdf_job(file: str):
    return process_pdf(file)