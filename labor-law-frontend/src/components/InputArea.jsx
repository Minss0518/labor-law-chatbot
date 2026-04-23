import { useState, useRef, useEffect } from "react";

export default function InputArea({ onSend, loading }) {
  const [input, setInput] = useState("");
  const inputRef = useRef(null);

  useEffect(() => {
    if (!loading) inputRef.current?.focus();
  }, [loading]);

  const handleSend = () => {
    if (!input.trim() || loading) return;
    onSend(input.trim());
    setInput("");
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  return (
    <div className="input-area">
      <textarea
        ref={inputRef}
        value={input}
        onChange={(e) => setInput(e.target.value)}
        onKeyDown={handleKeyDown}
        placeholder="근로기준법에 대해 질문하세요... (Enter로 전송)"
        className="textarea"
        rows={2}
        disabled={loading}
      />
      <button
        onClick={handleSend}
        disabled={loading || !input.trim()}
        className={`send-btn ${loading || !input.trim() ? "send-btn--disabled" : ""}`}
      >
        {loading ? "..." : "전송"}
      </button>
    </div>
  );
}
