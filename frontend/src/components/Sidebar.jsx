import { Link, useNavigate } from "react-router-dom";

function Sidebar() {

    const navigate = useNavigate();

    const logout = () => {

        localStorage.removeItem("token");
        localStorage.removeItem("username");
        localStorage.removeItem("role");

        navigate("/");
    };

    return (

        <div
            className="bg-dark text-white p-3"
            style={{
                width: "250px",
                minHeight: "100vh"
            }}
        >

            <h3>AI HR Analytics</h3>

            <hr />

            <ul className="nav flex-column">

                <li className="nav-item mb-2">
                    <Link
                        className="nav-link text-white"
                        to="/dashboard"
                    >
                        Dashboard
                    </Link>
                </li>

                <li className="nav-item mb-2">
                    <Link
                        className="nav-link text-white"
                        to="/employees"
                    >
                        Employees
                    </Link>
                </li>

                <li className="nav-item mb-2">
                    <Link
                        className="nav-link text-white"
                        to="/attendance"
                    >
                        Attendance
                    </Link>
                </li>

                <li className="nav-item mb-2">
                    <Link
                        className="nav-link text-white"
                        to="/performance"
                    >
                        Performance
                    </Link>
                </li>

                <li className="nav-item mb-2">
                    <Link
                        className="nav-link text-white"
                        to="/anomalies"
                    >
                        Anomalies
                    </Link>
                </li>

                <li className="nav-item mt-4">
                    <button
                        className="btn btn-danger"
                        onClick={logout}
                    >
                        Logout
                    </button>
                </li>

                <li className="nav-item mb-2">
                    <Link
                        className="nav-link text-white"
                        to="/upload"
                    >
                        Upload Data
                    </Link>
                </li>

            </ul>

        </div>
    );
}

export default Sidebar;