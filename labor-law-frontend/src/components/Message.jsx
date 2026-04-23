export default function Message({ role, content }) {
  const isUser = role === "user";

  return (
    <div className={`message-row ${isUser ? "message-row--user" : "message-row--bot"}`}>
      {!isUser && <div className="avatar">⚖️</div>}
      <div className={`bubble ${isUser ? "bubble--user" : "bubble--bot"}`}>
        {content}
      </div>
    </div>
  );
}
