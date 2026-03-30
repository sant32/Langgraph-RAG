from fastapi import APIRouter
from src.controller.graph_query import router as graph_query_router
from src.controller.upload import router as upload_router


router = APIRouter()

router.include_router(graph_query_router, prefix="/query", tags=["query"]) 
router.include_router(upload_router, prefix="/upload", tags=["upload"]) 