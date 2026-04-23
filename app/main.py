"""
main.py
FastAPI 서버 및 라우터 담당
RAG 로직은 rag.py, 모델은 semas.py 참고
"""

from contextlib import asynccontextmanager
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.schemas import ChatRequest, ChatResponse
from app import rag

load_dotenv()

query_engine = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    global query_engine
    print("🚀 RAG 엔진 초기화 중...")
    try:
        query_engine = rag.build_query_engine()
        print("✅ RAG 엔진 준비 완료!")
    except Exception as e:
        print(f"⚠️ 오류: {e}")
    yield
    print("🛑 서버 종료")


app = FastAPI(
    title="근로기준법 챗봇 API",
    description="근로기준법 PDF 기반 RAG 챗봇",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "근로기준법 챗봇 API ⚖️", "status": "running"}


@app.get("/health")
def health():
    return {"status": "ok", "engine_loaded": query_engine is not None}


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    if query_engine is None:
        raise HTTPException(status_code=503, detail="RAG 엔진이 준비되지 않았습니다.")
    answer = rag.query(query_engine, request.question)
    return ChatResponse(answer=answer)
