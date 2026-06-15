import { useEffect, useState } from "react";
import API from "../api/api";
import Layout from "../components/Layout";

function Dashboard() {

    const [stats, setStats] = useState({
        employees: 0,
        attendance: 0,
        performance: 0,
        anomalies: 0
    });

    useEffect(() => {
        fetchStats();
    }, []);

    const fetchStats = async () => {

        const response =
            await API.get(
                "/dashboard/stats"
            );

        setStats(
            response.data
        );
    };

    return (

        <Layout>

            <h2>Dashboard</h2>

            <div className="row mt-4">

                <div className="col-md-3">
                    <div className="card p-3">
                        <h5>Total Employees</h5>
                        <h2>{stats.employees}</h2>
                    </div>
                </div>

                <div className="col-md-3">
                    <div className="card p-3">
                        <h5>Attendance %</h5>
                        <h2>{stats.attendance}%</h2>
                    </div>
                </div>

                <div className="col-md-3">
                    <div className="card p-3">
                        <h5>Performance</h5>
                        <h2>{stats.performance}</h2>
                    </div>
                </div>

                <div className="col-md-3">
                    <div className="card p-3">
                        <h5>Anomalies</h5>
                        <h2>{stats.anomalies}</h2>
                    </div>
                </div>

            </div>

        </Layout>
    );
}

export default Dashboard;