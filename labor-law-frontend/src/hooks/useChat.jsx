import { useState } from "react";
import { API_URL } from "../constants/index.jsx";

const INITIAL_MESSAGE = {
  role: "bot",
  content: "안녕하세요! 근로기준법 챗봇입니다. 근로기준법에 관한 궁금한 점을 자유롭게 질문해 주세요.",
};

export function useChat() {
  const [messages, setMessages] = useState([INITIAL_MESSAGE]);
  const [loading, setLoading] = useState(false);

  const sendMessage = async (question) => {
    if (!question.trim() || loading) return;

    setMessages((prev) => [...prev, { role: "user", content: question }]);
    setLoading(true);

    try {
      const res = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question }),
      });
      const data = await res.json();
      setMessages((prev) => [...prev, { role: "bot", content: data.answer }]);
    } catch {
      setMessages((prev) => [
        ...prev,
        {
          role: "bot",
          content: "서버 연결에 실패했습니다. 서버가 실행 중인지 확인해 주세요.",
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  const resetChat = () => {
    setMessages([INITIAL_MESSAGE]);
  };

  return { messages, loading, sendMessage, resetChat };
}
