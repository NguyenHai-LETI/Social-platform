import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

export default function UserListPage() {
    const [users, setUsers] = useState([]);
    const navigate = useNavigate();

    useEffect(() => {
        // Get token from localStorage
        const token = localStorage.getItem("token");

        // Only fetch if a token exists
        if (token) {
            fetch("http://127.0.0.1:8000/api/api-view/list/", {
                method: "GET",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${token}`, // Send the access token
                },
            })
                .then((res) => {
                    // Check if the request was successful
                    if (!res.ok) {
                        if (res.status === 401) {
                            console.error("Authentication failed. Redirecting to login.");
                            navigate("/login");
                        }
                        throw new Error(`HTTP error! status: ${res.status}`);
                    }
                    return res.json();
                })
                .then((data) => setUsers(data))
                .catch((err) => console.error("Error fetching users:", err));
        } else {
            console.error("No authentication token found. Redirecting to login.");
            navigate("/login"); // Redirect to login if no token is found
        }
    }, [navigate]);

    return (
        <div className="p-6">
            <h2 className="text-xl font-semibold mb-4">Danh sách người dùng</h2>
            <div className="flex flex-wrap gap-2">
                {users.map((user) => (
                    <button
                        key={user.id}
                        onClick={() => navigate(`/chat/${user.id}`)}
                        className="px-3 py-2 bg-gray-200 rounded-lg hover:bg-gray-300"
                    >
                        {user.username}
                    </button>
                ))}
            </div>
        </div>
    );
}
