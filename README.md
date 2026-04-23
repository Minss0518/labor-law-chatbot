# 📋 근로기준법 RAG 챗봇

근로기준법 PDF를 기반으로 질문에 답변하는 AI 챗봇입니다.

## 🛠 기술 스택

- **Backend**: FastAPI, LlamaIndex, ChromaDB
- **Frontend**: React, Vite
- **AI**: OpenAI GPT-4o-mini, text-embedding-3-small
- **평가**: RAGAS

## 💡 주요 기능

- 근로기준법 PDF 문서 기반 질의응답
- 벡터 유사도 검색으로 관련 조항 추출
- React 기반 채팅 UI

## 📊 chunk_size 실험 결과

동일한 질문으로 chunk_size별 충실도(Faithfulness)를 비교했습니다.

| chunk_size | 연차휴가 충실도 | 퇴직금 충실도 |
|-----------|--------------|------------|
| 512       | 0.0          | 0.7        |
| 1024      | **0.9**      | 0.7        |
| 2048      | 0.0          | 0.7        |

→ **chunk_size 1024가 최적값으로 선정**

## 🚀 실행 방법

### 백엔드
```bash
pip install -r requirements.txt
python ingest.py
uvicorn app.main:app --reload
```

### 프론트엔드
```bash
cd labor-law-frontend
npm install
npm run dev
```