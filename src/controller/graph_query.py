from fastapi import APIRouter, Depends
from src.service.graph import app_graph
from pydantic import BaseModel

router = APIRouter()

class QueryRequest(BaseModel):
    question: str


@router.post("/")
def query(req: QueryRequest):

    state = {
        "question": req.question,
        "docs": [],
        "good_docs": [],
        "verdict": "",
        "reason": "",
        "strips": [],
        "kept_strips": [],
        "refined_context": "",
        "web_query": "",
        "web_docs": [],
        "answer": "",
    }

    result = app_graph.invoke(state)
    
    return {
        "answer": result["answer"],
        "verdict": result["verdict"]
    }