export default function Header({ onReset, isDark, onToggleDark }) {
  return (
    <header className="header">
      <div className="header-inner">
        <div className="logo">
          <span className="logo-icon">⚖️</span>
          <div>
            <div className="logo-title">근로기준법 챗봇</div>
            <div className="logo-sub">Labor Standards Act AI Assistant</div>
          </div>
        </div>
        <div className="header-actions">
          <button className="icon-btn" onClick={onReset} title="대화 초기화">
            🔄
          </button>
          <button className="icon-btn" onClick={onToggleDark} title="다크모드 전환">
            {isDark ? "☀️" : "🌙"}
          </button>
        </div>
      </div>
    </header>
  );
}
