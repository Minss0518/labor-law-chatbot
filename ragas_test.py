import os
from dotenv import load_dotenv
from app.rag import build_query_engine
from langchain_openai import ChatOpenAI

load_dotenv()

# 테스트 질문 3개
test_questions = [
    "연차휴가는 며칠이나 받을 수 있나요?",
    "퇴직금은 언제 받을 수 있나요?",
    "최저임금은 얼마인가요?"
]

engine = build_query_engine()
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

results = []

for q in test_questions:
    response = engine.query(q)
    contexts = [node.text for node in response.source_nodes]
    answer = str(response)

    # GPT한테 직접 평가 요청
    eval_prompt = f"""
다음 질문, 답변, 참고문서를 보고 평가해줘.

질문: {q}
답변: {answer}
참고문서: {" ".join(contexts[:2])}

1. 충실도(0~1): 답변이 참고문서에 근거하는가?
2. 관련성(0~1): 답변이 질문에 적절한가?

숫자만 간단히 알려줘. 예시: 충실도: 0.9 / 관련성: 0.8
"""
    eval_result = llm.invoke(eval_prompt)
    results.append({
        "질문": q,
        "답변": answer,
        "평가": eval_result.content
    })

print("\n===== 평가 결과 =====")
for r in results:
    print(f"\n질문: {r['질문']}")
    print(f"답변: {r['답변'][:100]}...")
    print(f"평가: {r['평가']}")