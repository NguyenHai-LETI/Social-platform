import { useState } from "react";
import { useNavigate } from "react-router-dom";

export default function LoginPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    // Gửi request login tới Django API (giả định /api/users/login/)
    try {
      const res = await fetch("http://127.0.0.1:8000/api/api-view/login/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password }),
      });
      if (res.ok) {
        const data = await res.json();

        // Save tokens to localStorage
        localStorage.setItem("token", data.token);
        localStorage.setItem("refresh_token", data.refresh_token);

        // Sau khi login thành công chuyển sang danh sách user
        navigate("/users");
      } else {
        alert("Sai tài khoản hoặc mật khẩu");
      }
    } catch (err) {
      console.error("Error:", err);
    }
  };

  return (
    <div>
      <h2>Đăng nhập</h2>
      <form onSubmit={handleLogin}>
        <div>
          <label>Tài khoản:</label>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
        </div>
        <div>
          <label>Mật khẩu:</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>
        <button type="submit">Đăng nhập</button>
      </form>
    </div>
  );
}
