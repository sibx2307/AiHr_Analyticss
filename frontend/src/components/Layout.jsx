import Layout from "../components/Layout";
import Sidebar from "./Sidebar";

function Layout({ children }) {

    return (

        <div className="d-flex">

            <Sidebar />

            <div
                className="container-fluid p-4"
            >
                {children}
            </div>

        </div>
    );
}

export default Layout;