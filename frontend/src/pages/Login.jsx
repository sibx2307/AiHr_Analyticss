import { useState } from "react";
import { useNavigate } from "react-router-dom";

import API from "../api/api";

function Login() {

    const navigate = useNavigate();

    const [username, setUsername] = useState("");

    const [password, setPassword] = useState("");

    const handleLogin = async (e) => {

        e.preventDefault();

        try {

            const response = await API.post(
                "/login",
                {
                    username,
                    password
                }
            );

            localStorage.setItem(
                "token",
                response.data.access_token
            );

            navigate("/dashboard");

        } catch (error) {

            alert(
                "Invalid username or password"
            );
        }
    };

    return (

        <div
            className="container d-flex justify-content-center align-items-center"
            style={{ height: "100vh" }}
        >

            <div
                className="card p-4 shadow"
                style={{ width: "400px" }}
            >

                <h2 className="text-center mb-4">
                    AI HR Analytics
                </h2>

                <form onSubmit={handleLogin}>

                    <input
                        type="text"
                        placeholder="Username"
                        className="form-control mb-3"
                        value={username}
                        onChange={(e) =>
                            setUsername(
                                e.target.value
                            )
                        }
                    />

                    <input
                        type="password"
                        placeholder="Password"
                        className="form-control mb-3"
                        value={password}
                        onChange={(e) =>
                            setPassword(
                                e.target.value
                            )
                        }
                    />

                    <button
                        className="btn btn-primary w-100"
                    >
                        Login
                    </button>

                </form>

            </div>

        </div>
    );
}

export default Login;