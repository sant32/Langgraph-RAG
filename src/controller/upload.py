from fastapi import APIRouter, File, UploadFile
import os
from src.service.ingestion import process_pdf
from src.service.queue import queue
from src.service.worker_tasks import process_pdf_job


UPLOAD_DIR = "uploads"
router = APIRouter()

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/")
async def upload_pdf(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)


    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    chunks = process_pdf(file_path)

    # enqueue job
    job = queue.enqueue(process_pdf_job, file_path)


    return {
        "message": "File uploaded and processed",
        "job_id": job.id
    }