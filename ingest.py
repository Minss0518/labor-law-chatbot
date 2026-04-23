"""
ingest.py
LlamaIndex로 PDF 읽어서 ChromaDB에 저장
"""

import os
from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, StorageContext
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core import Settings
import chromadb
from llama_index.core.node_parser import SentenceSplitter

load_dotenv()

# ── 설정 ──────────────────────────────────────────────
PDF_DIR = "data"
CHROMA_DIR = "vectorstore/chroma_db"
COLLECTION_NAME = "labor_law"
# ──────────────────────────────────────────────────────

def main():
    print("📄 PDF 로딩 중...")
    documents = SimpleDirectoryReader(PDF_DIR).load_data()
    print(f"   총 {len(documents)}개 문서 로드 완료")  # "페이지" → "문서"

    # 임베딩 설정
    Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small")

    # ChromaDB 설정
    print("🔢 ChromaDB 설정 중...")
    os.makedirs(CHROMA_DIR, exist_ok=True)
    chroma_client = chromadb.PersistentClient(path=CHROMA_DIR)
    chroma_collection = chroma_client.get_or_create_collection(COLLECTION_NAME)
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    # 인덱스 생성 및 저장
    print("💾 인덱스 생성 중... (시간이 걸릴 수 있어요)")
    index = VectorStoreIndex.from_documents(
        documents,
        storage_context=storage_context,
    )
    print("✅ ChromaDB 저장 완료!")
    print("\n🎉 완료! 서버를 실행하세요: uvicorn main:app --reload")

if __name__ == "__main__":
    main()

Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small")
# Settings.transformations = [SentenceSplitter(chunk_size=512, chunk_overlap=50)]
Settings.transformations = [SentenceSplitter(chunk_size=1024, chunk_overlap=200)]
# Settings.transformations = [SentenceSplitter(chunk_size=2048, chunk_overlap=200)]