import { useEffect, useRef } from "react";
import Message from "./Message.jsx";
import TypingIndicator from "./TypingIndicator.jsx";

export default function ChatBox({ messages, loading }) {
  const bottomRef = useRef(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, loading]);

  return (
    <div className="messages">
      {messages.map((msg, i) => (
        <Message key={i} role={msg.role} content={msg.content} />
      ))}
      {loading && <TypingIndicator />}
      <div ref={bottomRef} />
    </div>
  );
}
