"""
rag.py
LlamaIndex RAG 엔진 초기화 및 쿼리 담당
"""

import os
from llama_index.core import VectorStoreIndex, StorageContext, Settings
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI
import chromadb
from langsmith import traceable

CHROMA_DIR = "vectorstore/chroma_db"
COLLECTION_NAME = "labor_law"


def build_query_engine():
    """ChromaDB에서 인덱스를 불러와 쿼리 엔진 반환"""
    Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small")
    Settings.llm = OpenAI(model="gpt-4o-mini", temperature=0.2)

    chroma_client = chromadb.PersistentClient(path=CHROMA_DIR)
    chroma_collection = chroma_client.get_or_create_collection(COLLECTION_NAME)
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    index = VectorStoreIndex.from_vector_store(
        vector_store=vector_store,
        storage_context=storage_context,
    )

    query_engine = index.as_query_engine(
        similarity_top_k=4,
        response_mode="compact",
    )

    return query_engine

@traceable
def query(engine, question: str) -> str:
    """쿼리 엔진에 질문을 던지고 답변 문자열 반환"""
    response = engine.query(question)
    return str(response)
