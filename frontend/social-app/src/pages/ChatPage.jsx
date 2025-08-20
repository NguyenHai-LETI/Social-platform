import { useParams } from "react-router-dom";
import { useState } from "react";

export default function ChatPage() {
  const { userId } = useParams(); // ID user được click từ UserListPage
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const handleSend = () => {
    if (!input.trim()) return;
    setMessages([...messages, { sender: "me", text: input }]);
    setInput("");
    // TODO: Gửi message qua WebSocket hoặc API
  };

  return (
    <div className="flex flex-col h-screen p-4">
      <h2 className="text-lg font-bold mb-4">
        Chat với user ID: {userId}
      </h2>

      <div className="flex-1 border rounded-lg p-3 overflow-y-auto mb-4">
        {messages.map((msg, idx) => (
          <div
            key={idx}
            className={`p-2 rounded-lg mb-2 ${
              msg.sender === "me"
                ? "bg-blue-500 text-white self-end"
                : "bg-gray-200 text-black"
            }`}
          >
            {msg.text}
          </div>
        ))}
      </div>

      <div className="flex gap-2">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          className="flex-1 border rounded-lg px-3 py-2"
          placeholder="Nhập tin nhắn..."
        />
        <button
          onClick={handleSend}
          className="px-4 py-2 bg-green-500 text-white rounded-lg"
        >
          Gửi
        </button>
      </div>
    </div>
  );
}
