# services/vector.py

from langchain_mistralai import MistralAIEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv
import os

load_dotenv()
MISTRAIL_API_KEY = os.getenv('MISTRAL_API_KEY')
print(MISTRAIL_API_KEY)

embeddings = MistralAIEmbeddings(model="mistral-embed")

vector_store = Chroma(
    collection_name="example",
    embedding_function=embeddings,
    chroma_cloud_api_key=os.getenv("CHROMA_API_KEY"),
    tenant=os.getenv("CHROMA_TENANT"),
    database=os.getenv("CHROMA_DATABASE"),
)