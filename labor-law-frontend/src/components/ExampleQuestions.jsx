import { EXAMPLE_QUESTIONS } from "../constants/index.jsx";

export default function ExampleQuestions({ onSelect, disabled }) {
  return (
    <div className="example-section">
      <div className="example-label">💡 자주 묻는 질문</div>
      <div className="example-grid">
        {EXAMPLE_QUESTIONS.map((q, i) => (
          <button
            key={i}
            className="example-btn"
            onClick={() => onSelect(q)}
            disabled={disabled}
          >
            {q}
          </button>
        ))}
      </div>
    </div>
  );
}
