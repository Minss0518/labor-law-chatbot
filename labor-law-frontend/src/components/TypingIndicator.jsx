export default function TypingIndicator() {
  return (
    <div className="message-row message-row--bot">
      <div className="avatar">⚖️</div>
      <div className="bubble bubble--bot">
        <div className="typing-dots">
          <span className="dot" style={{ animationDelay: "0s" }} />
          <span className="dot" style={{ animationDelay: "0.2s" }} />
          <span className="dot" style={{ animationDelay: "0.4s" }} />
        </div>
      </div>
    </div>
  );
}
