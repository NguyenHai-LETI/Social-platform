import { useNavigate } from "react-router-dom";

export default function HomePage() {
  const navigate = useNavigate();

  return (
    <div className="flex flex-col items-center justify-center h-screen gap-4">
      <h1 className="text-2xl font-bold">Welcome to My App</h1>
      <button
        onClick={() => navigate("/register")}
        className="px-4 py-2 bg-blue-500 text-white rounded-lg"
      >
        Đăng ký
      </button>
      <button
        onClick={() => navigate("/login")}
        className="px-4 py-2 bg-green-500 text-white rounded-lg"
      >
        Đăng nhập
      </button>
    </div>
  );
}
